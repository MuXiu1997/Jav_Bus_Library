FROM python:3.7.3

RUN pip install flask -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

RUN pip install flask-cors -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

RUN pip install uwsgi -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

RUN pip install sqlalchemy -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

COPY ./uwsgi.ini /app/uwsgi.ini

EXPOSE 5000

CMD ["uwsgi", "--ini", "/app/uwsgi.ini"]