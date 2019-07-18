"""
save_image.py
二进制文件存储演示
"""

import  pymysql

# 连接数据库
db = pymysql.connect(host='localhost',
                     port = 3306,
                     user = 'root',
                     password = '123456',
                     database = 'stu',
                     charset = 'utf8')

# 获取游标 （操作数据库，执行sql语句）
cur = db.cursor()

# 存储图片
# with open('image.jpg','rb') as f:
#     data = f.read()
# try:
#     sql = "update class_1 set image = %s \
#     where name='Jame';"
#     cur.execute(sql,[data])
#     db.commit()
# except Exception as e:
#     db.rollback()
#     print(e)

# 获取图片
sql = "select image from class_1 \
where name='Jame'"
cur.execute(sql)
data = cur.fetchone()
with open('girl.jpg','wb') as f:
    f.write(data[0])


# 关闭数据库
cur.close()
db.close()