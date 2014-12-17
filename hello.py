#coding=utf-8 
from flask import Flask, url_for, render_template,request, Markup
import sqlite3
import os
import sys
reload(sys)
import random

sys.setdefaultencoding('utf-8')

app = Flask(__name__)


app.config.from_object(__name__)



#测试路由
@app.route('/hh')
def hh():
	haha = ''
	return render_template("pic_pc.html")

@app.route('/')
def turn():
	return render_template("turn.html")
@app.route('/index/')
@app.route('/index')
def index():

	try:
		paper = 1
		i = 0
		dict = []
		conn = sqlite3.connect('my.db')
		cursor = conn.cursor()
		sql = 'select no,title,content,img,year,month,day from article;'
		rs = cursor.execute(sql).fetchall()
		if len(rs)%5 == 0:
			artlen = len(rs)/5
		else:
			artlen = len(rs)/5 + 1
		for r in rs[::-1]:
			image = '/static/img/article/'
			if i >= 5:
				break
			i += 1
			if r[3] == '':
				if(len(r[2]) >=500):
					dict.append({'title':r[1],'content':r[2][:500],'article_id':r[0],'date':r[4]+'.'+r[5]+'.'+r[6]})
				else:
					dict.append({'title':r[1],'content':r[2],'article_id':r[0],'date':r[4]+'.'+r[5]+'.'+r[6]})
			else:
				image = image + r[3] + '.jpg'
				dict.append({'title':r[1],'content':r[2][:100],'image':image,'article_id':r[0],'date':r[4]+'.'+r[5]+'.'+r[6]})
		cursor.close()
		conn.close()
	except:
		print 'db is wrong'
	return render_template("index.html",dict=dict,paper=1,artlen=artlen)

@app.route('/index/next/<int:paper>')
def paper(paper):
	try:
		i = 0
		dict = []
		
		conn = sqlite3.connect('my.db')
		cursor = conn.cursor()
		sql = 'select no,title,content,img,year,month,day from article;'
		rs = cursor.execute(sql).fetchall()
		if len(rs)%5 == 0:
			artlen = len(rs)/5
		else:
			artlen = len(rs)/5 + 1
		if paper >= artlen:
			paper = artlen-1
		for r in rs[len(rs)-5*(paper)-1::-1]:
			image = '/static/img/article/'
			if i >= 5:
				break
			i += 1
			if r[3] == '':
				if(len(r[2]) >=700):
					dict.append({'title':r[1],'content':r[2][:700],'article_id':r[0],'date':r[4]+'.'+r[5]+'.'+r[6]})
				else:
					dict.append({'title':r[1],'content':r[2],'article_id':r[0],'date':r[4]+'.'+r[5]+'.'+r[6]})
			else:
				image = image + r[3] + '.jpg'
				dict.append({'title':r[1],'content':r[2][:100],'image':image,'article_id':r[0],'date':r[4]+'.'+r[5]+'.'+r[6]})
		cursor.close()
		conn.close()
		if paper == artlen:
			paper = paper
		else:
			paper += 1
	except:
		print 'db is wrong'
	return render_template("index.html",dict=dict,paper=paper,artlen=artlen)

@app.route('/index/last/<int:paper>')
def paperlast(paper):
	try:
		i = 0
		dict = []
		image = '/static/img/article/'
		conn = sqlite3.connect('my.db')
		cursor = conn.cursor()
		sql = 'select title,content,img,year,month,day from article;'
		rs = cursor.execute(sql).fetchall()
		if len(rs)%5 == 0:
			artlen = len(rs)/5
		else:
			artlen = len(rs)/5 + 1
		if paper > artlen:
			paper = artlen 
		for r in rs[len(rs)-(paper-2)*3-1::-1]:
			image = '/static/img/article/'
			if i >= 5:
				break
			i += 1
			if r[3] == '':
				if(len(r[2]) >=1700):
					dict.append({'title':r[1],'content':r[2][:500],'article_id':r[0],'date':r[4]+'.'+r[5]+'.'+r[6]})
				else:
					dict.append({'title':r[1],'content':r[2],'article_id':r[0],'date':r[4]+'.'+r[5]+'.'+r[6]})
			else:
				image = image + r[3] + '.jpg'
				dict.append({'title':r[1],'content':r[2][:100],'image':image,'article_id':r[0],'date':r[4]+'.'+r[5]+'.'+r[6]})
		cursor.close()
		conn.close()
		paper -= 1
	except:
		print 'db is wrong'
	return render_template("index.html",dict=dict,paper=paper,artlen=artlen)

