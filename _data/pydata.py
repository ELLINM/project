import cx_Oracle
import crwalling
import postertest

title = crwalling.select_title
grade = crwalling.select_grade
director = crwalling.select_director
date = crwalling.select_date
actor1 = crwalling.select_actor1
actor2 = crwalling.select_actor2
actor3 = crwalling.select_actor3
country = crwalling.select_country
genre = crwalling.select_genre
time = crwalling.select_runningtime
actor = crwalling.select_actor
poster = postertest.src

conn = cx_Oracle.connect("hr/hr@localhost")
cursor = conn.cursor()

sql = "insert into cinepic_movie values (:mno, :title, :genre, :director, :actor, :poster)"
data = [1, title, genre, director, ','.join(actor), poster]
cursor.execute(sql, data)

conn.commit()
cursor.close()
conn.close()
