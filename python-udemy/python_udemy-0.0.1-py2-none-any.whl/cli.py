# Copyright Peng Xiao
# All rights reserved.
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

from __future__ import print_function

from udemy import Udemy


def main():
    """main
    """
    my_udemy = Udemy(url='xxxx', token='xxxx')
    print(type(my_udemy))
    return my_udemy


if __name__ == '__main__':
    print(main())
