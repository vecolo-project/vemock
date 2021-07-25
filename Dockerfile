FROM python:3-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
VOLUME /usr/src/app/history

ENV station_id=6 \
    auto_off=true \
    max_seats=12 \
    history_path="history.json" \
    frequency_wait=2 \
    max_charge=20 \
    jwt_token="secret-token"\
    api_endpoint="https://localhost"\
    debug=false

CMD [ "python","-u", "./main.py" ]