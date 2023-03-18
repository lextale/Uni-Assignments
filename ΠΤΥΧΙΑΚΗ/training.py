# Training 
#Source: https://buffml.com/web-based-chatbot-using-flask-api/
#@title training.py
#Dataset: intents.json

import random
import json
import pickle
import numpy as np

import nltk
nltk.download('punkt')
nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD

lemmatizer = WordNetLemmatizer()

intents = json.loads(open('intents.json').read())

vocabulary =[]   # λ΄΄ιστα όλων των λέξεων στο patterns του dataset
classes = []
documents = []
ignore_letters = ['?', '!', ',', '.']

for intent in intents['intents']:
    for pattern in intent['patterns']:
        # Tokenization of question pattern
        word_list = nltk.word_tokenize(pattern)
        word_list = [lemmatizer.lemmatize(word.lower()) for word in word_list]


        # Vocabulary
        for w in word_list:
            if(w not in vocabulary):
                vocabulary.extend(word_list)
        
        # Class
        if intent['tag'] not in classes:
            classes.append(intent['tag'])
        
        # Save each tokenized question with its class
        documents.append((word_list, intent['tag']))

# Lemmatizer of vocabulary
vocabulary = [lemmatizer.lemmatize(word) for word in vocabulary if word not in ignore_letters]
vocabulary = sorted(set(vocabulary))
classes = sorted(set(classes))

pickle.dump(vocabulary, open('vocabulary.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

training = []
output_empty = [0] * len(classes)
for document in documents:
    bag = []
    word_patterns = document[0]
    for word in vocabulary:
        bag.append(1) if(word in word_patterns) else bag.append(0)

    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1
    training.append([bag, output_row])

random.shuffle(training)
training = np.array(training)
train_x = list(training[:, 0])
train_y = list(training[:, 1])

model = Sequential()
print('Training 0/5')
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
print('Training 1/5')
model.add(Dropout(0.5))
print('Training 2/5')
model.add(Dense(64, activation='relu'))
print('Training 3/5')
model.add(Dropout(0.5))
print('Training 4/5')
model.add(Dense(len(train_y[0]), activation='softmax'))
print('Training 5/5')

model.compile(loss='categorical_crossentropy', optimizer="adam", metrics=['accuracy'])

hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
model.save('chatbot_model.h5', hist)

print('Done!')
