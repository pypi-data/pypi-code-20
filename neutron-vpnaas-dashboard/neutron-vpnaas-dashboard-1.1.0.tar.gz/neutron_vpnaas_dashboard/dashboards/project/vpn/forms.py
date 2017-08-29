# Copyright 2013, Mirantis Inc
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import logging

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import forms
from horizon import messages

from neutron_vpnaas_dashboard.api import vpn as api_vpn


LOG = logging.getLogger(__name__)


class UpdateVPNService(forms.SelfHandlingForm):
    name = forms.CharField(max_length=80, label=_("Name"), required=False)
    vpnservice_id = forms.CharField(
        label=_("ID"),
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    description = forms.CharField(
        required=False, max_length=80, label=_("Description"))
    admin_state_up = forms.BooleanField(label=_("Enable Admin State"),
                                        required=False)

    failure_url = 'horizon:project:vpn:index'

    def handle(self, request, context):
        try:
            data = {'vpnservice': {'name': context['name'],
                                   'description': context['description'],
                                   'admin_state_up': context['admin_state_up'],
                                   }}
            vpnservice = api_vpn.vpnservice_update(
                request, context['vpnservice_id'], **data)
            msg = (_('VPN Service %s was successfully updated.')
                   % context['name'])
            messages.success(request, msg)
            return vpnservice
        except Exception as e:
            LOG.info('Failed to update VPN Service %(id)s: %(exc)s',
                     {'id': context['vpnservice_id'], 'exc': e})
            msg = _('Failed to update VPN Service %s') % context['name']
            redirect = reverse(self.failure_url)
            exceptions.handle(request, msg, redirect=redirect)


class UpdateEndpointGroup(forms.SelfHandlingForm):
    name = forms.CharField(
        max_length=80,
        label=_("Name"),
        required=False)
    endpoint_group_id = forms.CharField(
        label=_("ID"),
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    description = forms.CharField(
        required=False,
        max_length=80,
        label=_("Description"))

    failure_url = 'horizon:project:vpn:index'

    def handle(self, request, context):
        try:
            data = {'endpoint_group':
                    {'name': context['name'],
                     'description': context['description']}
                    }
            endpointgroup = api_vpn.endpointgroup_update(
                request, context['endpoint_group_id'], **data)
            msg = (_('Endpoint Group %s was successfully updated.')
                   % context['name'])
            messages.success(request, msg)
            return endpointgroup
        except Exception as e:
            LOG.info('Failed to update Endpint Group %(id)s: %(exc)s',
                     {'id': context['endpoint_group_id'], 'exc': e})
            msg = _('Failed to update Endpint Group %s') % context['name']
            redirect = reverse(self.failure_url)
            exceptions.handle(request, msg, redirect=redirect)


class UpdateIKEPolicy(forms.SelfHandlingForm):
    name = forms.CharField(max_length=80, label=_("Name"), required=False)
    ikepolicy_id = forms.CharField(
        label=_("ID"),
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    description = forms.CharField(
        required=False, max_length=80, label=_("Description"))
    # Currently this field has only one choice, so mark it as readonly.
    auth_algorithm = forms.ChoiceField(
        label=_("Authorization algorithm"),
        choices=[('sha1', _('sha1'))],
        widget=forms.ThemableSelectWidget(attrs={'readonly': 'readonly'}),
        required=False)
    encryption_algorithm = forms.ChoiceField(
        label=_("Encryption algorithm"),
        choices=[('3des', _('3des')),
                 ('aes-128', _('aes-128')),
                 ('aes-192', _('aes-192')),
                 ('aes-256', _('aes-256'))],
        required=False)
    ike_version = forms.ChoiceField(
        label=_("IKE version"),
        choices=[('v1', _('v1')),
                 ('v2', _('v2'))],
        required=False)
    # Currently this field has only one choice, so mark it as readonly.
    lifetime_units = forms.ChoiceField(
        label=_("Lifetime units for IKE keys"),
        choices=[('seconds', _('seconds'))],
        widget=forms.ThemableSelectWidget(attrs={'readonly': 'readonly'}),
        required=False)
    lifetime_value = forms.IntegerField(
        min_value=60,
        label=_("Lifetime value for IKE keys"),
        help_text=_("Equal to or greater than 60"),
        required=False)
    pfs = forms.ChoiceField(
        label=_("Perfect Forward Secrecy"),
        choices=[('group2', _('group2')),
                 ('group5', _('group5')),
                 ('group14', _('group14'))],
        required=False)
    # Currently this field has only one choice, so mark it as readonly.
    phase1_negotiation_mode = forms.ChoiceField(
        label=_("IKE Phase1 negotiation mode"),
        choices=[('main', 'main')],
        widget=forms.ThemableSelectWidget(attrs={'readonly': 'readonly'}),
        required=False)

    failure_url = 'horizon:project:vpn:index'

    def handle(self, request, context):
        try:
            data = {'ikepolicy':
                    {'name': context['name'],
                     'description': context['description'],
                     'auth_algorithm': context['auth_algorithm'],
                     'encryption_algorithm': context['encryption_algorithm'],
                     'ike_version': context['ike_version'],
                     'lifetime': {'units': context['lifetime_units'],
                                  'value': context['lifetime_value']},
                     'pfs': context['pfs'],
                     'phase1_negotiation_mode':
                     context['phase1_negotiation_mode'],
                     }}
            ikepolicy = api_vpn.ikepolicy_update(
                request, context['ikepolicy_id'], **data)
            msg = (_('IKE Policy %s was successfully updated.')
                   % context['name'])
            messages.success(request, msg)
            return ikepolicy
        except Exception as e:
            LOG.info('Failed to update IKE Policy %(id)s: %(exc)s',
                     {'id': context['ikepolicy_id'], 'exc': e})
            msg = _('Failed to update IKE Policy %s') % context['name']
            redirect = reverse(self.failure_url)
            exceptions.handle(request, msg, redirect=redirect)


class UpdateIPSecPolicy(forms.SelfHandlingForm):
    name = forms.CharField(max_length=80, label=_("Name"), required=False)
    ipsecpolicy_id = forms.CharField(
        label=_("ID"),
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    description = forms.CharField(
        required=False, max_length=80, label=_("Description"))
    # Currently this field has only one choice, so mark it as readonly.
    auth_algorithm = forms.ChoiceField(
        label=_("Authorization algorithm"),
        choices=[('sha1', _('sha1'))],
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False)
    encapsulation_mode = forms.ChoiceField(
        label=_("Encapsulation mode"),
        choices=[('tunnel', _('tunnel')),
                 ('transport', _('transport'))],
        required=False)
    encryption_algorithm = forms.ChoiceField(
        label=_("Encryption algorithm"),
        choices=[('3des', _('3des')),
                 ('aes-128', _('aes-128')),
                 ('aes-192', _('aes-192')),
                 ('aes-256', _('aes-256'))],
        required=False)
    # Currently this field has only one choice, so mark it as readonly.
    lifetime_units = forms.ChoiceField(
        label=_("Lifetime units"),
        choices=[('seconds', _('seconds'))],
        widget=forms.ThemableSelectWidget(attrs={'readonly': 'readonly'}),
        required=False)
    lifetime_value = forms.IntegerField(
        min_value=60,
        label=_("Lifetime value"),
        help_text=_("Equal to or greater than 60"),
        required=False)
    pfs = forms.ChoiceField(
        label=_("Perfect Forward Secrecy"),
        choices=[('group2', _('group2')),
                 ('group5', _('group5')),
                 ('group14', _('group14'))],
        required=False)
    transform_protocol = forms.ChoiceField(
        label=_("Transform Protocol"),
        choices=[('esp', _('esp')),
                 ('ah', _('ah')),
                 ('ah-esp', _('ah-esp'))],
        required=False)

    failure_url = 'horizon:project:vpn:index'

    def handle(self, request, context):
        try:
            data = {'ipsecpolicy':
                    {'name': context['name'],
                     'description': context['description'],
                     'auth_algorithm': context['auth_algorithm'],
                     'encapsulation_mode': context['encapsulation_mode'],
                     'encryption_algorithm': context['encryption_algorithm'],
                     'lifetime': {'units': context['lifetime_units'],
                                  'value': context['lifetime_value']},
                     'pfs': context['pfs'],
                     'transform_protocol': context['transform_protocol'],
                     }}
            ipsecpolicy = api_vpn.ipsecpolicy_update(
                request, context['ipsecpolicy_id'], **data)
            msg = (_('IPSec Policy %s was successfully updated.')
                   % context['name'])
            messages.success(request, msg)
            return ipsecpolicy
        except Exception as e:
            LOG.info('Failed to update IPSec Policy %(id)s: %(exc)s',
                     {'id': context['ipsecpolicy_id'], 'exc': e})
            msg = _('Failed to update IPSec Policy %s') % context['name']
            redirect = reverse(self.failure_url)
            exceptions.handle(request, msg, redirect=redirect)


class UpdateIPSecSiteConnection(forms.SelfHandlingForm):
    name = forms.CharField(max_length=80, label=_("Name"), required=False)
    ipsecsiteconnection_id = forms.CharField(
        label=_("ID"),
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    description = forms.CharField(
        required=False, max_length=80, label=_("Description"))
    peer_address = forms.IPField(
        label=_("Peer gateway public IPv4/IPv6 Address or FQDN"),
        help_text=_("Peer gateway public IPv4/IPv6 address or FQDN for "
                    "the VPN Connection"),
        version=forms.IPv4 | forms.IPv6,
        mask=False)
    peer_id = forms.IPField(
        label=_("Peer router identity for authentication (Peer ID)"),
        help_text=_("Peer router identity for authentication. "
                    "Can be IPv4/IPv6 address, e-mail, key ID, or FQDN"),
        version=forms.IPv4 | forms.IPv6,
        mask=False)
    peer_cidrs = forms.MultiIPField(
        required=False,
        label=_("Remote peer subnet(s)"),
        help_text=_("Remote peer subnet(s) address(es) "
                    "with mask(s) in CIDR format "
                    "separated with commas if needed "
                    "(e.g. 20.1.0.0/24, 21.1.0.0/24)"),
        version=forms.IPv4 | forms.IPv6,
        mask=True)
    local_ep_group_id = forms.CharField(
        required=False,
        label=_("Local Endpoint Group(s)"),
        help_text=_("IPsec connection validation requires "
                    "that local endpoints are subnets"))
    peer_ep_group_id = forms.CharField(
        required=False,
        label=_("Peer Endpoint Group(s)"),
        help_text=_("IPSec connection validation requires "
                    "that peer endpoints are CIDRs"))
    psk = forms.CharField(
        widget=forms.PasswordInput(render_value=True),
        max_length=80, label=_("Pre-Shared Key (PSK) string"))
    mtu = forms.IntegerField(
        min_value=68,
        required=False,
        label=_("Maximum Transmission Unit size for the connection"),
        help_text=_("Equal to or greater than 68 if the local subnet is IPv4. "
                    "Equal to or greater than 1280 if the local subnet "
                    "is IPv6."))
    dpd_action = forms.ChoiceField(
        label=_("Dead peer detection actions"),
        required=False,
        choices=[('hold', _('hold')),
                 ('clear', _('clear')),
                 ('disabled', _('disabled')),
                 ('restart', _('restart')),
                 ('restart-by-peer', _('restart-by-peer'))])
    dpd_interval = forms.IntegerField(
        min_value=1,
        required=False,
        label=_("Dead peer detection interval"),
        help_text=_("Valid integer lesser than the DPD timeout"))
    dpd_timeout = forms.IntegerField(
        min_value=1,
        required=False,
        label=_("Dead peer detection timeout"),
        help_text=_("Valid integer greater than the DPD interval"))
    initiator = forms.ChoiceField(
        label=_("Initiator state"),
        required=False,
        choices=[('bi-directional', _('bi-directional')),
                 ('response-only', _('response-only'))])
    admin_state_up = forms.BooleanField(label=_("Enable Admin State"),
                                        required=False)

    failure_url = 'horizon:project:vpn:index'

    def clean(self):
        cleaned_data = super(UpdateIPSecSiteConnection, self).clean()
        interval = cleaned_data.get('dpd_interval')
        timeout = cleaned_data.get('dpd_timeout')

        if not interval < timeout:
            msg = _("DPD Timeout must be greater than DPD Interval")
            self._errors['dpd_timeout'] = self.error_class([msg])
        return cleaned_data

    def handle(self, request, context):
        try:
            data = {
                'name': context['name'],
                'description': context['description'],
                'peer_address': context['peer_address'],
                'peer_id': context['peer_id'],
                'psk': context['psk'],
                'mtu': context['mtu'],
                'dpd': {'action': context['dpd_action'],
                        'interval': context['dpd_interval'],
                        'timeout': context['dpd_timeout']},
                'initiator': context['initiator'],
                'admin_state_up': context['admin_state_up']
            }
            if not context['peer_cidrs']:
                data['local_ep_group_id'] = context['local_ep_group_id']
                data['peer_ep_group_id'] = context['peer_ep_group_id']
            else:
                cidrs = context['peer_cidrs']
                data['peer_cidrs'] = [cidr.strip() for cidr in cidrs.split(',')
                                      if cidr.strip()]
            ipsecsiteconnection = api_vpn.ipsecsiteconnection_update(
                request, context['ipsecsiteconnection_id'],
                ipsec_site_connection=data)
            msg = (_('IPSec Site Connection %s was successfully updated.')
                   % context['name'])
            messages.success(request, msg)
            return ipsecsiteconnection
        except Exception as e:
            LOG.info('Failed to update IPSec Site Connection %(id)s: %(exc)s',
                     {'id': context['ipsecsiteconnection_id'], 'exc': e})
            msg = (_('Failed to update IPSec Site Connection %s')
                   % context['name'])
            redirect = reverse(self.failure_url)
            exceptions.handle(request, msg, redirect=redirect)
