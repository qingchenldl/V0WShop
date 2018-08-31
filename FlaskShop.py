#encoding: utf-8
from flask import *
import pymysql
import hashlib
import config
from models import *
from datetime import datetime


app = Flask(__name__)
app.config.from_object(config)

db = pymysql.connect(**config.mysql_config)
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
user = User()
goods = Goods()

# 初始化数据库
def init_db():
    with app.app_context():
        with app.open_resource('flaskshop.sql', mode='r') as f:
            cursor.execute(f.read())
        db.commit()

@app.route('/')
@app.route('/index/')
def index():
    # user=session.get('user_id')
    return render_template('index.html')

@app.route('/login/',methods=['GET','POST'])
def login():
    error = None
    if request.method == 'GET':
        return render_template('login.html',error=error)
    else:
        tel = request.form.get('telephone')
        password = request.form.get('password')
        if tel is None or password is None:
            error = u'手机号码或密码未填写完整'
            return render_template('login.html',error=error)
        else:
            if tel.isdigit() is not True:
                error=u'手机号码格式不正确，你是想SQL注入吗？'
                return render_template('login.html',error=error)
            else:
                telsql= "SELECT * from users where telephone='"+tel+"';"
                # print telsql
                cursor.execute(telsql)
                res = cursor.fetchone()
                # print result
                if res is None:
                    error = u'不存在该用户,请先注册！'
                    return render_template('login.html', error=error)
                else:
                    passmd5 = hashlib.md5(password).hexdigest()
                    # print passmd5
                    # print res[2]
                    if passmd5 != res[2]:
                        error = u'密码错误！请确认密码'
                        return render_template('login.html', error=error)
                    else:
                        user.setall(res)
                        # print user.username
                        session['user_id'] = user.tel
                        session.permanent = True
                        return redirect(url_for('index'))

@app.route('/detail/<gid>/',methods=['GET','POST'])
def detail(gid):
    buy=0
    user_id = session.get('user_id')
    if user_id is None:
        return redirect(url_for('login'))
    else:
        goodsql = "select * from goods where gid="+gid+";"
        # print goodsql
        cursor.execute(goodsql)
        res = cursor.fetchone()
        # print res
        goods.setall(res)
        g.goods = goods

        if request.method == 'GET':
            return render_template('detail.html')
        else:
            # print goods.price
            yu_e = user.getmoney()-goods.price
            if yu_e < 0:
                error = u"余额不足"
                return render_template('detail.html',error=error)
            else:
                user.setmoney(yu_e)
                # 修改数据库的值
                # 将历史呢数据存到history
                updatesql = "UPDATE users SET money="+str(yu_e)+" WHERE telephone='"+user_id+"';"
                now = str(datetime.now()).split('.')[0]
                if cursor.execute(updatesql):
                    buy = 1
                else:
                    error=u'未知错误'
                    return render_template('detail.html', error=error)
                # print now
                historysql = "INSERT INTO history (telphone,gid,datetime) VALUES('"+user.tel+"','"+goods.gid+"','"+now+"');"
                if cursor.execute(historysql):
                    history = u'购物历史添加成功'
                else:
                    history = u'购物历史添加失败'
                return render_template('detail.html',buy=buy,history=history)

@app.route('/register/',methods=['GET','POST'])
def register():
    error = None
    if request.method == 'GET':
        return render_template('register.html',error=error)
    else:
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        #验证：手机号是否重复，密码是否不一致
        if telephone=='' or username=='' or password1=='' or password2=='':
            error = u'请将信息填写完整'
            return render_template('register.html',error=error)
        else:
            sql_exist = "select * from users where telephone='"+telephone+"'"
            # print sql_exist
            if cursor.execute(sql_exist):
                error = u'手机号码已经注册了'
                return render_template('register.html',error=error)
            else:#验证两个密码是否一致
                if password1 != password2:
                    error = u'密码不一致'
                    return render_template('register.html',error=error)
                else:
                    save_pass = hashlib.md5(password1).hexdigest()
                    register_sql = "INSERT INTO users(telephone,username,password,money) VALUES ('" + telephone+ "','"+username+ "','"+save_pass+"', 0);"
                    # print register_sql
                    r = cursor.execute(register_sql)
                    db.commit()
                    if r:
                        return redirect(url_for('login'))
                    else:
                        error = u'未知错误'
                        return render_template('register.html',error=error)

@app.route('/user/<tel>',methods=['POST','GET'])
def userinfo(tel):
    user_id = session.get('user_id')
    if user_id is None:
        return redirect(url_for('login'))
    else:
        if request.method == 'GET':
            return render_template('user.html')
        else:
            if request.form.get('kejin')==u'立即充值':
                # print request.form.get('money')
                yu_e = float(request.form.get('money'))+user.getmoney()
                # print yu_e
                moneysql = "UPDATE users SET money="+str(yu_e)+" WHERE telephone='"+user_id+"';"
                # print moneysql
                if cursor.execute(moneysql):
                    error = u"充值成功"
                    user.setmoney(yu_e)
                else:
                    error = u"未知错误"
                return render_template('user.html',error=error)
            if request.form.get('gaimi') == u'修改密码':
                if user.password != hashlib.md5(request.form.get('old')).hexdigest():
                    error = u'原密码错误'
                    return render_template('user.html', error=error)
                else:
                    if request.form.get('password1') != request.form.get('password2'):
                        error = u'密码不一致'
                        return render_template('user.html', error=error)
                    else:
                        savepass = hashlib.md5(request.form.get('password1')).hexdigest()
                        updatepasssql = "UPDATE users SET password='"+savepass+"' WHERE telephone='"+user_id+"';"
                        # print updatepasssql
                        if cursor.execute(updatepasssql):
                            error = u'密码修改成功'
                        else:
                            error = u'未知错误，修改失败'
                        return render_template('user.html',error=error)

@app.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.before_request
def my_before_request():
    user_id = session.get('user_id')
    if user_id:
        g.user = user

@app.context_processor
def my_context_processor():
    if hasattr(g,'user'):
        return {'user':g.user}
    return {}

@app.context_processor
def my_context_processor():
    if hasattr(g,'goods'):
        return {'goods':g.goods}
    return {}

if __name__ == '__main__':
    # init_db()
    # 想挂外网
    # app.run(host='0.0.0.0',port=5000)
    # 本地
    app.run()