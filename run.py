from tensorflow import keras
import numpy as np
import input_data

model = keras.models.load_model('neural_network.model')

while 1:
    test = input("Word: ").lower()
    gen = np.array([input_data.make_data(test)])
    print(model.predict(gen))
