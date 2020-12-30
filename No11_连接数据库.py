import mysql.connector
host = "localhost"
user = "root"
password = "123456"
database="test"
mydb = mysql.connector.connect(host = host, user = user, password = password, database = database)
mycursor = mydb.cursor()
str = """SELECT s.name AS 姓名, 
			CASE s.sex 
				WHEN 1 THEN "男"
				WHEN 2 THEN "女"
				WHEN 0 THEN "未知"
			END AS 性别, 
			s.age AS 年龄, 
			group_concat(k.km separator '/') AS 科目
            FROM student s
            JOIN (SELECT * FROM student_kemu s JOIN kemu k ON s.kemuid = k.id) k ON s.id = k.studentid
            GROUP BY s.name, s.sex, s.age"""
mycursor.execute(str)
for i in mycursor:
    print(i)