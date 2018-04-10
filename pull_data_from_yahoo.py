import requests
from world_indice import world_indices


def pull_data_from_yahoo():
    url = 'https://query1.finance.yahoo.com/v7/finance/spark'
    payload = {'range': '1d', 'interval': '1m',
               'indicators': 'close',
               'includeTimestamps': 'false',
               'includePrePost': 'false', 'corsDomain': 'uk.finance.yahoo.com &.tsrc = finance'}
    for key in world_indices:
        payload['symbols'] = world_indices[key]
        response = requests.get(url, params=payload, verify=False)
        break



pull_data_from_yahoo()