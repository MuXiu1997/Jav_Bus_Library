docker rm -f JBL_uwsgi_flask

docker rm -f JBL_nginx

docker run -d -p 5000:5000 --name JBL_uwsgi_flask\
 -v /JBL/Back_end_Flask/run.py:/app/run.py\
 -v /JBL/Models_SQLAlchemy/models.py:/app/models.py\
 -v /JBL/Models_SQLAlchemy/Jav_Bus.db:/app/Jav_Bus.db\
 -v /JBL/Config/uwsgi.ini:/app/uwsgi.ini\
 jbl_uwsgi_flask:latest

docker run -d -p 80:80 --name JBL_nginx\
 -v /JBL/Front_end_Vue:/app/html\
 -v /JBL/Config/nginx.conf:/etc/nginx/nginx.conf\
 -v /JBL/images:/app/images\
 nginx:1.16

