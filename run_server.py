from subprocess import call

call(['docker', 'rm', '-f', 'JBL_redis'])
call(['docker', 'rm', '-f', 'JBL_flask_gunicorn'])
call(['docker', 'rm', '-f', 'JBL_nginx'])
call(['docker', 'run', '-d', '-p', '6379:6379', '--name', 'JBL_redis',
      '-v', '/JBL/Config/redis.conf:/usr/local/etc/redis/redis.conf',
      '-v', '/JBL/data:/data',
      'redis:5.0.5',
      'redis-server', '/usr/local/etc/redis/redis.conf'])

call(['docker', 'run', '-d', '-p', '5000:5000', '--name', 'JBL_flask_gunicorn',
      '-v', '/JBL/Back_end_Flask/manage.py:/app/manage.py',
      '-v', '/JBL/Back_end_Flask/app:/app/app',
      '-v', '/JBL/Config/gunicorn_conf.py:/app/gunicorn_conf.py',
      'jbl_flask_gunicorn:latest',
      'gunicorn', '-c', 'gunicorn_conf.py', 'manage:app'
      ])

call(['docker', 'run', '-d', '-p', '80:80', '--name', 'JBL_nginx',
      '-v', '/JBL/Front_end_Vue:/app/html',
      '-v', '/JBL/Config/nginx.conf:/etc/nginx/nginx.conf',
      '-v', '/JBL/images:/app/images',
      'nginx:1.16'])
