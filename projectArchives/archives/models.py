from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class level(models.Model):
    name = models.CharField(max_length=30)
    date_created = models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = "Level"
class Department(models.Model):
    dept_id = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=10)
    
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = "Department"
        
    
class Student(models.Model):
    GENDER = (('Male','Male'),('Female','Female'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(choices=GENDER, max_length=20)
    regNo =  models.CharField(unique=True,max_length=14)
    NTA_Level = models.CharField(max_length=2,null=True,blank=True)
    department = models.ForeignKey(Department,null=True,on_delete=models.CASCADE)
    academic_year = models.CharField(max_length=12)
    mobile = models.CharField(max_length=14, null=True,blank=True)
    photo = models.ImageField(upload_to='profile_pic',default='default.jpg', null=True, blank=True)
    
    
    def __str__(self):
        return self.regNo

    class Meta:
        db_table = "Student"
        

class Staff(models.Model):
    GENDER = (('Male','Male'),('Female','Female'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(choices=GENDER, max_length=20)
    staff_id =  models.IntegerField(unique=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    mobile = models.TextField(max_length=14, null=True,blank=True)
    photo = models.ImageField(upload_to='profile_pic/staff',default='default.jpg', null=True, blank=True)

    
    
    def __str__(self):
        return self.staff_id

    class Meta:
        db_table = "Staff"
        
        
class Project_type(models.Model):
    name = models.CharField(max_length=30)
    date_created = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.staff_id

    class Meta:
        db_table = "project_type"
        
class Project(models.Model):
    title = models.CharField
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    project_type = models.ForeignKey(Project_type,on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='cover', null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title

    class Meta:
        db_table = "project"



class Document(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    file = models.FileField(upload_to='projects')
    date_created = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.file

    class Meta:
        db_table = "document"       

class progress(models.Model):
    project = models.ForeignKey(Document,on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff,on_delete=models.CASCADE)
    progress = models.CharField(max_length=10)
    comments = models.TextField(max_length=100)
    date_created = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.progress

    class Meta:
        db_table = "progress"  