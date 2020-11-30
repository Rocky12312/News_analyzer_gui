import re
import nltk
import keras
import pickle
import string
import numpy as np
import tkinter as tk
import tensorflow as tf
from textblob import TextBlob
from newspaper import Article
from nltk.corpus import stopwords
from keras.models import load_model
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

#Loading the tokenizerfor tokenizing the input text(news text)
with open('tokenizer1.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)
    
#Loading the model(fake news classification mode)
model = load_model("Fake_news_classifier1.h5")

#Will be using word net lemmatizer to reduce the word to base form
lemmatizer = WordNetLemmatizer()

nltk.download('stopwords')

nltk.download('punkt')

nltk.download("wordnet")



def preprocessing(line):
    line = line.lower()
    tokens = word_tokenize(line)
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in tokens]
    words = [word for word in stripped if word.isalpha()]
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if not w in stop_words]
    words = [lemmatizer.lemmatize(w) for w in words]
    return " ".join(words)

#The function below will give a op(1 means the news is real and 0 means news is fake)
def fnews(text):
    text = preprocessing(text)
    text = [text]
    text = tokenizer.texts_to_sequences(text)
    text = tf.keras.preprocessing.sequence.pad_sequences(text, padding='post', maxlen=256)
    pred = model.predict(text)
    a = pred>0.5
    #a = np.argmax(model.predict(text), axis=-1)
    return a
