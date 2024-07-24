import streamlit as st
from tf_keras.models import load_model
from tf_keras.datasets import imdb
from tf_keras.preprocessing import sequence


def check_prediction(review):
    # Load the model
    model = load_model("models/model50.keras")

    # Get the word:integer mapping
    word_idx = imdb.get_word_index()

    # Convert each word to integer
    inp = []
    for word in review.split():
        if word in word_idx.keys():
            inp.append(word_idx[word])
        else:
            inp.append(1)

    # Perform the padding
    final_input = sequence.pad_sequences([inp],maxlen=500)

    # Finally predict the sentiment
    result = model.predict(final_input)[0][0]
    print(result)
    if result > 0.5:
        return "Negative"
    else:
        return "Positive"

# Streamlit app
st.title("IMDB Reviews Sentiment Analysis")

# Input text box
review = st.text_area("Enter your review here")

# Predict button
submit = st.button("Check sentiment")

if submit:
    st.write("Sentiment: ",check_prediction(review))
