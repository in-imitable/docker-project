FROM python

WORKDIR /usr/src/app

COPY . .

CMD [ "python", "./myfile.py" ]