from django.db.models import Avg, Sum, F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from .models import *

#http://localhost:8000/05-add
def add_views(request):
  # 方案１：Entry.objects.create()
  obj = Author.objects.create(name='Mike',age=32,email='wang.wc@gmail.com')
  print(obj.id,obj.name,obj.age,obj.email)

  # 方案２: obj.save()
  obj = Author(name='Lin',age=35,email='laowang@gmail.com')
  obj.save()

  # 方案３：obj.save()
  dic = {
    'name':'Chen',
    'age' : 39,
    'email' : 'brother@gmail.com',
    'isActive' : False
  }
  obj = Author(**dic)
  obj.save()
  print(obj.id, obj.name, obj.age, obj.email,obj.isActive)

  #向Publisher表中增加數據
  Publisher.objects.create(name='中南出版社',address='民族東路125號',city='台北市',country='台灣',website='http://www.central.com')
  #
  obj = Publisher(name='天龍出版社',address='重慶南路100號',city='台北市',country='台灣',website='http://www.sky.com')
  obj.save()
  #
  dic = {
    'name':'三名書局',
    'address':'重慶南路200號',
    'city':'台北市',
    'country':'台灣',
    'website':'http://www.three.com'
  }
  obj1 = Publisher(**dic)
  obj1.save()

  #在Book表中插入數據
  Book.objects.create(title='python榮耀歸來',publicate_date='2015-10-12')

  book = Book(title='python人工智能',publicate_date='2017-09-12')
  book.save()

  dic = {
    'title':'python聖經',
    'publicate_date':'2018-01-01'
  }
  book1 = Book(**dic)
  book1.save()


  return HttpResponse("Add OK")

def query_views(request):
  #排序
  authors = Author.objects.order_by('-id')
  for au in authors:
    print(au.id,au.name,au.age,au.email)
  return HttpResponse("Query OK")


def queryall_views(request):
  #查詢isActive的值為True表示未被刪除的數據
  authors = Author.objects.filter(isActive=True)
  return render(request,'07-queryall.html',locals())

def update_views(request,id):
  author = Author.objects.get(id=id)
  return render(request,'08-update.html',locals())

def update09_views(request):
  #修改isActive為False數據，將isActive更改為True
  Author.objects.filter(isActive=False).update(isActive=True)
  return HttpResponse('Update Success')

def delete_views(request,id):
  author = Author.objects.get(id=id)
  #通過isActive=False模擬刪除
  author.isActive = False
  author.save()
  #使用重定向定位到/07-queryall顯示所有表格數據
  return redirect('/07-queryall')


def doF_views(request):
  Author.objects.all().update(age=F('age')+10)
  return redirect('/07-queryall')

def raw_views(request):
  sql = "select * from index_author where age>45"
  authors = Author.objects.raw(sql)
  for au in authors:
    print(au.name,au.age,au.email)
  return HttpResponse("Query OK")

def authors_views(request):
  authors = Author.objects.all()
  return render(request,'13-authors.html',locals())

def oto_views(request):
  # wife = Wife()
  # wife.name = 'Mike夫人'
  # wife.age = 26
  # wife.author_id = 1
  # wife.save()

  # wife = Wife()
  # wife.name = "Lin夫人"
  # wife.age = 18
  # author = Author.objects.get(name='Lin')
  # wife.author = author
  # wife.save()

  #正向查循
  wife = Wife.objects.get(id=1)
  wife_author = wife.author
  #反向查詢
  author = Author.objects.get(id=1)
  author_wife = author.wife
  return render(request,'14-oto.html',locals())


def otm_views(request):
  # 正向查循:通過Book查詢Publisher,在15-otm.html中顯示每個book對應的publisher
  books = Book.objects.all()
  # 反向查詢
  pub = Publisher.objects.get(id=1)
  pub_books = pub.book_set.all()
  return render(request,'15-otm.html',locals())

def mtm_views(request):
  #正向查循：通過book查詢authors
  book = Book.objects.get(id=1)
  authors = book.authors.all()
  #反向查詢：通過author查詢book
  author = Author.objects.get(id=2)
  books = author.book_set.all()
  return render(request,'16-mtm.html',locals())

def titleCount_views(request):
  # count = Book.objects.title_count('Mike')
  # return HttpResponse('包含Mike書籍數量為%d' % count)
  authors = Author.objects.age_lt(45)
  for author in authors:
    print(author.name,author.age)
  return HttpResponse("Query OK")
