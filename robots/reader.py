
# -*- coding: utf-8 -*-
from __future__ import print_function
import json


import requests
from credentials import *
from datetime import datetime


class Reader():

    configs = {
            'endpoints': {
                'headlines': 'top-headlines',
                'everything': 'everything'
            },
            'urls': {
                'api_url': 'https://newsapi.org/v2/{}'
            }
    }

    api_url = 'https://newsapi.org/v2/{}'
    blue_chips = ['petrobras', 'itau']

    def get_headlines_from_api(self):
        r = requests.get(self.configs['urls']['api_url'].format(self.configs['endpoints']['headlines']),
                         params=
                         {
                             'sources': 'info-money',
                             'apiKey': NEWS_CREDENTIALS['apikey']
                         })

        return json.loads(r.text)

    def get_everything_from_api(self, q, date_from=datetime.now().strftime("%Y-%m-%d"),
                                date_to=datetime.now().strftime("%Y-%m-%d")):
        r = requests.get(self.configs['urls']['api_url'].format(self.configs['endpoints']['everything']),
                         params=
                         {
                             'sources': 'info-money',
                             'from_param': date_from,
                             'to': date_to,
                             'apiKey': NEWS_CREDENTIALS['apikey'],
                             'q': q,
                         }
                         )
        return json.loads(r.text)
