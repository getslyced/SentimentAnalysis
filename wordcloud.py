# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 23:24:03 2021

@author: sly
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from wordcloud import WordCloud, STOPWORDS


df = pd.read_csv("scrappedReviews.csv", index_col=0, encoding='latin-1')
all_reviews = ' '.join(df['reviews'].str.lower())

stopwords = STOPWORDS

wordcloud = WordCloud(stopwords=stopwords, background_color="white", max_words=100).generate(all_reviews)
rcParams['figure.figsize'] = 100, 200
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

wordcloud.to_file("wordcloud.png")
