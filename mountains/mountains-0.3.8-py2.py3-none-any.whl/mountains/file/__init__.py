# -*- coding: utf-8 -*-
# Created by restran on 2017/8/23
from __future__ import unicode_literals, absolute_import
from collections import deque
from mountains.encoding import force_text, force_bytes


def read_dict(file_name, clear_none=False):
    """
    读取字典文件
    :param clear_none:
    :param file_name:
    :return:
    """
    with open(file_name, 'r') as f:
        data = []
        i = 0
        for line in f:
            i += 1
            try:
                line = force_text(line).strip('\n').strip()
                data.append(line)
            except:
                print('read error line %s' % i)
        if clear_none:
            data = [t for t in data if t != '']
        data = deque(data)
    return data


def write_bytes_file(file_name, data):
    with open(file_name, 'wb') as f:
        f.write(force_bytes(data))


def read_bytes_file(file_name):
    with open(file_name, 'rb') as f:
        return f.read()

