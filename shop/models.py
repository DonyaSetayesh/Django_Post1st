from django.db import models

class Food(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='نام غذا')
    price = models.IntegerField(verbose_name='قیمت غذا', 
                                )
    
    def __str__(self) -> str:
        return self.name

class Customer(models.Model):
    firstname = models.CharField(verbose_name='نام مشتری', max_length=200)
    lastname = models.CharField(max_length=200, verbose_name='نام خانوادگی')
    phone_number = models.CharField(max_length=11, verbose_name='شماره همراه')
    
    def __str__(self) -> str:
        return f'{self.firstname} {self.lastname}'




class Order(models.Model):
    food = models.ForeignKey(Food, on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    
    
class Person(models.Model):
    name = models.CharField(verbose_name="نام", max_length=100)
    last_name = models.CharField(verbose_name="نام خانوادگی", max_length=100)
    national_code = models.CharField(verbose_name="کد ملی", max_length=10)
    father_name = models.CharField(verbose_name="نام پدر", max_length=100)
    role = models.IntegerField(verbose_name="نقش")
    password_hash = models.CharField(verbose_name="رمز عبور", max_length=255)

class Student(models.Model):    
    registration_type = models.IntegerField(verbose_name="نوع ثبت نام")
    entry_semester = models.IntegerField(verbose_name="نیمسال تحصیلی ورود")
    department_major_level = models.IntegerField(verbose_name="دپارتمان_گرایش_مقطع")
    has_graduated = models.BooleanField(verbose_name="فارغ از تحصیل شده است؟")
    Person= models.ForeignKey(Person, on_delete=models.CASCADE)

class Email(models.Model):
    Email = models.CharField(verbose_name="ایمیل",max_length=200 )
    Person= models.ForeignKey(Person, on_delete=models.CASCADE)
class PostalAddress(models.Model):
    pomail = models.CharField(verbose_name="ایمیل",max_length=200 )
    Person= models.ForeignKey(Person, on_delete=models.CASCADE)
class PhoneNumber(models.Model):
    PhoneNumber = models.CharField(verbose_name="ایمیل",max_length=200 )
    Person= models.ForeignKey(Person, on_delete=models.CASCADE)