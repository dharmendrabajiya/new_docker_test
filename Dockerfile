FROM python:3-alpine

WORKDIR /usr/flask_uuid

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3","main.py"]