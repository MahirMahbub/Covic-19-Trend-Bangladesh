# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 18:40:26 2020

@author: Mahir Mahbub
"""
# %%
import pandas as pd
import numpy as np
import tensorflow as tf

from tensorflow.keras.layers import LSTM, Dropout, Dense
from tensorflow.keras import optimizers, Sequential
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range=(0,1))
# %%
final_similar_data = pd.read_csv(r"..\weather_similar_confirmed.csv")
# %%
#sc = MinMaxScaler(feature_range=(0,1))
test_bangladesh_data = final_similar_data.iloc[[0]]
train_data = final_similar_data.iloc[1:]
# %%
TIME_STEPS = 5
LABEL_STEPS = 2
BATCH_SIZE = 18
loop_go = final_similar_data.shape[1] - TIME_STEPS - LABEL_STEPS
X_train = []
Y_train = []
for country_data in train_data.values:
    full_sequence = np.diff(country_data[2:])
    for start in range(loop_go-2):
        X_train.append(full_sequence[start:TIME_STEPS+start])
        Y_train.append(full_sequence[TIME_STEPS+start: TIME_STEPS+start+LABEL_STEPS])

X_train = np.array(X_train).reshape(552, 5, 1).astype(np.float64)
Y_train = np.array(Y_train).reshape(552, 2).astype(np.float64)

# %%

#, batch_input_shape=(12, 5, 1),

''' 
lstm_model = Sequential()
lstm_model.add(LSTM(100, dropout=0.0, recurrent_dropout=0.0, stateful=False, kernel_initializer='random_uniform'))
lstm_model.add(Dropout(0.5))
#lstm_model.add(Dense(20,activation='relu'))
lstm_model.add(Dense(1,activation='sigmoid'))
#optimizer = optimizers.RMSprop(lr=0.001)
lstm_model.compile(loss='mean_squared_error', optimizer="adam")

history = lstm_model.fit(X_train, Y_train, epochs=200, verbose=2, batch_size=BATCH_SIZE,
                    shuffle=False)
'''
model = Sequential()
model.add(LSTM(units=100,return_sequences=True,input_shape=(X_train.shape[1], 1)))
model.add(Dropout(0.2))
model.add(LSTM(units=100,return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=100,return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=100))
#model.add(Dropout(0.2))
model.add(Dense(units=2))
optimizer = optimizers.RMSprop(lr=0.001)
es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=100)
model.compile(optimizer=optimizer, loss='mean_squared_error')
model.fit(X_train,Y_train,epochs=200, batch_size=BATCH_SIZE, validation_split = 0.2, callbacks=[es])
# %%
#	Bangladesh	23.685	90.3563	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	3	3	3	3	3	3	3	5	8	10	14
# [5, 8, 10, 14, 17, 20]
x_ = np.array(np.diff([ 3, 5, 8, 10, 14, 17])).reshape(1,5, 1)
print(model.predict(x_))

test_full_sequence = test_bangladesh_data.values
# %%
test_full_sequence = test_full_sequence.reshape(test_full_sequence.shape[1], 1)[2:]
test_full_sequence = np.append(test_full_sequence, [5, 8, 10]).astype(np.float64)
test_full_sequence = np.diff(test_full_sequence)

#%%
X_test = []
Y_test = []
for start in range(loop_go+3-2):
    X_test.append(test_full_sequence[start:TIME_STEPS+start])
    Y_test.append(test_full_sequence[TIME_STEPS+start: TIME_STEPS+start+LABEL_STEPS])
# %%
X_test = np.array(X_test).reshape(49,  5, 1).astype(np.float64)
#Y_test = np.array(Y_test).reshape(48, 2).astype(np.float64)
predicted = np.floor(model.predict(X_test))
first_day = []
second_day = []
for pred in predicted:
    first_day.append(pred[0])
    second_day.append(pred[1])