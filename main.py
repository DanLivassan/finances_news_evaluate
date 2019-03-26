
# -*- coding: utf-8 -*-
from __future__ import print_function
import json

import requests
from credentials import *
from datetime import datetime
from robots.reader import Reader
from robots.analyzer import Analyzer

reader = Reader()
analyzer = Analyzer()

news = []
for bluechip in reader.blue_chips:
    news.append(reader.get_everything_from_api(q=bluechip)['articles'])

analyzer.analize_sentiment(reader.blue_chips, news)

