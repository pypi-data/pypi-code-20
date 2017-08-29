"""
Copyright 2013-2016 PhishMe, Inc.  All rights reserved.

This software is provided by PhishMe, Inc. ("PhishMe") on an "as is" basis and any express or implied warranties,
including but not limited to the implied warranties of merchantability and fitness for a particular purpose, are
disclaimed in all aspects.  In no event will PhishMe be liable for any direct, indirect, special, incidental or
consequential damages relating to the use of this software, even if advised of the possibility of such damage. Use of
this software is pursuant to, and permitted only in accordance with, the agreement between you and PhishMe.
"""

import base64
import json
import logging
import sys

from phishme_intelligence.core import intelligence
from phishme_intelligence.core import rest_api
from phishme_intelligence.core import sqlite
from phishme_intelligence.output.base_integration import BaseIntegration

# Determine the major version of python running this script.
PYTHON_MAJOR_VERSION = sys.version_info[0]


class CarbonBlack(BaseIntegration):

    def __init__(self, config, product):
        """

        :param config:
        :param product:
        :return:
        """

        super(CarbonBlack, self).__init__(config=config, product=product)

        self.logger = logging.getLogger(__name__)

        self.rest_api = rest_api.RestApi(config=self.config, product=self.product)

        self.sqlite = sqlite.SQLite(location=config.get(self.product, 'sqlite_location'),
                                    data_retention_days=config.get(self.product, 'sqlite_data_retention_days'))
        self.headers = {'X-Auth-Token': config.get(self.product, 'api_token')}

        self.reports = []

    def process(self, mrti, threat_id):
        """

        :param mrti:
        :param threat_id:
        :return:
        """

        # Add MRTI to sqlite.
        self.sqlite.add_threat_id(intel=mrti)

    def post_run(self, config_file_location):
        """
        Pull threats out of a sqlite db, create a feed file, and synchronize it with Carbon Black.

        :param config_file_location:
        :return:
        """

        # Get threats out of db and format them for CB.
        for json_data in self.sqlite.get_threats():
            intel = intelligence.Malware(json_data)

            self._create_report(mrti=intel)

        # Write CB-formatted data.
        self._write_feed_object()

        # Check if an ID exists or not. If it does not, then pause here and tell the user to add the feed in the CB GUI.
        if not self.config.get(self.product, 'feed_id'):

            # Sleep here and wait for positive feedback that the feed has been added.
            response = 'not yet'
            while response != 'done':

                # Message to solicit user input.
                message = 'Please go to your CB GUI and configure this feed. You should enter the correct URI to point to ' + \
                          self.config.get(self.product, 'cb_feed') + \
                          '. When complete, please type \'done\' to continue.'

                if PYTHON_MAJOR_VERSION == 3:
                    response = input(message)
                else:
                    response = raw_input(message)

            # User has signified that they did set up the PhishMe Intelligence feed in their Carbon Black instance.
            self._feed_extract_id(config_file_location=config_file_location)

        # Since the feed_id was found, just need to synchronize.
        self._feed_synchronize()

    def _write_feed_object(self):
        """
        Write all the reports to a feed file.

        :param config:
        :return:
        """

        with open('pm_lib_intel/output/product/carbon_black/phishme_logo.png', 'rb') as icon_file:
            icon_base64 = base64.b64encode(icon_file.read())

        with open('pm_lib_intel/output/product/carbon_black/phishme_logo_small.png', 'rb') as icon_small_file:
            icon_small_base64 = base64.b64encode(icon_small_file.read())

        feed = {}

        feed_info = {}
        feed_info.update(name=self.config.get(self.product, 'feed_name'))
        feed_info.update(display_name='PhishMe Intelligence')
        feed_info.update(provider_url='http://phishme.com')
        feed_info.update(summary='PhishMe Intelligence is a reliable and timely way to stop dangerous phishing attacks.')
        feed_info.update(tech_data='This feed may not be shared outside your organization.')
        feed_info.update(category='Connectors')
        feed_info.update(icon=icon_base64.decode('utf8'))
        feed_info.update(icon_small=icon_small_base64.decode('utf8'))

        feed.update(feedinfo=feed_info)
        feed.update(reports=self.reports)

        self._write_cb_feed(feed)

    def _write_cb_feed(self, feed):
        """
        Write feed file to disk.

        :param feed:
        :return:
        """
        with open(self.config.get(self.product, 'cb_feed'), 'w+') as file_handler:
            file_handler.write(json.dumps(feed, indent=4, sort_keys=True))

    def _create_report(self, mrti):
        """

        :param mrti:
        :return:
        """

        report_base = {}
        report_base['iocs'] = {}
        report_base.update(timestamp=int(round(mrti.last_published / 1e3)))
        report_base.update(link=mrti.active_threat_report)

        # Copy basic report object to impact-specific report objects.
        report_major = report_base.copy()
        report_moderate = report_base.copy()
        report_minor = report_base.copy()
        report_none = report_base.copy()

        ipv4_major, ipv4_moderate, ipv4_minor, ipv4_none, dns_major, dns_moderate, dns_minor, dns_none, md5_major, md5_none = ([] for i in range(10))

        # Loop through blockset to extract all impact ratings and IOC types.
        for item in mrti.block_set:

            if item.block_type == 'Domain Name' and item.impact == 'Major':
                dns_major.append(item.watchlist_ioc)
            elif item.block_type == 'Domain Name' and item.impact == 'Moderate':
                dns_moderate.append(item.watchlist_ioc)
            elif item.block_type == 'Domain Name' and item.impact == 'Minor':
                dns_minor.append(item.watchlist_ioc)
            elif item.block_type == 'Domain Name' and item.impact == 'None':
                dns_none.append(item.watchlist_ioc)
            elif item.block_type == 'IPv4 Address' and item.impact == 'Major':
                ipv4_major.append(item.watchlist_ioc)
            elif item.block_type == 'IPv4 Address' and item.impact == 'Moderate':
                ipv4_moderate.append(item.watchlist_ioc)
            elif item.block_type == 'IPv4 Address' and item.impact == 'Minor':
                ipv4_minor.append(item.watchlist_ioc)
            elif item.block_type == 'IPv4 Address' and item.impact == 'None':
                ipv4_none.append(item.watchlist_ioc)
            else:
                pass

        # Look through executableset to extract all md5s, but exclude any specifically listed in config.ini.
        excluded_md5 = []
        if self.config.getboolean(self.product, 'excluded_md5_use'):
            excluded_md5 = json.loads(self.config.get(self.product, 'excluded_md5'))

        for item in mrti.executable_set:

            # Prevent duplicate md5s.
            if item.subtype == 'Otherwise benign software application repurposed for use by malware':
                if item.md5 not in md5_none and item.md5 not in excluded_md5:
                    md5_none.append(item.md5)
            else:
                if item.md5 not in md5_major and item.md5 not in excluded_md5:
                    md5_major.append(item.md5)

        # Initialize booleans to track whether individual reports should be sent to Carbon Black, based on whether
        report_major_contains_data = False
        report_moderate_contains_data = False
        report_minor_contains_data = False
        report_none_contains_data = False

        # Report Major
        report_major.update(id=str(mrti.threat_id) + '_Major')
        report_major.update(title='ThreatID:' + str(mrti.threat_id) + ' ImpactRating:Major' + ' MalwareFamily:' + mrti.malware_family)
        report_major.update(score=self.config.getint(self.product, 'impact_major'))
        report_major['iocs'] = {}
        if ipv4_major:
            report_major['iocs']['ipv4'] = ipv4_major
            report_major_contains_data = True
        if dns_major:
            report_major['iocs']['dns'] = dns_major
            report_major_contains_data = True
        if md5_major:
            report_major['iocs']['md5'] = md5_major
            report_major_contains_data = True

        # Report Moderate
        report_moderate.update(id=str(mrti.threat_id) + '_Moderate')
        report_moderate.update(title='ThreatID:' + str(mrti.threat_id) + ' ImpactRating:Moderate' + ' MalwareFamily:' + mrti.malware_family)
        report_moderate.update(score=self.config.getint(self.product, 'impact_moderate'))
        report_moderate['iocs'] = {}
        if ipv4_moderate:
            report_moderate['iocs']['ipv4'] = ipv4_moderate
            report_moderate_contains_data = True
        if dns_moderate:
            report_moderate['iocs']['dns'] = dns_moderate
            report_moderate_contains_data = True

        # Report Minor
        report_minor.update(id=str(mrti.threat_id) + '_Minor')
        report_minor.update(title='ThreatID:' + str(mrti.threat_id) + ' ImpactRating:Minor' + ' MalwareFamily:' + mrti.malware_family)
        report_minor.update(score=self.config.getint(self.product, 'impact_minor'))
        report_minor['iocs'] = {}
        if ipv4_minor:
            report_minor['iocs']['ipv4'] = ipv4_minor
            report_minor_contains_data = True
        if dns_minor:
            report_minor['iocs']['dns'] = dns_minor
            report_minor_contains_data = True

        # Report None
        report_none.update(id=str(mrti.threat_id) + '_None')
        report_none.update(title='ThreatID:' + str(mrti.threat_id) + ' ImpactRating:None' + ' MalwareFamily:' + mrti.malware_family)
        report_none.update(score=self.config.getint(self.product, 'impact_none'))
        report_none['iocs'] = {}
        if ipv4_none:
            report_none['iocs']['ipv4'] = ipv4_none
            report_none_contains_data = True
        if dns_none:
            report_none['iocs']['dns'] = dns_none
            report_none_contains_data = True
        if md5_none:
            report_none['iocs']['md5'] = md5_none
            report_none_contains_data = True

        # Only include an individual report if it contains IOCs
        if report_major_contains_data:
            self.reports.append(report_major)
        if report_moderate_contains_data:
            self.reports.append(report_moderate)
        if report_minor_contains_data:
            self.reports.append(report_minor)
        if report_none_contains_data:
            self.reports.append(report_none)

    def _feed_extract_id(self, config_file_location):
        """

        :param config:
        :param config_file_location:
        :return:
        """

        # Build URI to get Feed ID from Carbon Black.
        url = self.config.get(self.product, 'host_with_protocol') + '/api/v1/feed'

        # Make API call to Carbon Black.
        # response = self._connect_to_carbon_black(config=config, url=url, verb='GET')
        response = self.rest_api.connect_to_api(verb='GET', url=url, headers=self.headers)

        # Loop through feeds in Carbon Black.
        for feed in json.loads(response):

            if feed.get('name') == self.config.get(self.product, 'feed_name'):

                # Set the Feed ID in the config file.
                feed_id = str(feed.get('id'))
                self.config.set(self.product, 'feed_id', feed_id)
                self.logger.info(self.config.get(self.product, 'feed_name') + ' was found in Carbon Black with Feed ID: ' + feed_id)

                # Write the new config file to disk.
                with open(config_file_location, 'w') as configfile:
                    self.config.write(configfile)

    def _feed_synchronize(self):
        """
        Initiates a synchronization by Carbon Black of a specific feed.

        :return:
        """

        # Build the URL for synchronization.
        url = self.config.get(self.product, 'host_with_protocol') + \
              '/api/v1/feed/' + \
              str(self.config.get(self.product, 'feed_id')) + \
              '/synchronize'

        # Use this data to request a _full_ sync.
        data = json.dumps({'full_sync': True})

        # response = self._connect_to_carbon_black(config=config, url=url, verb='POST', data=data)
        response = self.rest_api.connect_to_api(verb='POST', url=url, data=data, headers=self.headers)

        self.logger.info('Synchronization response from Carbon Black: ' + str(response))
