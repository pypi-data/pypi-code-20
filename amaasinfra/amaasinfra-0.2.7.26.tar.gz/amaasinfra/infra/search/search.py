import boto3
import json
import requests

class Search(object):
    def __init__(self, domain, endpoint):
        self._domain = domain 
        self._endpoint = endpoint

    def search(self):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def put_documents(self):
        raise NotImplementedError

    def delete_document(self):
        raise NotImplementedError

    def get_index(self):
        raise NotImplementedError

    def put_index(self):
        raise NotImplementedError

    def delete_index(self):
        raise NotImplementedError

    def get_type(self):
        raise NotImplementedError


class ElasticSearch(Search):
    """
    To further improve this, add cloudwatch here for non-200 status code response
    for delete/put methods
    """
    def __init__(self, domain, endpoint):
        super().__init__(domain, endpoint)

    def search(self, keywords, index, type='', keyward_operator='OR', filters=[], **kwargs):
        url = ''
        q = ''

        # if type parameter provided the search scope is set to type level
        # otherwise index level
        if type:
            url = '{}/{}/{}/_search'.format(self._endpoint, index, type)
        else:
            url = '{}/{}/_search'.format(self._endpoint, index)


        if kwargs.get('fuzzy', False):
            q = ' {} '.format(keyward_operator).join(['*{}*'.format(item) for item in keywords])
        else:
            q = ' {} '.format(keyward_operator).join(keywords)

        search_criterias={'query': {'query_string':{'default_operator': keyward_operator,
                                                    'query': q}}} 
        
        if filters:
            search_criterias['query']['query_string'].update({'fields': filters})

         # handle pagination if parameters provided
        if kwargs.get('page', None):
            search_criterias.update({'from': (kwargs.get('page')-1)*kwargs.get('page_size', 30)})
            search_criterias.update({'size': kwargs.get('page_size', 30)})  

        return json.loads(requests.post(url=url,
                                        data=json.dumps(search_criterias),
                                        headers={'Content-Type':'application/json'}).__dict__.get('_content')).get('hits')

    def update(self, document, index, type, id):
        url = '{}/{}/{}/{}'.format(self._endpoint, index, type, id)
        if requests.put(url=url,
                        data=json.dumps(document),
                        headers={'Content-Type':'application/json'}).__dict__.get('status_code') == 200:
            return True
        else:
            return False

    def put_documents(self, documents, id_name, index, type):
        url = '{}/{}/{}/_bulk?pretty'.format(self._endpoint, index, type)
        payload = ''
        for doc in documents:
            payload += json.dumps({ "index":  { "_index": index, "_type": type, "_id": doc.pop(id_name) }})
            payload += '\n'
            payload += json.dumps(doc)
            payload += '\n'

        if requests.put(url=url,
                        data=payload,
                        headers={'Content-Type':'application/json'}).__dict__.get('status_code') == 200:
            return True
        else:
            return False

    def delete_document(self, index, type, id):
        url = '{}/{}/{}/{}'.format(self._endpoint, index, type, id)
        if requests.delete(url=url).__dict__.get('status_code') == 200:
            return True
        else:
            return False

    def get_index(self, index):
        url = '{}/{}/_search'.format(self._endpoint, index)
        response = requests.get(url=url).__dict__

        if response.get('status', 404) == 404:
            return False

        return json.loads(response.get('_content')).get('hits')

    def put_index(self, index):
        if requests.put(url=''.join([self._endpoint, '/', index]),
                        headers={'Content-Type':'application/json'}).__dict__.get('status_code') == 200:
            return True
        else:
            return False

    def delete_index(self, index):
        if requests.delete(url=''.join([self._endpoint, '/', index])).__dict__.get('status_code') == 200:
            return True
        else:
            return False

    def get_type(self, index, type):
        url = '{}/{}/{}/_search'.format(self._endpoint, index, type)

        response = requests.get(url=url).__dict__

        if response.get('status', 404) == 404:
            return False

        return json.loads(response.get('_content')).get('hits')

class CloudSearch(Search):
    """
    This is for the implementation of AWS CloudSearch which built on top of Solr
    """
    def __init__(self, domain, endpoint):
        super().__init__(domain, endpoint)

    def search(self, keywords, index='', type=''):
        pass

    def update(self, document):
        pass

    def put_documents(self, documents, index, type):
        pass

    def get_index(self):
        pass

    def put_index(self, index):
        pass

    def delete_index(self, index):
        pass

    def get_type(self):
        pass

if __name__ == '__main__':
    es = ElasticSearch(domain='amaas',
                       endpoint='https://search-amaas-ff7lf5t5xoszxef72ojuasgaf4.ap-southeast-1.es.amazonaws.com')

    #print(es.put_index('test'))

    # es.put_documents([{'id': 999, 'display_name': 'display name for 999', 'description': 'description for 999'},
    #                   {'id': 1000, 'display_name': 'display name for 1000', 'description': 'description for 1000'}], index='assets', type='asset_references')
    # es.search(keywords=['name'], index='assets', fuzzy=True)
    # es.update({'display_name': 'test from update'}, 'assets', 'assets', 4564)
    # es.delete_index(index='assets')
    # print(es.get_index(index='assets'))