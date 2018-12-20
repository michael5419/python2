from django.db import models

#自定義BookManager類，用於覆蓋實體類中objects
class BookManager(models.Manager):
  def title_count(self,keywords):
    return self.filter(title__contains=keywords).count()

class AuthorManager(models.Manager):
  def age_lt(self,age):
    return self.filter(age__lt=age)

class Publisher(models.Model):
  name = models.CharField(max_length=30)
  address = models.CharField(max_length=200)
  city = models.CharField(max_length=50)
  country = models.CharField(max_length=50)
  website = models.URLField()

  def __str__(self):
    return self.name
#创建　Author 的实体类
#1.name - 姓名(CharField -> varchar)
#2.age - 年龄(IntegerField -> int)
#3.email - 电子邮件(EmailField -> varchar)
class Author(models.Model):
  #使用AuthorManager對象覆蓋本類中objects
  objects = AuthorManager()
  name = models.CharField(max_length=30,verbose_name='姓名')
  age = models.IntegerField(verbose_name='年齡')
  email = models.EmailField(null=True,verbose_name='郵件')
  isActive = models.BooleanField(default=True,verbose_name='激活用戶')
  #增加一的字段，表示用戶頭像，可以上傳
  picture = models.ImageField(upload_to="static/upload",null=True,verbose_name='頭像')
  def __str__(self):
    return self.name

  #增加內部類Meta來定義展現方式
  class Meta:
    db_table = 'author'
    verbose_name = '作者'
    verbose_name_plural = verbose_name
    ordering = ['-age']

  def __repr__(self):
    return "<Author:%r>" % self.name

class Book(models.Model):
  objects = BookManager()
  title = models.CharField(max_length=50)
  publicate_date = models.DateField()
  publisher = models.ForeignKey(Publisher,null=True)
  authors = models.ManyToManyField(Author)

  def __str__(self):
    return self.title

class Wife(models.Model):
  name = models.CharField(max_length=30,verbose_name='姓名')
  age = models.IntegerField(verbose_name='年齡')
  author = models.OneToOneField(Author,verbose_name='配偶')

  def __str__(self):
    return self.name



