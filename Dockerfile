FROM python:3.12
WORKDIR /usr/src/app
COPY main.py ./
COPY requirements.txt ./
RUN pip install pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "main.py" ]
