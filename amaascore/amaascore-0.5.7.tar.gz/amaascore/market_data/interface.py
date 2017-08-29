from __future__ import absolute_import, division, print_function, unicode_literals

import json
import logging

from amaascore.config import ENVIRONMENT
from amaascore.core.amaas_model import json_handler
from amaascore.core.interface import Interface
from amaascore.market_data.utils import json_to_eod_price, json_to_fx_rate


class MarketDataInterface(Interface):

    def __init__(self, environment=ENVIRONMENT, logger=None, endpoint=None):
        self.logger = logger or logging.getLogger(__name__)
        super(MarketDataInterface, self).__init__(endpoint=endpoint, endpoint_type='market_data',
                                                  environment=environment)

    def persist_eod_prices(self, asset_manager_id, business_date, eod_prices, update_existing_prices=True):
        """

        :param asset_manager_id:
        :param business_date: The business date for which these are rates.  Not really needed, could be derived...
        :param eod_prices:
        :param update_existing_prices:
        :return:
        """
        self.logger.info('Persist EOD Prices - Asset Manager: %s - Business Date: %s', asset_manager_id, business_date)
        url = '%s/eod-prices/%s/%s' % (self.endpoint, asset_manager_id, business_date.isoformat())
        params = {'update_existing_prices': update_existing_prices}
        eod_prices_json = [eod_price.to_interface() for eod_price in eod_prices]
        response = self.session.post(url, params=params, json=eod_prices_json)
        if response.ok:
            eod_prices = [json_to_eod_price(eod_price) for eod_price in response.json()]
            return eod_prices
        else:
            self.logger.error(response.text)
            response.raise_for_status()

    def retrieve_eod_prices(self, asset_manager_id, business_date, asset_ids=None):
        self.logger.info('Retrieve EOD Prices - Asset Manager: %s - Business Date: %s', asset_manager_id, business_date)
        url = '%s/eod-prices/%s/%s' % (self.endpoint, asset_manager_id, business_date.isoformat())
        params = {'asset_ids': ','.join(asset_ids)} if asset_ids else {}
        response = self.session.get(url=url, params=params)
        if response.ok:
            eod_prices = [json_to_eod_price(eod_price) for eod_price in response.json()]
            self.logger.info('Returned %s EOD Prices.', len(eod_prices))
            return eod_prices
        else:
            self.logger.error(response.text)
            response.raise_for_status()

    def roll_prices(self, asset_manager_id, previous_date, asset_ids, update_existing_prices=False):
        url = '%s/roll-prices/%s' % (self.endpoint, asset_manager_id)
        params = {'update_existing_prices': update_existing_prices}
        json_body = json.loads(json.dumps({'previous_date': previous_date,
                                           'asset_ids': ','.join(asset_ids)}, default=json_handler))
        response = self.session.post(url=url, params=params, json=json_body)
        if response.ok:
            prices = [json_to_eod_price(price) for price in response.json()]
            self.logger.info('Rolled %s Prices.', len(prices))
            return prices
        else:
            self.logger.error(response.text)
            response.raise_for_status()

    def persist_fx_rates(self, asset_manager_id, business_date, fx_rates, update_existing_rates=True):
        """

        :param asset_manager_id:
        :param business_date: The business date for which these are rates.  Not really needed, could be derived...
        :param fx_rates:
        :param update_existing_rates:
        :return:
        """
        self.logger.info('Persist FX Rates - Asset Manager: %s - Business Date: %s', asset_manager_id, business_date)
        url = '%s/fx-rates/%s/%s' % (self.endpoint, asset_manager_id, business_date.isoformat())
        params = {'update_existing_rates': update_existing_rates}
        fx_rates_json = [fx_rate.to_interface() for fx_rate in fx_rates]
        response = self.session.post(url, params=params, json=fx_rates_json)
        if response.ok:
            fx_rates = [json_to_fx_rate(fx_rate) for fx_rate in response.json()]
            return fx_rates
        else:
            self.logger.error(response.text)
            response.raise_for_status()

    def retrieve_fx_rates(self, asset_manager_id, business_date, asset_ids=None):
        self.logger.info('Retrieve FX Rates - Asset Manager: %s - Business Date: %s', asset_manager_id, business_date)
        url = '%s/fx-rates/%s/%s' % (self.endpoint, asset_manager_id, business_date.isoformat())
        params = {'asset_ids': ','.join(asset_ids)} if asset_ids else {}
        response = self.session.get(url=url, params=params)
        if response.ok:
            fx_rates = [json_to_fx_rate(fx_rate) for fx_rate in response.json()]
            self.logger.info('Returned %s FX Rates.', len(fx_rates))
            return fx_rates
        else:
            self.logger.error(response.text)
            response.raise_for_status()

    def clear(self, asset_manager_id):
        """ This method deletes all the data for an asset_manager_id.
            It should be used with extreme caution.  In production it
            is almost always better to Inactivate rather than delete. """
        self.logger.info('Clear Market Data - Asset Manager: %s', asset_manager_id)
        url = '%s/clear/%s' % (self.endpoint, asset_manager_id)
        response = self.session.delete(url)
        if response.ok:
            eod_price_count = response.json().get('eod_price_count', 'Unknown')
            self.logger.info('Deleted %s EOD Prices.', eod_price_count)
            fx_rate_count = response.json().get('fx_rate_count', 'Unknown')
            self.logger.info('Deleted %s FX Rates.', fx_rate_count)
            return response.json()
        else:
            self.logger.error(response.text)
            response.raise_for_status()
