from tf_keras.models import load_model
from tf_keras.datasets import imdb
from tf_keras.preprocessing import sequence

sent = "I really liked the movie. It was a great movie. I would recommend it to my friends."
inp = []

# Load the model
model = load_model("model50.keras")

# Get the word:integer mapping
word_idx = imdb.get_word_index()

print(word_idx[:5])

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