from tf_keras import Sequential
from tf_keras.layers import Embedding, SimpleRNN, Dense, Dropout
from tf_keras.callbacks import ModelCheckpoint, EarlyStopping

def create_model():
    model = Sequential()
    model.add(Embedding(50000,64))
    model.add(SimpleRNN(64))
    model.add(Dense(1,activation='sigmoid'))
    model.compile(optimizer='rmsprop',loss='binary_crossentropy',metrics=['acc'])
    return model

def set_callbacks():
    checkpoint = ModelCheckpoint("models/best_model50.keras", monitor='val_loss', verbose=0, save_best_only=True, save_weights_only=False)
    earlystop = EarlyStopping(monitor='val_acc',patience=1)
    return [checkpoint,earlystop]


create_model().summary()