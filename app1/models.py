from django.db import models

# Create your models here.
# ORM --- object Relational Mapper

# class ActivePersons(models.Manager):#.....custom model manager
#     def get_queryset(self):
#         return super().get_queryset().filter(is_active=True)#...model.objects.all

# class ActivePersons(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(is_active=False)#.....for in active data

# class Person(models.Model):
#     name = models.CharField(max_length = 200)
#     age = models.IntegerField()
#     mobile_no = models.IntegerField()
#     address = models.CharField(max_length = 100)
#     email = models.EmailField(null = True)
#     data_joined = models.DateTimeField(auto_now = True, null = True)#...imp.....automatically time is add according to system
#     data_updated = models.DateTimeField(auto_now_add = True, null = True)#...imp
#     is_active = models.BooleanField(default = True)#...imp
#     activep = ActivePersons()#.......it will give active data only
#     objects = models.Manager#......it will give all data....both are manager
#     inactivep = ActivePersons()#....for inactive person



#     def __str__(self):
#         return f"{self.name} -- {self.address}"

#     def show_details(self):
#         print(f"""Person Name:- {self.name}
#     Person Age:- {self.age}
#     Person Mobile_no :-{self.mobile_no}
#     Person Address :- {self.address}   
#     """)

    

#     @classmethod
#     def get_data_above_age(cls):
#         return cls.objects.filter(age__gte = 25)#.....gt....greater than....gte....greater than all equals to....lt, lts, startswith, endswith

#     @classmethod
#     def get_avg(cls):
#         data = Person.objects.all().values("id", "name", "age")
#         lst = list(map(lambda x: x["age"], list(data)))
#         data = Person.objects.all().values("id", "name", "age")
#         print(sum(lst)//len(lst))

#     @classmethod
#     def get_active_data(cls):
#         return cls.objects.filter(is_active = False )#....actice

#     @classmethod
#     def get_in_active_data(cls):
#         return cls.objects.filter(is_active = False)

# startproject, startapp, runserver, makemigrations



class CommonClass(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True#.....table create and query hit nhi honi chaiye common class ki isliye abstract = true defined kiya hai


class College(CommonClass):
    adr = models.CharField(max_length = 100)
    est_date = models.DateField(auto_now=True)
    class Meta:
        db_table = "College"

class Principle(CommonClass):
    exp = models.FloatField()
    qulifi = models.CharField(max_length = 100)
    college = models.OneToOneField(College, on_delete = models.CASCADE, related_name = "principle")
    class Meta:
        db_table = "principle"

class Department(CommonClass):
    dept_str = models.IntegerField()
    college = models.ForeignKey(College, on_delete = models.CASCADE, related_name = "dept")#.....foreignkey = onetomanyfield
    class Meta:
        db_table = "dept"

class Student(CommonClass):
    marks = models.IntegerField()
    age = models.IntegerField()
    department = models.ForeignKey(Department, on_delete = models.CASCADE, related_name = "studs")#.....foreignkey = onetomanyfield
    class Meta:
        db_table = "student"

class Subjects(CommonClass):
    is_practical = models.BooleanField(default=False)
    student = models.ManyToManyField(Student)
    dept = models.ForeignKey(Department, on_delete = models.CASCADE, related_name = "subjects")
    class Meta:
        db_table = "subjects"


# ERD-- Entity Relational Diagram
# get models from database


# 2 example--many to many 

class FuelType(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

class Carmodel(models.Model):
    name = models.CharField(max_length = 255)
    fueltype = models.ManyToManyField(FuelType, related_name = 'carmodels')

    def __str__(self):
        return self.name



