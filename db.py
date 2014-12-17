#coding=utf-8 
import sqlite3
import os
import random

def db():
		conn = sqlite3.connect('my.db')
		cursor = conn.cursor()
		sql = 'select * from article;'
		rs = cursor.execute(sql).fetchall()
		print len(rs)
		print rs
		print rs[0][2]
		ret = {}
		title = ' '
		title = rs[0][1]
		ret.update({'title':title})
		print ret
		#for r in rs:
		#	print r
		#	print type(r)
		cursor.close()
		conn.close()

def db2():
		dict = []

		conn = sqlite3.connect('my.db')
		cursor = conn.cursor()
		sql = 'select * from article;'
		rs = cursor.execute(sql).fetchall()
		print rs
		total = len(rs)
		for r in rs:
			print r
			if(r[1] == ''):
				print 'title is empty'
			dict.append({'title':r[1],'content':r[2]})
		print dict
		i = 0
		cursor.close()
		conn.close()

def db_insert():
		filename = '1.txt'
		conn = sqlite3.connect('my.db')
		cursor = conn.cursor()
		string = open(filename,'r').read()
		sql = "insert into article values(10,'test',?,'')"
		cursor.execute(sql,(string,))
		#注意这里最后要有逗号你妹的！！
		conn.commit()
		cursor.close()
		conn.close()
		print len(string)
		print 'success'
		
def hhh():
	article_id = 1
	conn = sqlite3.connect('my.db')
	cursor = conn.cursor()
	sql = 'select title,content from article where no = ?;'
	rs = cursor.execute(sql,(article_id,)).fetchone()
	
	print rs

def string():
	str = '为我们这么吊'
	print len(str)
	print str[:3]

def css():
	img_css = []
	top = '0'
	left = '0'
	for cssid in range(1,5):
			istop = random.randint(0,1)
			if istop==0:
				ran = random.randint(20,700)
				top = str(ran)
			else:
				ran = random.randint(20,600)
				left = str(ran)
			deg = str(random.randint(-20,20))
			number = str(cssid)
			print deg
			print top
			print left
			css = '.pic'+number+' {top: '+top+'px; left: '+left+'px; -webkit-transform:rotate('+deg+'deg);-moz-transform: rotate('+deg+'deg); transform: rotate('+deg+'deg);}'
			image='<img src="\static/images/mm'+number+'.jpg" class="pic'+number+'">'
			img_css.append({'image':image,'css':css})

def rd(x):
	#a = random.randint(10,20)
	a = 11
	for r in x:
		if abs(a-r) < 2:
			a = random.randint(10,20)
			a = rd(x)
		print a
		return a
	print a

def article_list():
	month_list = [0 for x in range(12)]
	year_list = [0 for x in range(10)]
	year_no = []
	year = 0
	flag = 1
	conn = sqlite3.connect('my.db')
	cursor = conn.cursor()
	sqly = "select year from article order by year;"
	sql = "select title,content,year,month,no,day from article where month=? and year =?;"
	firsty = cursor.execute(sqly).fetchone()
	firstyear = int(firsty[0])
	for y in range(firstyear,firstyear+10):
		for m in range(1,13):
			rs = cursor.execute(sql,(m,y,)).fetchall()
			month_list[m-1] = rs
			if rs != [] and flag==1:
				flag = 0
				year_no.append(y)
		flag = 1
		year_list[year] = month_list
		month_list = [0 for x in range(12)]
		year += 1
	cursor.close()
	conn.close()
	print year_list
	


if __name__ == '__main__':
	article_list();