# -*- coding: utf-8 -*-
from mydb import TornaDB
from tornado.options import options
db = TornaDB.Connection(host='127.0.0.1',port='3306',database='blog',user='root',password='root')
def getArticle(url):
    sql = ("SELECT a.aid,a.url,a.title,a.content,a.created,a.allowComment FROM article a WHERE url=%(url)s LIMIT 1")
    db.cursor.execute(sql,{ 'url': url })
    return db.cursor.fetchone()
def addArticle(title,content,url):
    sql = "INSERT INTO article (url, title, content, created) VALUES( %s, %s, %s, CURRENT_TIMESTAMP() ) "
    data = (url,title,content)
    db.cursor.execute(sql,data)

def findUserNameReturnPassWord(username):
    sql = "SELECT * FROM user WHERE username = %(username)s LIMIT 1 "
    db.cursor.execute(sql,{'username':username})
    return db.cursor.fetchone()
def getComments(aid):
    sql = "SELECT author,content,created FROM comments WHERE aid = %(aid)s AND status='public' ORDER BY cid DESC"
    db.cursor.execute(sql,{'aid':aid})
    return db.cursor.fetchall()

def addComment(data):
    sql = "INSERT INTO comments (aid, author,email,url,content,created) VALUES( %s, %s, %s, %s, %s, CURRENT_TIMESTAMP() ) "
    db.cursor.execute(sql,data)