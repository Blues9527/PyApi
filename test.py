import flask, json
from database.db_helper import DBHelper
from network.clazz_message import Message

server = flask.Flask(__name__)


@server.route('/index', methods=['get', 'post'])
def index():
    m = Message()
    m.set_msg('这是我第一个接口')
    m.set_code('200')
    return m.to_json()


@server.route('/login', methods=['get', 'post'])
def login():
    username = flask.request.values.get('username')
    password = flask.request.values.get('password')

    print('username:  %s  password:  %s' % (username, password))

    # 先判断用户名和密码是否为空，为空则返回404
    if username is None or password is None:
        m = Message()
        m.set_msg('params is null')
        m.set_code('500')
        return m.to_json()

    # 再判断数据库里是否有对应的用户名和密码
    if tuple(DBHelper().db_select(
            'select * from user where username = \'%s\' and  password = \'%s\'' % (username, password))).__len__() == 0:
        # 如果查询返回的tuple为空，实际情况是登陆失败跳到注册
        m = Message()
        m.set_msg('login failed')
        m.set_code('500')
        return m.to_json()

    else:
        m = Message()
        m.set_msg('login success')
        m.set_code('200')
        return m.to_json()


@server.route('/register', methods=['get', 'post'])
def register():
    username = flask.request.values.get('username')
    password = flask.request.values.get('password')

    if username is None or password is None:
        m = Message()
        m.set_msg('register failed , params are null')
        m.set_code('500')
        return m.to_json()
    elif tuple(DBHelper().db_select('select * from user where username = \'%s\'' % username)).__len__() == 0:
        DBHelper().db_execute('insert into user(username,password) values (\'%s\',\'%s\')' % (username, password))
        m = Message()
        m.set_msg('register success')
        m.set_code('200')
        return m.to_json()
    else:
        m = Message()
        m.set_msg('username is already exits')
        m.set_code('500')
        return m.to_json()


server.run(port=8090, debug=True, host='192.168.33.93')
