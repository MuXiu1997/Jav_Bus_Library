docker rm -f JBL_redis

docker rm -f JBL_uwsgi_flask

docker rm -f JBL_nginx

docker run -d -p 6379:6379 --name JBL_redis\
 -v /JBL/Config/redis.conf:/usr/local/etc/redis/redis.conf\
 -v /JBL/data:/data\
 redis:5.0.5 redis-server /usr/local/etc/redis/redis.conf

docker run -d -p 5000:5000 --name JBL_uwsgi_flask\
 -v /JBL/Back_end_Flask/manage.py:/app/manage.py\
 -v /JBL/Back_end_Flask/app:/app/app\
 -v /JBL/Config/uwsgi.ini:/app/uwsgi.ini\
 jbl_uwsgi_flask:latest

docker run -d -p 80:80 --name JBL_nginx\
 -v /JBL/Front_end_Vue:/app/html\
 -v /JBL/Config/nginx.conf:/etc/nginx/nginx.conf\
 -v /JBL/images:/app/images\
 nginx:1.16
