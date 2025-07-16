FROM python:3

WORKDIR /aquamaringa

COPY . .

RUN rm -rf .venv

RUN pip install --upgrade pip

RUN mkdir -p static

RUN pip install -r requirements.txt

CMD alembic upgrade head && uvicorn api:app --host 0.0.0.0 --port 8083 --reload