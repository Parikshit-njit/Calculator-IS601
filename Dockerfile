FROM python:3

ADD src .

RUN pip install --upgrade pip

CMD [ "python" , "-m", "unittest", "discover", "-s", "Calculator"]