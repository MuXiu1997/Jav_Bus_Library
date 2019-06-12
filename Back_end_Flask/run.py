import json

from flask import Flask, jsonify, Response, request
from flask_cors import CORS
from models import Info, Session
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})  # 使前端能从后端拿到数据


@app.route("/api/GET/table-data")  # index页数据
def index():
    session = Session()

    host = request.host_url
    designation = request.args.get('designation')
    star_name = request.args.get('starName')
    is_like = request.args.get('isLike')
    current_page = int(request.args.get('currentPage'))

    conditions = []  # 查询条件
    if designation:
        for designation_kw in designation.split(' '):
            conditions.append(Info.designation.like(''.join(('%', designation_kw.upper(), '%'))))
    if star_name:
        for star_name_kw in star_name.split(' '):
            conditions.append(Info.star_name.like(''.join(('%', star_name_kw.upper(), '%'))))
    if is_like:
        conditions.append(Info.is_like == int(is_like))

    all_data_obj = session.query(
        Info.designation,
        Info.designation_title,
        Info.star_name,
        Info.publish_time,
        Info.sample_count,
        Info.magnet_count,
        Info.is_like
    ).filter(*conditions)

    logging.debug(all_data_obj.statement.compile(compile_kwargs={"literal_binds": True}))  # 查看SQL语句

    all_data_len = all_data_obj.count()
    if all_data_len < (current_page - 1) * 50:
        current_page = all_data_len // 50 + 1

    table_data = all_data_obj.order_by(Info.publish_time.desc()).slice(current_page * 50 - 50, current_page * 50).all()

    response_table_data = []
    for each_data in table_data:
        response_table_data.append(
            {'cover': '{}images/{}/{}.jpg'.format(host,
                                                  each_data.designation,
                                                  each_data.designation),
             'designation': each_data.designation,
             'designationTitle': each_data.designation_title,
             'starName': each_data.star_name,
             'publishTime': each_data.publish_time,
             'sampleCount': each_data.sample_count,
             'magnetCount': each_data.magnet_count,
             'isLike': each_data.is_like})

    session.close()

    return jsonify({
        'tableData': response_table_data,
        'len': all_data_len,
        'currentPage': current_page
    })


@app.route('/api/PATCH/table-data/is-like', methods=['PATCH'])  # 修改是否收藏
def is_like_change():
    session = Session()

    designation = request.json.get('designation')
    is_like = request.json.get('isLike')
    data = session.query(Info).get(designation)
    data.is_like = is_like

    session.commit()
    session.close()

    return Response(status=200)


@app.route('/api/GET/infos/')  # info页数据
def info():
    session = Session()

    host = request.host_url
    designation = request.args.get('designation')
    data = session.query(Info).get(designation)
    response = dict()
    response['urlList'] = list(map(
        lambda url: '{}images/{}/{}'.format(host, data.designation, url), json.loads(data.url_list)
    ))
    response['magnetTableData'] = json.loads(data.magnet_infos)

    session.close()

    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
