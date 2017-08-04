from keras.models import Sequential
from keras.layers import Dense, Activation
from keras import layers
import numpy
import keras

model = Sequential()
model.add(Dense(64, input_dim=100))
model.add(Activation("relu"))
model.add(Dense(10))
model.add(Activation("softmax"))

model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
x_train = numpy.random.random((1000,100))
y_train = keras.utils.to_categorical(numpy.random.randint(10, size=(1000,1)), num_classes=10)
x_test = numpy.random.random((100,100))
y_test = keras.utils.to_categorical(numpy.random.randint(10, size=(100,1)), num_classes=10)
print (model.get_config())
print (model.summary())
print (layers.get_config())
#print (model.get_layer())
#print (model.get_weights())
print (model.to_json())
#model.fit(x_train, y_train, epochs=5, batch_size=32)
#model.train_on_batch(x_batch, y_batch)

#score = model.evaluate(x_test, y_test,  batch_size=128)
#print ("score is", score, model.metrics_names)
