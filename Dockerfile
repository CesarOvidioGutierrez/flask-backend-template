FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=5000

EXPOSE $PORT

CMD flask run --host=0.0.0.0 --port=$PORT

