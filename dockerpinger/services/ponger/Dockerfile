FROM python:3.6
COPY ./ponger/requirements.txt /home/broentech/requirements.txt
RUN pip install -r /home/broentech/requirements.txt
COPY ./ponger/ponger.py /home/broentech/ponger.py
COPY ./ponger /home/broentech/ponger
WORKDIR /home/broentech
CMD bash -c "python -u /home/broentech/ponger.py"
