FROM python:3.11
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install --no-cache-dir --prefer-binary  -r requirements.txt
EXPOSE 8501
COPY . /app
ENTRYPOINT [ "streamlit", "run" ]
CMD ["app.py"]
