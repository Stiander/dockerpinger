FROM python:3.6
COPY ./pinger/requirements.txt /home/broentech/requirements.txt
RUN pip install -r /home/broentech/requirements.txt
COPY ./pinger/pinger.py /home/broentech/pinger.py
COPY ./pinger /home/broentech/pinger
WORKDIR /home/broentech
CMD bash -c "python -u /home/broentech/pinger.py"
