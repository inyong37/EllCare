from keras.models import Sequential
from keras.layers import Dense
import numpy as np

dataset = np.loadtxt("test.txt", encoding='utf-8', delimiter="\t")
X = dataset[:, 0:12]
Y = dataset[:, 12]
model = Sequential()
model.add(Dense(12, input_dim=12, init='uniform', activation='relu'))
model.add(Dense(8, init='uniform', activation='relu'))
model.add(Dense(1, init='uniform', activation='sigmoid'))
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, Y, validation_split=0.2, nb_epoch=200, batch_size=20)
