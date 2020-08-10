FROM python:3.7

WORKDIR /api

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

RUN export PYTHONPATH=*'${PYTHONPATH}:/app'

COPY  .  .

CMD ["python", "./runapi.py"]