import requests

IP_RANGE_URL = 'http://ip-ranges.amazonaws.com/ip-ranges.json'

ranges = requests.get(IP_RANGE_URL).json()

services = {}

for prefix in ranges['prefixes']:
    services.setdefault(
        prefix['service'],
        {},
    ).setdefault(
        prefix['region'],
        set(),
    ).add(
        prefix['ip_prefix'],
    )

for service, regions in services.items():
    print('{}:'.format(service))
    for region, prefixes in regions.items():
        print('\t{}:'.format(region))
        for prefix in sorted(prefixes):
            print('\t\t{}'.format(prefix))
