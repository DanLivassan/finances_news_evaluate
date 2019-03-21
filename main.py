# -*- coding: utf-8 -*-
from __future__ import print_function
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions
import requests


api_url = 'https://newsapi.org/v2/top-headlines?sources=info-money&apiKey=35ea20fd8b00426497eacb6d963baed0'


def get_news_from_api():
    r = requests.get(api_url)
    return json.loads(r.text)


# If service instance provides API key authentication
service = NaturalLanguageUnderstandingV1(
     version='2018-11-16',
     ## url is optional, and defaults to the URL below. Use the correct URL for your region.
     url='https://gateway.watsonplatform.net/natural-language-understanding/api',
     iam_apikey='sl2YVw3CSbT9KSfDKN_WsSZG6lbjGyMJOGToF8dGmo6o')

for article in get_news_from_api()['articles'][:1]:
    print(json.dumps(article))
    response = service.analyze(
        url=article['url'],
        features=Features(entities=EntitiesOptions(),
                          keywords=KeywordsOptions())).get_result()
    print(json.dumps(response, indent=2))
