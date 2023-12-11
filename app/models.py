from django.db import models

# Create your models here.
class Dept(models.Model):
    Deptno=models.IntegerField(primary_key=True)
    Dname=models.CharField(max_length=100)
    loc=models.CharField(max_length=100)
    def __str__(self):
        return self.Dname
    
class Emp(models.Model):
    Empno=models.IntegerField()
    Ename=models.CharField(max_length=100)
    Job=models.IntegerField()
    Mgr=models.CharField(max_length=100)
    Hiredate=models.DateField()
    Sal=models.IntegerField()
    comm=models.IntegerField()
    Deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)
    def __str__(self):
        return self.Ename
    

    