# Copyright 2016 Dravetech AB. All rights reserved.
#
# The contents of this file are licensed under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with the
# License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

"""napalm_eos package."""
from napalm_eos.eos import EOSDriver
import pkg_resources

try:
    __version__ = pkg_resources.get_distribution('napalm-eos').version
except pkg_resources.DistributionNotFound:
    __version__ = "Not installed"

__all__ = ('EOSDriver',)
