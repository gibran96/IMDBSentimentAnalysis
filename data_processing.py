from tf_keras.datasets import imdb
from tf_keras.preprocessing.sequence import pad_sequences
import numpy as np

def load_data():
    ((XT, YT), (Xt, Yt)) = imdb.load_data(num_words=50000)
    print(XT.shape, YT.shape, Xt.shape, Yt.shape)
    return XT, YT, Xt, Yt

def pad_data(XT, Xt, maxlen=500):
    XT = pad_sequences(XT, maxlen=maxlen)
    Xt = pad_sequences(Xt, maxlen=maxlen)
    print(XT.shape, Xt.shape)
    return XT, Xt

def l1_norm(XT, Xt):
    return np.sum(np.abs(XT),axis=1), np.sum(np.abs(Xt),axis=1)

def l2_norm(XT, Xt):
    return np.sqrt(np.sum(np.square(XT))), np.sqrt(np.sum(np.square(Xt)))

XT, YT, Xt, Yt = load_data()

XT, Xt = pad_data(XT, Xt)
Xt, Xt = l2_norm(XT, Xt)
print(XT.shape, Xt.shape)

# word_idx = imdb.get_word_index()
# idx_word = dict([value,key] for (key,value) in word_idx.items())
# actual_review = ' '.join([idx_word.get(idx-3,'?') for idx in XT[0]])
# print(actual_review)
# print(len(actual_review.split()))