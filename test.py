from tf_keras.models import load_model
from tf_keras.datasets import imdb
from tf_keras.preprocessing import sequence

from data_processing import Xt, XT, Yt, pad_data

sent = "Terrible movie terrible acting terrible plot. Waste of time DO NOT watch"
inp = []

# Load the model
model = load_model("models/model50_8.keras")

# evaluate the model
XT, Xt = pad_data(XT, Xt)
model.evaluate(Xt,Yt)

# Get the word:integer mapping
word_idx = imdb.get_word_index()

# print(word_idx[:5])

# Convert each word to integer
for word in sent.split():
  if word in word_idx.keys():
    inp.append(word_idx[word])
  else:
    inp.append(1)

print(inp) 

# Perform the padding
final_input = sequence.pad_sequences([inp],maxlen=500)

# Finally predict the sentiment
print(model.predict(final_input))