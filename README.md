# Streamlit App for spam deplyment 
* Deployed with Docker

  * streamlit run - *for local test*
  * docker build -t streamlit-spam-detector -f build/Dockerfile .
  * docker run -p 8501:8501 streamlit-spam-detector