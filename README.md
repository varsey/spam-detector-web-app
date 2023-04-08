# Streamlit and FastAPI apps for spam detection 
* Deployed with Docker

Streamlit:
  * streamlit run app-streamlit - *for local test*
  * docker build -t streamlit-spam-detector -f build/Dockerfile-streamlit .
  * docker run -p 8501:8501 streamlit-spam-detector

FastAPI:
  * uvicorn app-fastapi:app --reload- *for local test*
  * docker build -t fastapi-spam-detector -f build/Dockerfile-fastapi .
  * docker run -p 80:80 fastapi-spam-detector