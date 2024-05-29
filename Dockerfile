FROM python:3.10-slim
RUN pip install --upgrade pip
COPY . /apps
WORKDIR /apps
RUN pip install -r requirements.txt
CMD ["python", "make_prediction.py"]