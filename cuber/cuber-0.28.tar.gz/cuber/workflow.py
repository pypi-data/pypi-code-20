import importlib
import copy
import json
import logging
from functools32 import lru_cache

logger = logging.getLogger(__name__)

class Workflow():
    def __init__(self, workflow_file = None, graph = None):
        '''
        Example:
        {
            'module': 'dcg_metric',
            'class': 'DCGMetric',
            'deps': [
                {
                    'prefix': 'model1',
                    'graph': {

                    }
                },
                {
                    'arg_name': 'data',
                    'graph': {
                        'module': 'lastfm_data',
                        'class': 'LastFMData',
                        'attrs': {
                            'short': False,
                        }
                    }
                }

            ]
        }
        '''
        if workflow_file is not None:
            with open(workflow_file) as f:
                graph_json = f.read()
            logger.debug('Graph json: {}'.format(graph_json))
            self.graph = json.loads(graph_json)
        elif isinstance(graph, basestring):
            graph_json = graph
            logger.debug('Graph json: {}'.format(graph_json))
            self.graph = json.loads(graph_json)
        else:
            self.graph = graph

    def get_graph(self, name):
        return self.graph[name]

    def run(self, disable_inmemory_cache = False, disable_file_cache = False):
        return self.__run_graph('main', disable_inmemory_cache = disable_inmemory_cache, disable_file_cache = disable_file_cache)

    def __run_graph(self, graph_, disable_inmemory_cache, disable_file_cache):
        '''
            TODO: improve excprions for incorrect graph
        '''
        logger.info('Graph to do: {}'.format(graph_))

        if isinstance(graph_, basestring): # this is graph name
            logger.info('Go to {}'.format(graph_))
            return self.__run_graph(self.get_graph(graph_), disable_inmemory_cache = disable_inmemory_cache, disable_file_cache = disable_file_cache)

        # required fields
        for key in {'module', 'class'}:
            assert key in graph_

        for key in graph_.keys():
            assert key in {'attrs', 'deps', 'class', 'module', 'comment'}

        attrs = copy.deepcopy(graph_.get('attrs', {}))
        for dep in graph_.get('deps', {}):
            for key in dep.keys():
                assert key in {'fields', 'graph', 'prefix', 'comment'}

            res = self.__run_graph(dep['graph'], disable_inmemory_cache = disable_inmemory_cache, disable_file_cache = disable_file_cache)
            if 'fields' not in dep:
                for key in res:
                    attr_key = dep.get('prefix', '') + key
                    if attr_key in attrs:
                        logger.error('Parameter for cube is not unique: {} at graph:\n{}'.format(attr_key, graph_))
                        raise ValueError('Graph configuration error')
                    attrs[attr_key] = res[key]
            else:
                for new_key, old_key in dep['fields'].iteritems():
                    attr_key = dep.get('prefix', '') + new_key
                    if attr_key in attrs:
                        logger.error('Parameter for cube is not unique: {} at graph:\n{}'.format(attr_key, graph_))
                        raise ValueError('Graph configuration error')
                    attrs[attr_key] = res[old_key]

        module = importlib.import_module(graph_['module'])
        logger.debug('Attrs keys: {}'.format(attrs.keys()))
        cube_init = getattr(module, graph_['class'])(**attrs)
        res = cube_init.get(
            disable_inmemory_cache = disable_inmemory_cache, 
            disable_file_cache = disable_file_cache
        )
        return res
