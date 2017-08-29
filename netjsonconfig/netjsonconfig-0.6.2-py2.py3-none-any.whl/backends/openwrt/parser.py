import re
import tarfile
from collections import OrderedDict

from ...utils import sorted_dict
from ..base.parser import BaseParser

packages_pattern = re.compile('^package\s', flags=re.MULTILINE)
block_pattern = re.compile('^config\s', flags=re.MULTILINE)
config_pattern = re.compile('^(option|list)\s*([^\s]*)\s*(.*)')
config_path = 'etc/config/'


class OpenWrtParser(BaseParser):
    def parse_text(self, config):
        return self._get_uci_packages(config)

    def parse_tar(self, tar):
        fileobj = tar.buffer if hasattr(tar, 'buffer') else tar
        tar = tarfile.open(fileobj=fileobj)
        text = ''
        for member in tar.getmembers():
            if not member.name.startswith(config_path):
                continue
            text += 'package {name}\n\n{contents}'.format(**{
                'name': member.name.replace(config_path, ''),
                'contents': tar.extractfile(member).read().decode()
            })
        return self._get_uci_packages(text)

    def _strip_quotes(self, value):
        return value.replace('\'', '')\
                    .replace('\"', '')

    def _get_uci_packages(self, text):
        results = re.split(packages_pattern, text)
        packages = OrderedDict()
        for result in results:
            result = result.strip()
            if not result:
                continue
            lines = result.split('\n')
            name = lines[0]
            contents = result[len(name):]
            packages[name] = self._get_uci_blocks(contents)
        return packages

    def _get_uci_blocks(self, text):
        results = re.split(block_pattern, text)
        blocks = []
        counter = 0
        for result in results:
            result = result.strip()
            if not result:
                continue
            counter += 1
            lines = result.split('\n')
            parts = lines[0].split()
            config_type = self._strip_quotes(parts[0])
            try:
                config_name = self._strip_quotes(parts[1])
            except IndexError:
                config_name = '{0}_{1}'.format(config_type, counter)
            block = OrderedDict()
            block['.type'] = config_type
            block['.name'] = config_name
            # loop over rest of lines
            for line in lines[1:]:
                match = re.search(config_pattern, line.strip())
                if not match:
                    continue
                parts = match.groups()
                key = self._strip_quotes(parts[1])
                value = self._strip_quotes(parts[2])
                # simple options
                if parts[0] == 'option':
                    block[key] = value
                # list options
                else:
                    block[key] = block.get(key, []) + [value]
            blocks.append(sorted_dict(block))
        return blocks
