from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import optimizers
import numpy as np

import input_data


model = Sequential()
model.add(Dense(units=18, activation='sigmoid', input_dim=26))
model.add(Dense(units=1, activation='sigmoid'))

sgd = optimizers.SGD(lr=1)
model.compile(loss='mean_squared_error', optimizer=sgd)

data = input_data.InputData()
model.fit(data.X, data.Y, epochs=1500, verbose=False)

test = input("Word: ").lower()
gen = np.array([input_data.make_data(test)])
print(model.predict(gen))
