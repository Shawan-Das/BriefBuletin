# import json
# , datetime
import mysql.connector
def save(news, topic):



    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="newsportal"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO tblposts ( postTitle, categoryID, postDetails, postUrl, postImage ) VALUES (%s, %s, %s, %s,%s)"
    val = (news["title"], topic, news['summary'], news['link'], news['img'])
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
# save('https://www.bbc.com/news/av/world-europe-63318579',1)