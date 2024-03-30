import streamlit as st
from transformers import pipeline
from PIL import Image

sentiment_pipeline = pipeline("text-classification", model="crypter70/IndoBERT-Sentiment-Analysis")

def getEmoji(label, score):
    if label == "POSITIVE":
        image = Image.open('./images/positive.PNG')
    elif label == "NEUTRAL":
        image = Image.open('./images/neutral.PNG')
    elif label == "NEGATIVE":
        image = Image.open('./images/negative.PNG')
    
    st.text("")
    st.write("Score: ", score)
    st.image(image, caption=label)
    

def getSentiment(text):
    label = sentiment_pipeline(text)[0]['label']
    score = str(sentiment_pipeline(text)[0]['score'])[:5]

    return label, score


def main():
    
    st.title("Sentiment Analysis WebApp 😊😐🙁")
    st.subheader("Indonesian and English")
    st.text("Analyzing textual data provided by the user to identify sentiments within it.")
    st.text("")   

    example_list = ["Doi asik bgt orangnya", "Ada pengumuman nih gaiss, besok liburr", "Kok gitu sih kelakuannya"]
    options = example_list + ["Input a new text ..."]

    selection = st.selectbox("Input Text", options=options)

    text = ""

    if selection == "Input a new text ...": 
        otherOption = st.text_input("Enter your text...")
        text = otherOption
    else:
        text = selection

    if st.button("Predict"):
        with st.spinner('Predict the sentiment...'):
            label, score = getSentiment(text)
            getEmoji(label, score)

    st.markdown("---")
    st.markdown("<div style='text-align: center;'>Powered by <a href='https://huggingface.co/crypter70/IndoBERT-Sentiment-Analysis' target='_blank'>IndoBERT-Sentiment-Analysis</a></div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()