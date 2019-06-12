import os

from sqlalchemy import create_engine, Column, String, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_file_name = 'Jav_Bus.db'  # SQLite文件名
db_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), db_file_name)  # SQLite文件所在路径
# sqlite默认建立的对象只能让建立该对象的线程使用，而sqlalchemy是多线程的
# 所以我们需要指定check_same_thread=False来让建立的对象任意线程都可使用
engine = create_engine('sqlite:///{}?check_same_thread=False'.format(db_file_path), echo=False)  # 创建数据库连接
Base = declarative_base()  # 建立基本映射类，用于继承
Session = sessionmaker(bind=engine)  # 创建CRUD的会话类
# session = Session()  # Session类实例化


# info表的映射模型
class Info(Base):
    # 表名
    __tablename__ = 'info'

    designation = Column(String(), primary_key=True, unique=True)
    designation_title = Column(String())
    publish_time = Column(String())
    star_name = Column(String())
    magnet_infos = Column(String())
    sample_count = Column(Integer())
    magnet_count = Column(Integer())
    url_list = Column(String())
    is_like = Column(Boolean())


if __name__ == '__main__':
    # 建表
    Base.metadata.create_all(engine)
