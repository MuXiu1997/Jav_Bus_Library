FROM python:3.7.3

RUN pip install sqlalchemy -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

RUN pip install scrapy -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

RUN pip install Pillow -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

RUN cd / && mkdir app

WORKDIR /app

CMD ["bash"]