@app.route('/test_mobile')
def test_mobile():
	return render_template("test_mobile.html")

@app.route('/article/<int:article_id>')
@app.route('/index/article/<int:article_id>')
def article(article_id):
	conn = sqlite3.connect('my.db')
	cursor = conn.cursor()
	sql = 'select title,content,img,year,month,day from article where no = ?;'
	rs = cursor.execute(sql,(article_id,)).fetchone()
	title = ''
	title = title + rs[0]
	content = rs[1]
	date = rs[3]+'.'+rs[4]+'.'+rs[5]
	img = rs[2]
	cursor.close()
	conn.close()
	return render_template("article.html",title=title,content=content,date=date,img=img)


@app.route('/article/edit',methods=['GET', 'POST'])
def edit():
	return render_template("edit.html")

@app.route('/add_article')
def add_article():
	pass

@app.route('/img/<string:pla>')
def img(pla):
	if pla == 'pc':
		img_css = []
		toplast = 0
		leftlast = 0
		left = '30'
		top = '0'
		i = 0
		conn = sqlite3.connect('my.db')
		cursor = conn.cursor()
		sql = 'select name,file,type from img;'
		rs = cursor.execute(sql).fetchall()
		for r in rs:
			cssid = r[0]
			fname = r[1]
			tname = r[2]
			
			istop = random.randint(0,1)
			ran = random.randint(20,80)
			'''
			top = str(toplast+ran)
			
			while abs(int(top)-toplast) < 50:
				top = str(random.randint(20,300))
				i = i + 1
				if i ==10:
					i = 0
					break
					'''
			if int(leftlast) > 900:
				leftlast = 0
				top = str(toplast+250)
				toplast = int(top)
				i = 0
				left = '30'
			#ran = random.randint(20,100)
			if i != 0:
				left = str(leftlast+random.randint(180,220))
			'''
			while abs(int(left)-leftlast) < 50:
				left = str(random.randint(20,300))
				i = i + 1
				if i ==10:
					i = 0
					break
					'''
			leftlast = int(left)
			deg = str(random.randint(-20,20))
			number = cssid
			css = '.pic'+number+' {top: '+top+'px; left: '+left+'px; -webkit-transform:rotate('+deg+'deg);-moz-transform: rotate('+deg+'deg); transform: rotate('+deg+'deg);max-width:300px;max-height:300px;}'
			image='<img src="\static/img/'+fname+'/'+number+'.'+tname+'" class="pic'+number+' ">'
			img_css.append({'image':image,'css':css})
			i=i+1
		cursor.close()
		conn.close()
		return render_template("img_pc.html",img_css=img_css)
	else:
		return render_template("img_mobile.html")


@app.route('/article_list')
def article_list():
	month_list = [0 for x in range(12)]
	year_list = [0 for x in range(10)]
	left_list = []
	left = []
	year_no = []
	year = 0
	flag = 1
	conn = sqlite3.connect('my.db')
	cursor = conn.cursor()
	sqll = "select year from article order by year desc;"
	sqly = "select year from article order by year;"
	sql = "select title,content,year,month,no,day from article where month=? and year =?;"
	firsty = cursor.execute(sqly).fetchone()
	lasty = cursor.execute(sqll).fetchone()
	firstyear = int(firsty[0])
	lastyear = int(lasty[0])+1
	for y in range(firstyear,lastyear):
		for m in range(1,13):
			rs = cursor.execute(sql,(m,y,)).fetchall()
		#	for i in range(len(rs)):
		#		left.append(leftlen+=100)
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
	return render_template("article_list.html",year_list=year_list,year_no=year_no,firstyear=firstyear)

@app.route('/introduce')
def introduce():
	return render_template("introduce.html")



if __name__ == '__main__':
	app.debug = True
	#app.run(host='0.0.0.0')
	app.run();