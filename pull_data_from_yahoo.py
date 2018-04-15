import requests
import json
from celery_settings import app
from world_indice import world_indices

@app.task
def pull_data_from_yahoo():
    url = 'https://query1.finance.yahoo.com/v7/finance/spark'
    payload = {'range': '1d', 'interval': '1m',
               'indicators': 'close',
               'includeTimestamps': 'false',
               'includePrePost': 'false', 'corsDomain': 'uk.finance.yahoo.com &.tsrc = finance'}
    result_list = []
    for key in world_indices:
        payload['symbols'] = key
        response = requests.get(url, params=payload, verify=False)
        response = json.loads(response.content)
        try:
            intraday_vlaues = response['spark']['result'][0]['response'][0]['indicators']['quote'][0]['close']
        except:
            continue

        closing_value = next((re for re in reversed(intraday_vlaues) if re), None)
        if not closing_value:
            print("An error occured , No closing value found")

        opening_value = response['spark']['result'][0]['response'][0]['meta']['previousClose']
        result_list.append((key, closing_value, opening_value))
    return result_list

pull_data_from_yahoo()