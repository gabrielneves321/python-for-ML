# -*- coding: utf-8 -*-
"""Untitled78.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Vv1z5L0jD97Uy9wMkEgCosN2aBVEQB9I
"""

import textblob
from textblob import TextBlob
text = 'Today is a beautiful day. Tomorrow looks like bad weather.'
blob = TextBlob(text)
blob

spanish = blob.translate(to='es')

spanish

chinese = blob.translate(to='zh')

chinese

chinese = blob.translate(from_lang='en', to='zh')

spanish.translate()

chinese.translate()

from textblob import Word
index = Word('index')

index.pluralize()

cacti = Word('cacti')
cacti.singularize()

import nltk
nltk.download('punkt')

from textblob import TextBlob
animals = TextBlob('dog cat fish bird').words

animals.pluralize()

# Commented out IPython magic to ensure Python compatibility.
from textblob import Word
word = Word('theyr')
# %precision 2

word.spellcheck()

word.correct()

from textblob import Word
sentence = TextBlob('Ths sentense has missplled wrds.')
sentence.correct()