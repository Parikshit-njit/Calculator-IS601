FROM python:3

ADD . .

RUN pip install --upgrade pip
RUN pip3 install numpy

CMD [ "python" , "-m", "unittest", "discover", "-s", "calculator"]