# -*- coding: utf-8 -*-
"""Untitled73.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13j5Xk0IKqHjXB9FVweYclRnOuvjD2pVY
"""

pip install textblob

import textblob
import subprocess
cmd = ['python','-m','textblob.dowload_corpora']
subprocess.run(cmd)

from textblob import TextBlob

text = 'Today is a beautiful day. Tomorrow looks like bad waether.'

blob = TextBlob(text)

blob

blob.sentences

blob.words

blob

blob.tags

blob.noun_phrases