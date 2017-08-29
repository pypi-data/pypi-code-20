import unittest

from netjsonconfig import OpenWrt
from netjsonconfig.exceptions import ValidationError
from netjsonconfig.utils import _TabsMixin


class TestWireless(unittest.TestCase, _TabsMixin):
    maxDiff = None

    _wifi_netjson = {
        "interfaces": [
            {
                "name": "wlan0",
                "type": "wireless",
                "addresses": [
                    {
                        "address": "192.168.1.1",
                        "mask": 24,
                        "proto": "static",
                        "family": "ipv4"
                    }
                ],
                "wireless": {
                    "radio": "radio0",
                    "mode": "access_point",
                    "ssid": "MyWifiAP",
                    "hidden": True,
                    "ack_distance": 300,
                    "rts_threshold": 1300,
                    "frag_threshold": 1500
                }
            }
        ]
    }
    _wifi_uci = """package network

config interface 'wlan0'
    option ifname 'wlan0'
    option ipaddr '192.168.1.1'
    option netmask '255.255.255.0'
    option proto 'static'

package wireless

config wifi-iface 'wifi_wlan0'
    option device 'radio0'
    option distance '300'
    option frag '1500'
    option hidden '1'
    option ifname 'wlan0'
    option mode 'ap'
    option network 'wlan0'
    option rts '1300'
    option ssid 'MyWifiAP'
"""

    def test_render_wifi_interface(self):
        o = OpenWrt(self._wifi_netjson)
        expected = self._tabs(self._wifi_uci)
        self.assertEqual(o.render(), expected)

    def test_parse_wifi_interface(self):
        o = OpenWrt(native=self._wifi_uci)
        self.assertEqual(o.config, self._wifi_netjson)

    def test_parse_wifi_interface_partial(self):
        o = OpenWrt(native="""package wireless

config wifi-iface 'wifi_wlan0'
    option device 'radio0'
    option ifname 'wlan0'
    option mode 'ap'
    option network 'wlan0'
    option ssid 'MyWifiAP'
""")
        expected = {
            "interfaces": [
                {
                    "name": "wlan0",
                    "type": "wireless",
                    "wireless": {
                        "radio": "radio0",
                        "mode": "access_point",
                        "ssid": "MyWifiAP"
                    }
                }
            ]
        }
        self.assertEqual(o.config, expected)

    _multiple_wifi_netjson = {
        "interfaces": [
            {
                "name": "wlan0",
                "type": "wireless",
                "addresses": [
                    {
                        "proto": "dhcp",
                        "family": "ipv4"
                    }
                ],
                "wireless": {
                    "radio": "radio0",
                    "mode": "access_point",
                    "ssid": "ap-ssid"
                }
            },
            {
                "name": "wlan1",
                "type": "wireless",
                "addresses": [
                    {
                        "proto": "dhcp",
                        "family": "ipv4"
                    }
                ],
                "wireless": {
                    "radio": "radio1",
                    "mode": "adhoc",
                    "ssid": "adhoc-ssid",
                    "bssid": "00:11:22:33:44:55"
                }
            }
        ]
    }
    _multiple_wifi_uci = """package network

config interface 'wlan0'
    option ifname 'wlan0'
    option proto 'dhcp'

config interface 'wlan1'
    option ifname 'wlan1'
    option proto 'dhcp'

package wireless

config wifi-iface 'wifi_wlan0'
    option device 'radio0'
    option ifname 'wlan0'
    option mode 'ap'
    option network 'wlan0'
    option ssid 'ap-ssid'

config wifi-iface 'wifi_wlan1'
    option bssid '00:11:22:33:44:55'
    option device 'radio1'
    option ifname 'wlan1'
    option mode 'adhoc'
    option network 'wlan1'
    option ssid 'adhoc-ssid'
"""

    def test_render_multiple_wifi(self):
        o = OpenWrt(self._multiple_wifi_netjson)
        expected = self._tabs(self._multiple_wifi_uci)
        self.assertEqual(o.render(), expected)

    def test_parse_multiple_wifi(self):
        o = OpenWrt(native=self._multiple_wifi_uci)
        self.assertEqual(o.config, self._multiple_wifi_netjson)

    _wifi_bridge_netjson = {
        "interfaces": [
            {
                "name": "eth0.1",
                "type": "ethernet"
            },
            {
                "name": "wlan0",
                "type": "wireless",
                "wireless": {
                    "radio": "radio0",
                    "mode": "access_point",
                    "ssid": "open"
                }
            },
            {
                "name": "br-lan",
                "type": "bridge",
                "bridge_members": [
                    "eth0.1",
                    "wlan0"
                ],
                "addresses": [
                    {
                        "address": "192.168.1.1",
                        "mask": 24,
                        "proto": "static",
                        "family": "ipv4"
                    }
                ]
            }
        ]
    }
    _wifi_bridge_uci = """package network

config interface 'eth0_1'
    option ifname 'eth0.1'
    option proto 'none'

config interface 'wlan0'
    option ifname 'wlan0'
    option proto 'none'

config interface 'br_lan'
    option ifname 'eth0.1 wlan0'
    option ipaddr '192.168.1.1'
    option netmask '255.255.255.0'
    option proto 'static'
    option type 'bridge'

package wireless

config wifi-iface 'wifi_wlan0'
    option device 'radio0'
    option ifname 'wlan0'
    option mode 'ap'
    option network 'wlan0'
    option ssid 'open'
"""

    def test_render_wifi_bridge(self):
        o = OpenWrt(self._wifi_bridge_netjson)
        expected = self._tabs(self._wifi_bridge_uci)
        self.assertEqual(o.render(), expected)

    def test_parse_wifi_bridge(self):
        o = OpenWrt(native=self._wifi_bridge_uci)
        self.assertEqual(o.config, self._wifi_bridge_netjson)

    _wifi_networks_netjson = {
        "interfaces": [
            {
                "name": "eth0",
                "type": "ethernet"
            },
            {
                "name": "wlan0",
                "type": "wireless",
                "addresses": [
                    {
                        "proto": "dhcp",
                        "family": "ipv4"
                    }
                ],
                "wireless": {
                    "radio": "radio0",
                    "mode": "access_point",
                    "ssid": "open",
                    "network": ["wlan0", "eth0"]
                }
            }
        ]
    }
    _wifi_networks_uci = """package network

config interface 'eth0'
    option ifname 'eth0'
    option proto 'none'

config interface 'wlan0'
    option ifname 'wlan0'
    option proto 'dhcp'

package wireless

config wifi-iface 'wifi_wlan0'
    option device 'radio0'
    option ifname 'wlan0'
    option mode 'ap'
    option network 'wlan0 eth0'
    option ssid 'open'
"""

    def test_render_wifi_networks(self):
        o = OpenWrt(self._wifi_networks_netjson)
        expected = self._tabs(self._wifi_networks_uci)
        self.assertEqual(o.render(), expected)

    def test_parse_wifi_network(self):
        o = OpenWrt(native=self._wifi_networks_uci)
        self.assertEqual(o.config, self._wifi_networks_netjson)

    def test_render_wireless_empty_network_attr(self):
        o = OpenWrt({
            "interfaces": [
                {
                    "name": "wlan0",
                    "type": "wireless",
                    "wireless": {
                        "radio": "radio0",
                        "mode": "access_point",
                        "ssid": "open",
                        "network": []
                    }
                }
            ]
        })
        expected = self._tabs("""package network

config interface 'wlan0'
    option ifname 'wlan0'
    option proto 'none'

package wireless

config wifi-iface 'wifi_wlan0'
    option device 'radio0'
    option ifname 'wlan0'
    option mode 'ap'
    option network 'wlan0'
    option ssid 'open'
""")
        self.assertEqual(o.render(), expected)

    def test_wireless_network_attr_validation(self):
        o = OpenWrt({
            "interfaces": [
                {
                    "name": "wlan0",
                    "type": "wireless",
                    "wireless": {
                        "radio": "radio0",
                        "mode": "access_point",
                        "ssid": "open",
                        "network": "lan 0"
                    }
                }
            ]
        })
        # pattern does not validate
        with self.assertRaises(ValidationError):
            o.validate()
        # maxLength does not validate
        o.config['interfaces'][0]['wireless']['network'] = ['lan0123456789012345']
        with self.assertRaises(ValidationError):
            o.validate()
        # ensure fix works
        o.config['interfaces'][0]['wireless']['network'] = ['lan']
        o.validate()

    _interface_network_netjson = {
        "interfaces": [
            {
                "name": "wlan0",
                "type": "wireless",
                "network": "guests",
                "wireless": {
                    "radio": "radio0",
                    "mode": "access_point",
                    "ssid": "open"
                }
            }
        ]
    }
    _interface_network_uci = """package network

config interface 'guests'
    option ifname 'wlan0'
    option proto 'none'

package wireless

config wifi-iface 'wifi_wlan0'
    option device 'radio0'
    option ifname 'wlan0'
    option mode 'ap'
    option network 'guests'
    option ssid 'open'
"""

    def test_render_interface_network(self):
        o = OpenWrt(self._interface_network_netjson)
        expected = self._tabs(self._interface_network_uci)
        self.assertEqual(o.render(), expected)

    def test_parse_interface_network(self):
        o = OpenWrt(native=self._interface_network_uci)
        self.assertEqual(o.config, self._interface_network_netjson)

    def test_network_dot_conversion(self):
        o = OpenWrt({
            "interfaces": [
                {
                    "name": "wlan0",
                    "type": "wireless",
                    "wireless": {
                        "radio": "radio0",
                        "mode": "access_point",
                        "ssid": "open",
                        "network": ["eth0.1"],
                    }
                }
            ]
        })
        expected = self._tabs("""package network

config interface 'wlan0'
    option ifname 'wlan0'
    option proto 'none'

package wireless

config wifi-iface 'wifi_wlan0'
    option device 'radio0'
    option ifname 'wlan0'
    option mode 'ap'
    option network 'eth0_1'
    option ssid 'open'
""")
        self.assertEqual(o.render(), expected)

    def test_network_dash_conversion(self):
        o = OpenWrt({
            "interfaces": [
                {
                    "name": "wlan0",
                    "type": "wireless",
                    "wireless": {
                        "radio": "radio0",
                        "mode": "access_point",
                        "ssid": "open",
                        "network": ["eth0-1"],
                    }
                }
            ]
        })
        expected = self._tabs("""package network

config interface 'wlan0'
    option ifname 'wlan0'
    option proto 'none'

package wireless

config wifi-iface 'wifi_wlan0'
    option device 'radio0'
    option ifname 'wlan0'
    option mode 'ap'
    option network 'eth0_1'
    option ssid 'open'
""")
        self.assertEqual(o.render(), expected)

    _disabled_netjson = {
        "interfaces": [
            {
                "disabled": True,
                "name": "wlan0",
                "type": "wireless",
                "wireless": {
                    "radio": "radio0",
                    "mode": "station",
                    "ssid": "mywifi",
                    "bssid": "00:11:22:33:44:55"
                }
            }
        ]
    }
    _disabled_uci = """package network

config interface 'wlan0'
    option enabled '0'
    option ifname 'wlan0'
    option proto 'none'

package wireless

config wifi-iface 'wifi_wlan0'
    option bssid '00:11:22:33:44:55'
    option device 'radio0'
    option disabled '1'
    option ifname 'wlan0'
    option mode 'sta'
    option network 'wlan0'
    option ssid 'mywifi'
"""

    def test_render_interface_disabled(self):
        """
        see issue #35
        https://github.com/openwisp/netjsonconfig/issues/35
        """
        o = OpenWrt(self._disabled_netjson)
        expected = self._tabs(self._disabled_uci)
        self.assertEqual(o.render(), expected)

    def test_parse_interface_disabled_full(self):
        o = OpenWrt(native=self._disabled_uci)
        self.assertEqual(o.config, self._disabled_netjson)

    def test_parse_interface_disabled_partial(self):
        o = OpenWrt(native="""package wireless

config wifi-iface 'wifi_wlan0'
    option bssid '00:11:22:33:44:55'
    option device 'radio0'
    option disabled '1'
    option ifname 'wlan0'
    option mode 'sta'
    option network 'wlan0'
    option ssid 'mywifi'
""")
        self.assertEqual(o.config, self._disabled_netjson)

    _wds_netjson = {
        "interfaces": [
            {
                "name": "wlan0",
                "type": "wireless",
                "wireless": {
                    "radio": "radio0",
                    "mode": "access_point",
                    "wds": True,
                    "ssid": "MyWdsAp"
                }
            }
        ]
    }
    _wds_uci = """package network

config interface 'wlan0'
    option ifname 'wlan0'
    option proto 'none'

package wireless

config wifi-iface 'wifi_wlan0'
    option device 'radio0'
    option ifname 'wlan0'
    option mode 'ap'
    option network 'wlan0'
    option ssid 'MyWdsAp'
    option wds '1'
"""

    def test_render_wds_ap(self):
        o = OpenWrt(self._wds_netjson)
        expected = self._tabs(self._wds_uci)
        self.assertEqual(o.render(), expected)

    def test_parse_wds_ap(self):
        o = OpenWrt(native=self._wds_uci)
        self.assertEqual(o.config, self._wds_netjson)

    def test_wifi_options_zero(self):
        """
        ensure ack_distance, rts_threshold and frag_threshold
        are ignored if left empty
        """
        o = OpenWrt({
            "interfaces": [
                {
                    "name": "wlan0",
                    "type": "wireless",
                    "wireless": {
                        "radio": "radio0",
                        "mode": "access_point",
                        "ssid": "MyWifiAP",
                        "wmm": True,
                        "ack_distance": 0,
                        "rts_threshold": 0,
                        "frag_threshold": 0
                    }
                }
            ]
        })
        expected = self._tabs("""package network

config interface 'wlan0'
    option ifname 'wlan0'
    option proto 'none'

package wireless

config wifi-iface 'wifi_wlan0'
    option device 'radio0'
    option ifname 'wlan0'
    option mode 'ap'
    option network 'wlan0'
    option ssid 'MyWifiAP'
    option wmm '1'
""")
        self.assertEqual(o.render(), expected)

    _macfilter_netjson = {
        "interfaces": [
            {
                "name": "wlan0",
                "type": "wireless",
                "wireless": {
                    "radio": "radio0",
                    "mode": "access_point",
                    "ssid": "MyWifiAP",
                    "macfilter": "deny",
                    "maclist": [
                        "E8:94:F6:33:8C:1D",
                        "42:6c:8f:95:0f:00"
                    ]
                }
            }
        ]
    }
    _macfilter_uci = """package network

config interface 'wlan0'
    option ifname 'wlan0'
    option proto 'none'

package wireless

config wifi-iface 'wifi_wlan0'
    option device 'radio0'
    option ifname 'wlan0'
    option macfilter 'deny'
    list maclist 'E8:94:F6:33:8C:1D'
    list maclist '42:6c:8f:95:0f:00'
    option mode 'ap'
    option network 'wlan0'
    option ssid 'MyWifiAP'
"""

    def test_render_macfilter(self):
        o = OpenWrt(self._macfilter_netjson)
        expected = self._tabs(self._macfilter_uci)
        self.assertEqual(o.render(), expected)

    def test_parse_macfilter(self):
        o = OpenWrt(native=self._macfilter_uci)
        self.assertEqual(o.config, self._macfilter_netjson)

    def test_maclist_format(self):
        o = OpenWrt({
            "interfaces": [
                {
                    "name": "wlan0",
                    "type": "wireless",
                    "wireless": {
                        "radio": "radio0",
                        "mode": "access_point",
                        "ssid": "MyWifiAP",
                        "macfilter": "deny",
                        "maclist": [
                            "E8:94:F6:33:8C:1D",
                        ]
                    }
                }
            ]
        })
        o.validate()
        # too short
        o.config['interfaces'][0]['wireless']['maclist'][0] = '00:11:22:33:44'
        with self.assertRaises(ValidationError):
            o.validate()
        # valid
        o.config['interfaces'][0]['wireless']['maclist'][0] = '00-11-22-33-44-55'
        o.validate()
        # should not be valid
        o.config['interfaces'][0]['wireless']['maclist'][0] = '00:11:22:33:44:ZY'
        with self.assertRaises(ValidationError):
            o.validate()
        # empty is not valid
        o.config['interfaces'][0]['wireless']['maclist'][0] = ''
        with self.assertRaises(ValidationError):
            o.validate()

    _wds_bridge_netjson = {
        "interfaces": [
            # client
            {
                "name": "wlan0",
                "type": "wireless",
                "wireless": {
                    "mode": "station",
                    "radio": "radio0",
                    "network": ["wds_bridge"],
                    "ssid": "FreeRomaWifi",
                    "bssid": "C0:4A:00:2D:05:FD",
                    "wds": True
                }
            },
            # repeater access point
            {
                "name": "wlan1",
                "type": "wireless",
                "wireless": {
                    "mode": "access_point",
                    "radio": "radio1",
                    "network": ["wds_bridge"],
                    "ssid": "FreeRomaWifi"
                }
            },
            # WDS bridge
            {
                "name": "br-wds_bridge",
                "network": "wds_bridge",
                "type": "bridge",
                "addresses": [
                    {
                        "proto": "dhcp",
                        "family": "ipv4"
                    }
                ],
                "bridge_members": [
                    "wlan0",
                    "wlan1",
                ]
            }
        ]
    }
    _wds_bridge_uci = """package network

config interface 'wlan0'
    option ifname 'wlan0'
    option proto 'none'

config interface 'wlan1'
    option ifname 'wlan1'
    option proto 'none'

config interface 'wds_bridge'
    option ifname 'wlan0 wlan1'
    option proto 'dhcp'
    option type 'bridge'

package wireless

config wifi-iface 'wifi_wlan0'
    option bssid 'C0:4A:00:2D:05:FD'
    option device 'radio0'
    option ifname 'wlan0'
    option mode 'sta'
    option network 'wds_bridge'
    option ssid 'FreeRomaWifi'
    option wds '1'

config wifi-iface 'wifi_wlan1'
    option device 'radio1'
    option ifname 'wlan1'
    option mode 'ap'
    option network 'wds_bridge'
    option ssid 'FreeRomaWifi'
"""

    def test_render_wds_bridge(self):
        o = OpenWrt(self._wds_bridge_netjson)
        expected = self._tabs(self._wds_bridge_uci)
        self.assertEqual(o.render(), expected)

    def test_parse_wds_bridge(self):
        o = OpenWrt(native=self._wds_bridge_uci)
        self.assertEqual(o.config, self._wds_bridge_netjson)

    _80211s_netjson = {
        "interfaces": [
            {
                "name": "mesh0",
                "type": "wireless",
                "wireless": {
                    "radio": "radio0",
                    "mode": "802.11s",
                    "mesh_id": "ninux",
                    "network": ["lan"]
                }
            },
            {
                "name": "br-lan",
                "network": "lan",
                "type": "bridge",
                "bridge_members": ["mesh0"],
                "addresses": [
                    {
                        "address": "192.168.0.1",
                        "mask": 24,
                        "proto": "static",
                        "family": "ipv4"
                    }
                ]
            }
        ]
    }
    _80211s_uci = """package network

config interface 'mesh0'
    option ifname 'mesh0'
    option proto 'none'

config interface 'lan'
    option ifname 'mesh0'
    option ipaddr '192.168.0.1'
    option netmask '255.255.255.0'
    option proto 'static'
    option type 'bridge'

package wireless

config wifi-iface 'wifi_mesh0'
    option device 'radio0'
    option ifname 'mesh0'
    option mesh_id 'ninux'
    option mode 'mesh'
    option network 'lan'
"""

    def test_render_mesh_80211s(self):
        o = OpenWrt(self._80211s_netjson)
        expected = self._tabs(self._80211s_uci)
        self.assertEqual(o.render(), expected)

    def test_parse_mesh_80211s(self):
        o = OpenWrt(native=self._80211s_uci)
        self.assertEqual(o.config, self._80211s_netjson)

    _bssid_netjson = {
        "interfaces": [
            {
                "name": "wlan0",
                "type": "wireless",
                "wireless": {
                    "radio": "radio0",
                    "mode": "adhoc",
                    "ssid": "bssid-test",
                    "bssid": "00:11:22:33:44:55"
                }
            }
        ]
    }

    def test_bssid_format(self):
        o = OpenWrt(self._bssid_netjson)
        o.validate()
        # too short
        o.config['interfaces'][0]['wireless']['bssid'] = '00:11:22:33:44'
        with self.assertRaises(ValidationError):
            o.validate()
        # valid
        o.config['interfaces'][0]['wireless']['bssid'] = '00-11-22-33-44-55'
        o.validate()
        # should not be valid
        o.config['interfaces'][0]['wireless']['bssid'] = '00:11:22:33:44:ZY'
        with self.assertRaises(ValidationError):
            o.validate()

    def test_bssid_adhoc(self):
        o = OpenWrt(self._bssid_netjson)
        # bssid is required
        del o.config['interfaces'][0]['wireless']['bssid']
        with self.assertRaises(ValidationError):
            o.validate()
        # empty is not valid
        o.config['interfaces'][0]['wireless']['bssid'] = ''
        with self.assertRaises(ValidationError):
            o.validate()

    def test_bssid_station(self):
        o = OpenWrt(self._bssid_netjson)
        o.config['interfaces'][0]['wireless']['mode'] = 'station'
        o.validate()
        # bssid is not required
        del o.config['interfaces'][0]['wireless']['bssid']
        o.validate()
        # empty is valid
        o.config['interfaces'][0]['wireless']['bssid'] = ''
        o.validate()

    _list_option_netjson = {
        "interfaces": [
            {
                "name": "wlan0",
                "type": "wireless",
                "wireless": {
                    "radio": "radio0",
                    "mode": "access_point",
                    "ssid": "open",
                    "basic_rate": ["6000", "9000"]
                }
            }
        ]
    }
    _list_option_uci = """package network

config interface 'wlan0'
    option ifname 'wlan0'
    option proto 'none'

package wireless

config wifi-iface 'wifi_wlan0'
    list basic_rate '6000'
    list basic_rate '9000'
    option device 'radio0'
    option ifname 'wlan0'
    option mode 'ap'
    option network 'wlan0'
    option ssid 'open'
"""

    def test_render_list_option(self):
        o = OpenWrt(self._list_option_netjson)
        expected = self._tabs(self._list_option_uci)
        self.assertEqual(o.render(), expected)

    def test_parse_list_option(self):
        o = OpenWrt(native=self._list_option_uci)
        self.assertEqual(o.config, self._list_option_netjson)

    def test_isolate(self):
        o = OpenWrt({
            "interfaces": [
                {
                    "name": "wlan0",
                    "type": "wireless",
                    "wireless": {
                        "radio": "radio0",
                        "mode": "access_point",
                        "ssid": "open",
                        "isolate": True
                    }
                }
            ]
        })
        self.assertIn("option isolate '1'", o.render())
        # try entering an invalid value
        o.config['interfaces'][0]['wireless']['isolate'] = 'wrong'
        with self.assertRaises(ValidationError):
            o.validate()

    _macaddr_netjson = {
        "interfaces": [
            {
                "name": "wlan0",
                "type": "wireless",
                "mac": "E8:94:F6:33:8C:00",
                "wireless": {
                    "radio": "radio0",
                    "mode": "access_point",
                    "ssid": "open"
                }
            }
        ]
    }
    _macaddr_uci = """package network

config interface 'wlan0'
    option ifname 'wlan0'
    option proto 'none'

package wireless

config wifi-iface 'wifi_wlan0'
    option device 'radio0'
    option ifname 'wlan0'
    option macaddr 'E8:94:F6:33:8C:00'
    option mode 'ap'
    option network 'wlan0'
    option ssid 'open'
"""

    def test_render_macaddr_override(self):
        o = OpenWrt(self._macaddr_netjson)
        expected = self._tabs(self._macaddr_uci)
        self.assertEqual(o.render(), expected)

    def test_parse_macaddr_override(self):
        o = OpenWrt(native=self._macaddr_uci)
        self.assertEqual(o.config, self._macaddr_netjson)

    _custom_id_netjson = {
        "interfaces": [
            {
                "name": "wlan0",
                "type": "wireless",
                "wireless": {
                    "id": "arbitrary_id",
                    "radio": "radio0",
                    "mode": "access_point",
                    "ssid": "MyWifiAP"
                }
            }
        ]
    }
    _custom_id_uci = """package network

config interface 'wlan0'
    option ifname 'wlan0'
    option proto 'none'

package wireless

config wifi-iface 'arbitrary_id'
    option device 'radio0'
    option ifname 'wlan0'
    option mode 'ap'
    option network 'wlan0'
    option ssid 'MyWifiAP'
"""

    def test_render_wifi_custom_id(self):
        o = OpenWrt(self._custom_id_netjson)
        expected = self._tabs(self._custom_id_uci)
        self.assertEqual(o.render(), expected)

    def test_parse_wifi_custom_id(self):
        o = OpenWrt(native=self._custom_id_uci)
        self.assertEqual(o.config, self._custom_id_netjson)
