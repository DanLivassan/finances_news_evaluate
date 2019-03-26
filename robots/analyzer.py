
# -*- coding: utf-8 -*-
from __future__ import print_function
from credentials import *
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, SentimentOptions, KeywordsOptions
import json


class Analyzer():

    service = NaturalLanguageUnderstandingV1(
        version='2018-11-16',
        url='https://gateway.watsonplatform.net/natural-language-understanding/api',
        iam_apikey=WATSON_CREDENTIALS['apikey'])

    def analyze_sentiment(self, list_of_bluechips, list_of_news):
        response=json.loads('{"error":"No content"}')
        for new in list_of_news:
            for article in new:
                response = self.service.analyze(
                    text=article['description'],
                    features=Features(sentiment=SentimentOptions(targets=list_of_bluechips),
                                      keywords=KeywordsOptions())).get_result()
                print(json.dumps(response, indent=2))
        return response