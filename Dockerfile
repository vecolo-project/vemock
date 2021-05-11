FROM pypy:3-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
VOLUME /usr/src/app/history

CMD [ "pypy3", "./main.py" ]