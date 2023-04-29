# Overview of the saved models

## Τρίτη, 11 Απριλίου 2023
Tried the following three models and hyperparameters. There was a serious bug in chatbot.py script that I have to change the training script and redo the training. First model includes the bug. Second model uses the fixed script. Third uses fixed script and Regulators. Training outcome looks promising. Regulators model might need a fee more epochs.

## 1_Automated Thai-FAQ Chatbot using RNN-LSTM - Training.h5
### Date: Τρίτη, 11 Απριλίου 2023

### Description
First training with satisfying results

### Dataset
intents.txt
267 Questions that each correspond to unique answers

### Model
model = Sequential()
model.add(Embedding(input_dim=len(documents), output_dim=100, input_length=MAXLEN))
model.add(SpatialDropout1D(0.2))
model.add(LSTM(100, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(267, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(x=np.array(padded_sequences), y=np.array(one_hot_features), epochs=1500, batch_size=32)

###Evaluation
9/9 [==============================] - 2s 93ms/step - loss: 0.0318 - accuracy: 1.0000
Test loss: 0.031756386160850525
Test accuracy: 1.0



## 2_Automated Thai-FAQ Chatbot using RNN-LSTM - Training.h5
### Date: Τρίτη, 11 Απριλίου 2023

### Description
Fixed major bug in chatbot.py where in case of an inserted word not in vocabulary the mapping of the word was assigned the number 1 which is index to an existing word in vocabulary:
-Added to training script a line that appended the '<PAD>' word to the vocabulary
-Changed chatbot script to assign the index of '<PAD>' to the missing word

### Dataset
intents.txt
267 Questions that each correspond to unique answers

### Model
model = Sequential()
model.add(Embedding(input_dim=len(documents), output_dim=100, input_length=MAXLEN))
model.add(SpatialDropout1D(0.2))
model.add(LSTM(100, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(len(documents), activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(x=np.array(padded_sequences), y=np.array(one_hot_features), epochs=1500, batch_size=32)

###Evaluation
9/9 [==============================] - 1s 18ms/step - loss: 0.0086 - accuracy: 1.0000
Test loss: 0.008580760098993778
Test accuracy: 1.0

### Notes
Model looks overfitted. Responds great to questions in the dataset. Responds poorly to new information.
Future work: Try less epochs


## 3_Automated Thai-FAQ Chatbot using RNN-LSTM - Training.h5
### Date: Τρίτη, 11 Απριλίου 2023

### Description
Attempt using Regulazer L2 = 0.01

### Dataset
intents.txt
267 Questions that each correspond to unique answers

### Model
model = Sequential()
model.add(Embedding(input_dim=len(documents), output_dim=100, input_length=MAXLEN))
model.add(SpatialDropout1D(0.2))
model.add(LSTM(100, dropout=0.2, recurrent_dropout=0.2, kernel_regularizer=l2(0.01)))
model.add(Dense(len(documents), activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(x=np.array(padded_sequences), y=np.array(one_hot_features), epochs=1500, batch_size=32)

###Evaluation
9/9 [==============================] - 1s 12ms/step - loss: 0.2966 - accuracy: 0.9738
Test loss: 0.29655295610427856
Test accuracy: 0.9737827777862549

## Notes
Forgot to save model. It needed further training anyaway.



## Τετάρτη, 12 Απριλίου 2023
Today I am training the following:
- Yesterday's Regularization Model to save model
- Main model with removed stopwords (pronouns included)
- Regularization model with removed stopwords (pronouns included) 1500 epochs
I would also like to test 1700 epochs training for regularized models (stopwords or not script). But so far results show it might not do any difference.


## 4_Automated Thai-FAQ Chatbot using RNN-LSTM - Training.h5
### Date: Τετάρτη, 12 Απριλίου 2023

### Description
Retrained 3_Automated Thai-FAQ Chatbot using RNN-LSTM - Training.h5 to save it

### Dataset
intents.txt
267 Questions that each correspond to unique answers

### Model
model = Sequential()
model.add(Embedding(input_dim=len(documents), output_dim=100, input_length=MAXLEN))
model.add(SpatialDropout1D(0.2))
model.add(LSTM(100, dropout=0.2, recurrent_dropout=0.2, kernel_regularizer=l2(0.01)))
model.add(Dense(len(documents), activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(x=np.array(padded_sequences), y=np.array(one_hot_features), epochs=1500, batch_size=32)

###Evaluation
9/9 [==============================] - 1s 10ms/step - loss: 0.2481 - accuracy: 0.9775
Test loss: 0.24810221791267395
Test accuracy: 0.9775280952453613

## Notes


## 5_Automated Thai-FAQ Chatbot using RNN-LSTM - Training.h5
### Date: Τετάρτη, 12 Απριλίου 2023

### Description
Removed stopwords from vocabulary. Trained with main model.

### Dataset
intents.txt
267 Questions that each correspond to unique answers

### Model
model = Sequential()
model.add(Embedding(input_dim=len(documents), output_dim=100, input_length=MAXLEN))
model.add(SpatialDropout1D(0.2))
model.add(LSTM(100, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(len(documents), activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(x=np.array(padded_sequences), y=np.array(one_hot_features), epochs=1500, batch_size=32)

###Evaluation
9/9 [==============================] - 1s 31ms/step - loss: 13.0744 - accuracy: 0.0075
Test loss: 13.074442863464355
Test accuracy: 0.00749063678085804

## Notes
Performed extremely poorly during evaluation in contrast to training.

## 6_Automated Thai-FAQ Chatbot using RNN-LSTM - Training.h5
### Date: Τετάρτη, 12 Απριλίου 2023

### Description
Removed stopwords from vocabulary. Trained with regularization model.

### Dataset
intents.txt
267 Questions that each correspond to unique answers

### Model
model = Sequential()
model.add(Embedding(input_dim=len(documents), output_dim=100, input_length=MAXLEN))
model.add(SpatialDropout1D(0.2))
model.add(LSTM(100, dropout=0.2, recurrent_dropout=0.2, kernel_regularizer=l2(0.01)))
model.add(Dense(len(documents), activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(x=np.array(padded_sequences), y=np.array(one_hot_features), epochs=1500, batch_size=32)

###Evaluation
9/9 [==============================] - 0s 7ms/step - loss: 12.3089 - accuracy: 0.0112
Test loss: 12.308941841125488
Test accuracy: 0.01123595517128706

## Notes


## Πέμπτη, 13 Απριλίου 2023
Today I have created a new augmented dataset from intents.txt and modified main and no stopwords script to train it. I am going to train 4 models:
- Main	1500 epochs
- Stopwords	1500 epochs
- Stopwords Regularized	1500 epochs
- Main Regularized 1500	epochs

## 7_Augmented Main.h5
### Date: Πέμπτη, 13 Απριλίου 2023

### Description
Trained augmented dataset with main model.

### Dataset
aug_intents.txt
267 Questions that each correspond to unique answers

### Model
model = Sequential()
model.add(Embedding(input_dim=len(documents), output_dim=100, input_length=MAXLEN))
model.add(SpatialDropout1D(0.2))
model.add(LSTM(100, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(int(len(documents)/4), activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(x=np.array(padded_sequences), y=np.array(one_hot_features), epochs=1500, batch_size=32)

###Evaluation
34/34 [==============================] - 1s 10ms/step - loss: 0.2646 - accuracy: 0.7912
Test loss: 0.2646045982837677
Test accuracy: 0.7911984920501709

## Notes
Not tested it yet with chatbot.py

## 7_Augmented Regularizer.h5
### Date: Πέμπτη, 13 Απριλίου 2023

### Description
Regularizer model for augmented dataset 1500 epochs

### Dataset
aug_intents.txt
267 Questions that each correspond to unique answers

### Model
model = Sequential()
model.add(Embedding(input_dim=len(documents), output_dim=100, input_length=MAXLEN))
model.add(SpatialDropout1D(0.2))
model.add(LSTM(100, dropout=0.2, recurrent_dropout=0.2, kernel_regularizer=l2(0.01)))
model.add(Dense(int(len(documents)/4), activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(x=np.array(padded_sequences), y=np.array(one_hot_features), epochs=1500, batch_size=32)

###Evaluation
34/34 [==============================] - 0s 6ms/step - loss: 0.4361 - accuracy: 0.7846
Test loss: 0.4361450672149658
Test accuracy: 0.7846441864967346

## Notes
Not tested it yet with chatbot.py

## 7_Augmented Stopwords.h5
### Date: Πέμπτη, 13 Απριλίου 2023

### Description
Augmented dataset Stopwords

### Dataset
aug_intents.txt
267 Questions that each correspond to unique answers

### Model
model = Sequential()
model.add(Embedding(input_dim=len(documents), output_dim=100, input_length=MAXLEN))
model.add(SpatialDropout1D(0.2))
model.add(LSTM(100, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(int(len(documents)/4), activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(x=np.array(padded_sequences), y=np.array(one_hot_features), epochs=1500, batch_size=32)

###Evaluation
Dataset in use:	 aug_intents.txt
34/34 [==============================] - 1s 9ms/step - loss: 33.7023 - accuracy: 0.0103
Test loss: 33.702335357666016
Test accuracy: 0.010299625806510448

## Notes

## .h5
### Date: Πέμπτη, 13 Απριλίου 2023

### Description


### Dataset
aug_intents.txt
267 Questions that each correspond to unique answers

### Model


model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(x=np.array(padded_sequences), y=np.array(one_hot_features), epochs=1500, batch_size=32)

###Evaluation


## Notes

## .h5
### Date: 

### Description


### Dataset
aug_intents.txt
267 Questions that each correspond to unique answers

### Model


model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(x=np.array(padded_sequences), y=np.array(one_hot_features), epochs=1500, batch_size=32)

###Evaluation


## Notes

