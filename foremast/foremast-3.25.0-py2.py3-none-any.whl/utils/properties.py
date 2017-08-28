#   Foremast - Pipeline Tooling
#
#   Copyright 2016 Gogo, LLC
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
"""Get Application properties that have been generated by `create-configs`."""
import json
import logging

LOG = logging.getLogger(__name__)


def get_properties(properties_file='raw.properties.json', env=None):
    """Get contents of _properties_file_ for the _env_.

    Args:
        properties_file (str): File name of `create-configs` JSON output.
        env (str): Environment to read optionally

    Returns:
        dict: JSON loaded Application properties for _env_.
        None: Given _env_ was not found in `create-configs` JSON output.

    """
    with open(properties_file, 'rt') as file_handle:
        properties = json.load(file_handle)

    env_properties = properties.get(env, properties)
    LOG.debug('Found properties for %s:\n%s', env, env_properties)
    return env_properties
