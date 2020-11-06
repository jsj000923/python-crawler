import pymysql
def su(name):
    print('**************'+name+'*************')

def xt():
    su('欢迎来到学生管理系统')
    su('1.增加学生信息')
    su('2.修改学生信息')
    su('3.查询学生信息')
    su('4.删除学生信息')

def xg():
    print("1.修改姓名")
    print("2.修改性别")
    print("3.修改班级")
    print("4.修改全部")
    

db= pymysql.connect(host ='127.0.0.1', port=3306,  user = "root", password = "", db = "lx")
conn = db.cursor()
xt()
t = int(input("请输入你要操作的信息，输入序号即可"))
if(t == 1):
    name = input('请输入你的姓名')
    sex  = input('请输入你的性别')
    cla  = input('请输入你的班级') 
    sql = "insert into student(name,sex,class) values('{}','{}','{}')".format(name,sex,cla)
    conn.execute(sql)
    print("成功")
elif(t == 2):
    name = input("请输入你要修改的名字")
    xg()
    gd = int(input("请输入你要修改的编号"))
    if(gd == 1 ):
        name1 = input("你要修改后的名字")
        sql = "update student set name='{}' where name='{}' and is_delete!=1".format(name1,name)
        conn.execute(sql)
    elif(gd==2):
        sex   = input("你要修改后的性别")
        sql = "update student set sex='{}' where name='{}' and is_delete!=1".format(sex,name)
        conn.execute(sql)
    elif(gd==3):
        cla   = input("你要修改后的班级")
        sql = "update student set class='{}' where name='{}' and is_delete!=1".format(cla,name)
        conn.execute(sql)
    elif(gd==4):
        name1 = input("你要修改后的名字")
        sex   = input("你要修改后的性别")
        cla   = input("你要修改后的班级")   
        sql = "update student set name='{}',sex='{}',class='{}' where name='{}' and is_delete!=1".format(name1,sex,cla,name)
        conn.execute(sql)
elif(t == 3):
    name = input("请输入你要查询的名字")
    sql = "select name,sex,class from student where name='{}' and is_delete != 1".format(name)
    conn.execute(sql)
    jl = conn.fetchall()
    for i in jl:
        print(i[0],i[1],i[2])
elif(t == 4):
    name = input("请输入你要查询的名字")
    sql = "update student set is_delete = 1 where name='{}'".format(name)
    conn.execute(sql)