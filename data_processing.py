from tf_keras.datasets import imdb
from tf_keras.preprocessing.sequence import pad_sequences


def load_data():
    ((XT, YT), (Xt, Yt)) = imdb.load_data(num_words=50000)
    print(XT.shape, YT.shape, Xt.shape, Yt.shape)
    return XT, YT, Xt, Yt

XT, YT, Xt, Yt = load_data()

def pad_data(XT, Xt, maxlen=500):
    XT = pad_sequences(XT, maxlen=maxlen)
    Xt = pad_sequences(Xt, maxlen=maxlen)
    print(XT.shape, Xt.shape)
    return XT, Xt

word_idx = imdb.get_word_index()
idx_word = dict([value,key] for (key,value) in word_idx.items())
actual_review = ' '.join([idx_word.get(idx-3,'?') for idx in XT[0]])
print(actual_review)
print(len(actual_review.split()))