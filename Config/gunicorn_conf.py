import multiprocessing

bind = '0.0.0.0:5000'
workers = multiprocessing.cpu_count()
pidfile = '/tmp/gunicorn.pid'
