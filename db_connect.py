from database.db_helper import DBHelper

# DBHelper().db_select('select * from object')


# 插入语句
# sql1 = 'insert into object(id,english,chinese,math) values (5,\'20\',\'41\',\'99\')'
# DBHelper().db_execute(sql1)

DBHelper().db_select('select * from user where username = \'blues\'')
