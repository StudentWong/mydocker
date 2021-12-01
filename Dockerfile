FROM python:3.6.4

MAINTAINER studentwang2006

ENV environment1=asd

ENV environment2=edf

run mkdir /app 

add test.py /app

workdir /app

cmd ["python", "test.py", "10", "zxc", "key"]
