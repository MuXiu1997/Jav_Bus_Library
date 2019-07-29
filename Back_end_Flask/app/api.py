from flask import Blueprint, jsonify, Response, request
from redis import ConnectionPool, Redis

api = Blueprint('api', __name__)
# redis_pool = ConnectionPool(host='172.17.0.1', port=6379, db=0, decode_responses=True)
redis_pool = ConnectionPool(host='192.168.217.132', port=6379, db=0, decode_responses=True)


@api.route('/api/videos/')  # list页数据
def get_videos():
    rds = Redis(connection_pool=redis_pool)
    list_keys = rds.keys('l_*')
    pipe = rds.pipeline()
    [pipe.hgetall(key) for key in list_keys]
    result = pipe.execute()
    response = jsonify(result)
    return response


@api.route('/api/videos/<designation>/details/')  # detail页数据
def get_video_details(designation):
    rds = Redis(connection_pool=redis_pool)
    result = rds.get('d_{}'.format(designation))
    response = Response(result, mimetype='application/json')
    return response


@api.route('/api/videos/<designation>/', methods=['PUT'])  # 修改是否收藏
def put_video(designation):
    is_like = request.json.get('il')  # 0/1/'0'/'1'

    rds = Redis(connection_pool=redis_pool)
    try:
        rds.hset('l_{}'.format(designation), 'il', is_like)
        response = jsonify(result='succeed', error=None)
    except Exception as e:
        response = jsonify(result='error', error=e)
    return response
