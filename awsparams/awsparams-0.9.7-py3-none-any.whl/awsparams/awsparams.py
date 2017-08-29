#!/usr/bin/env python3.6
# Copyright 2016 Brigham Young University
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import boto3
from getpass import getpass
__VERSION__ = '0.9.7'


def connect_ssm(profile=''):
    if profile:
        session = boto3.Session(profile_name=profile)
        ssm = session.client('ssm')
    else:
        ssm = boto3.client('ssm')
    return ssm


def put_parameter(profile, overwrite, parameter):
    ssm = connect_ssm(profile)
    if overwrite:
        parameter['Overwrite'] = True
    ssm.put_parameter(**parameter)


def remove_parameter(profile, param):
    ssm = connect_ssm(profile)
    ssm.delete_parameter(Name=param)


# TODO refactor to regular get_parameter + clarity ie line 52 is hard to read
def get_parameter(name, profile=None, cache=None, decryption=False):
    ssm = connect_ssm(profile)
    param = next(parm for parm in ssm.get_parameters(
        Names=[name], WithDecryption=decryption)['Parameters'])
    if param.get('Description'):
        param['Description'] = next((parm['Description'] for parm in cache if parm['Name'] == name)) if cache else next(
            (parm['Description'] for parm in get_all_parameters(profile) if parm['Name'] == name))
    return param


def get_all_parameters(profile, pattern=None, simplify=False):
    ssm = connect_ssm(profile)
    parameter_page = ssm.describe_parameters()
    parameters = parameter_page['Parameters']
    while parameter_page.get('NextToken'):
        parameter_page = ssm.describe_parameters(
            NextToken=parameter_page['NextToken'])
        parameters.extend(parameter_page['Parameters'])
    if pattern and simplify:
        return [param for param in translate_results(parameters) if pattern in param]
    elif pattern:
        return [param for param in parameters if pattern in param['Name']]
    elif simplify:
        return translate_results(parameters)
    else:
        return parameters


def translate_results(parameters):
    return [parm['Name'] for parm in parameters]


def ls_param(src='', profile=None, values=False, with_decryption=False):
    """
    List Paramters, optional matching a specific prefix/pattern
    """
    if with_decryption and not values:
        values = True
    for parm in get_all_parameters(profile, src, simplify=True):
        if values:
            try:
                ls_values = get_parameter(
                    parm, profile=profile, decryption=with_decryption)
                print("{}: {}".format(ls_values['Name'], ls_values['Value']))
            except Exception as err:
                print("Unknown error occured: {}".format(err))
        else:
            print(parm)


def cp_param(src, dst, src_profile='', dst_profile='', prefix=False, overwrite=False):
    """
    Copy a parameter, optionally across accounts
    """
    # cross account copy without needing dst
    if src_profile and dst_profile and src_profile != dst_profile and not dst:
        dst = src
    elif not dst:
        print("dst (Destination) is required when not copying to another profile")
        return
    if prefix:
        params = get_all_parameters(src_profile, src)
        for i in params:
            put = get_parameter(
                name=i['Name'], profile=src_profile, cache=params, decryption=True)
            put['Name'] = put['Name'].replace(src, dst)
            put_parameter(dst_profile, overwrite, put)
            print("Copied {} to {}".format(
                i['Name'], put['Name']))
    else:
        if isinstance(src, str):
            src_param = [src]
        for i in src_param:
            put = get_parameter(name=i, profile=src_profile, decryption=True)
            put['Name'] = dst
            put_parameter(dst_profile, overwrite, put)
            print("Copied {} to {}".format(src, dst))


def mv_param(src, dst, prefix=False, profile=None):
    """
    Move or rename a parameter
    """
    if prefix:
        cp_param(src, dst, src_profile=profile, dst_profile=profile, prefix=prefix)
        rm_param(src, force=True, prefix=True, profile=profile)
    else:
        cp_param(src, dst, src_profile=profile, dst_profile=profile)
        rm_param(src, force=True, profile=profile)


def sanity_check(param, force):
    if force:
        return True
    sanity_check = input("Remove {} y/n ".format(param))
    return sanity_check == 'y'

def rm_param(src, force=False, prefix=False, profile=None):
    """
    Remove/Delete a parameter
    """
    if prefix:
        params = get_all_parameters(profile, src, True)
        if len(params) == 0:
            print("No parameters with the {} prefix found".format(src))
        else:
            for param in params:
                if sanity_check(param, force):
                    remove_parameter(profile, param)
                    print("The {} parameter has been removed".format(param))
    else:
        param = get_parameter(name=src, profile=profile)
        if 'Name' in param:
            if sanity_check(src, force):
                remove_parameter(profile, src)
                print("The {} parameter has been removed".format(src))
        else:
            print("Parameter {} not found".format(src))


def new_param(name, value, param_type='String', description='', profile=None, overwrite=False):
    """
    Create a new parameter
    """
    if not value:
        if param_type == 'SecureString':
            value = getpass(prompt="SecureString: ")
        elif param_type == 'StringList':
            value = input("Input Values seperated by ',': ")
        elif param_type == 'String':
            value = input('Parameter Value: ')

    param = {
        'Name': name,
        'Value': value,
        'Type': param_type,
        'Overwrite': overwrite
    }
    if description:
        param['Description'] = description
    put_parameter(profile, overwrite, param)


def set_param(src, value, profile=None):
    """
    Edit an existing parameter
    """
    put = get_parameter(name=src, profile=profile, decryption=True)
    put['Value'] = value
    put_parameter(profile, True, put)
    print("set '{}' to '{}'".format(src, value))
