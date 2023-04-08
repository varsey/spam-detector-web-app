import streamlit as st
import joblib
import os

spam_clf = joblib.load(open(os.getcwd() + '/notebook/models/spam_detector_model.pkl', 'rb'))
vectorizer = joblib.load(open(os.getcwd() + '/notebook/models/vectorizer.pkl', 'rb'))


def main(title="Your Awesome Streamlit Text classification App".upper()):
    st.markdown(
        f"<h1 style='text-align: center; font-size: 65px; color: #4682B4;'>{title}</h1>",
        unsafe_allow_html=True
    )

    with st.expander("1. Ckeck if your text is a spam or ham 😀"):
        text_message = st.text_input("Please enter your message")
        if st.button("Predict"):
            prediction = spam_clf.predict(vectorizer.transform([text_message]))
            info = 'Ham' if prediction[0] == 0 else 'Spam'
            st.success(f'Prediction: {info}')


if __name__ == "__main__":
    main()
