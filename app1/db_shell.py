# exec(open(r'F:\code files\B8_django_web\first_project\app1\db_shell.py').read())

from app1.models import *

# to get all data
# obj = Person.objects.all()
# print(list(obj))#....query set in list

# for Person in obj:
#     print(Person)#.....person name and address
#     print(Person.__dict__)#....get dict name, age, mobilr no, address



# to get first data

# first_data = Person.objects.first()
# print(first_data)


# to get data by id

# obj = Person.objects.get(id = 1)#....single record
# print(obj)


# to get data by id

# try:
#     obj = Person.objects.get(id = 5)
# except Person.DoesNotExist:
#     print("Record does not exist")



# to get multiple data by passing filename

# obj = Person.objects.filter(age = 23)
# print(obj)


# to check query

# obj = Person.objects.all()#..SELECT "app1_person"."id", "app1_person"."name", "app1_person"."age", "app1_person"."mobile_no", "app1_person"."address" FROM "app1_person"
# print(obj.query)


# obj = Person.objects.filter(age = 30, address = "pune")#.....  , is called as "and"
# print(obj.query)


# modify existing data

# p1 = Person.objects.get(id = 1)
# print(p1.__dict__)
# p1.mobile_no = 9217368740
# print(p1.__dict__)
# p1.save()#....to save changes in database


# to delete data
# p1 = Person.objects.get(id = 5)# delete 5 no of data
# p1.delete()


# save method-- 1st way

# p1 = Person(name = "komal", age = 24, mobile_no = 7421546812, address = "Nanded") 
# p1.save()


# 2nd way--

# Person.objects.create(name = "saurabh", age = 27, mobile_no = 7421756812, address = "Mumbai")#....here we don't need p1.save()


# bulk_create

# p1 = Person(name = "surekha", age = 46, mobile_no = 11, address = "chennai")
# p2 = Person(name = "Ishwar", age = 54, mobile_no = 22, address = "Thane")
# p3 = Person(name = "Harshad", age = 28, mobile_no = 33, address = "Goa")
# p4 = Person(name = "yogita", age = 33, mobile_no = 44, address = "Delhi")

# Person.objects.bulk_create([p1, p2, p3, p4])


# count--

# print(Person.objects.count())


# to delete all data

# Person.objects.all().delete()


# to delete multiple data-
# Person.objects.filter(age = 25).delete()


# istartwith--

# print(Person.objects.filter(name__istartswith = "s"))

# endswith--

# print(Person.objects.filter(name__endswith = "s"))

# exclude--
# print(Person.objects.exclude(name__startswith = "a"))


# exixts--

# print(Person.objects.filter(name = "poonam").exists())

# order_by--

# print(Person.objects.all().order_by("name"))#.....we can fetch data from id, name and -id in decs

# Person.objects.get(id = 1).show_details()#....to fetch single record from model.py file


# for per_obj in Person.objects.all():#....to fetch multiple data from model.py file
#     per_obj.show_details()


# print(Person.get_data_above_age())


from django.contrib.auth import get_user_model
# user = get_user_model()



# video no 103--

# data = Person.objects.all().values("id", "name", "age")#....list of dict
# print(data)


# data = Person.objects.all().values("id", "name", "age")
# for i in data:
#     print(i)


# data = Person.objects.all().values("id", "name", "age")
# name_list = []
# for i in data:
#     name_list.append(i["name"])#.....fetch name from database
# print(name_list)


# data = Person.objects.all().values("id", "name", "age")
# age_list = []
# for i in data:
#     age_list.append(i["age"])# age
# print(age_list)


# data = Person.objects.all().values("id", "name", "age")
# lst = list(map(lambda x: x["age"], list(data)))#....fetch age with the used of map and lambda
# print(lst)
# print(sum(lst)//len(lst))


# data = Person.objects.all().values_list("name")#....list of tuple
# print(list(data))


# database change to mysql
# from django.contrib.auth.models import User
# User.objects.create_user(username = "poonam", password = "python@123")#...always use create_user

# data = Person.objects.filter(id_in = [3, 5])
# print(data)
# for i in data:
#     i.is_active = False
#     i.save()


# print(Person.objects.filter(is_active = True))

# print(Person.get_active_data())#.....for this we have to do ctrl z  kara lagel baher yenya sathi...then shell open then path execute

# print(Person.get_in_active_data())

# data = Person.objects.filter(id__in = [3, 5]).update(is_active=False)
# print(data)


# print(Person.objects.filter(is_active=True))

# print(Person.objects.filter(is_active=False))

# print(Person.activep.all())

# print(Person.activep.create())#........for delete, update, create we have to use activep as manager.....not objects as a manager....it will give active person

# print(Person.inactivep.create())#.....it will give inactive person



# Video no 105--
# exec(open(r'F:\code files\B8_django_web\first_project\app1\db_shell.py').read())

# clgs = College.objects.all()
# prns = Principle.objects.all()
# depts = Department.objects.all()
# studs = Student.objects.all()
# subjs = Subjects.objects.all()

# print(clgs)
# print(prns)
# print(depts)
# print(studs)
# print(subjs)
# for this we have to hit commond shell and then execute path


# for fetching department--

# depts = Department.objects.all()
# for i in depts:
#     print(i)
# for this we have to hit commond shell and then execute path


# depts = Department.objects.all()
# for i in depts:
#     print(i.__dict__)#.....get dict of depts


# clgs = College.objects.all()
# for i in clgs:
#     print(i.__dict__)


# prns = Principle.objects.all()
# for i in prns:
#     print(i.__dict__)


# studs = Student.objects.all()
# for i in studs:
#     print(i.__dict__)


# subjs = Subjects.objects.all()
# for i in subjs:
#     print(i.__dict__)


# fetch principle from college--

# clgs = College.objects.all()
# clg = clgs[0]
# print(clg.principle)#.......here p of principle is small......one to one


# fetch college from principle---

# prns = Principle.objects.first()
# print(prns.college)#....one to one


# fetch department from clg

# clgs = College.objects.all()
# clg = clgs[0]
# print(clg.department_set.all())#....d small....this is one to many


# fetch college from dept---

# depts = Department.objects.first()
# print(depts.college)#........many to one


# fetch student from dept---

# depts = Department.objects.first()
# print(depts.student_set.all())#......one to many


# depts = Department.objects.get(id = 2)#.....we can fetch like this also
# print(depts.student_set.all())#......one to many


# get all stud department wise--

# all_depts = Department.objects.all()
# for i in all_depts:
#     print(f"Department name:-{i.name}, studs:- {list(i.student_set.all())}")



# all_depts = Department.objects.all()
# d = {}
# for i in all_depts:
#     d[i.name] = list(i.student_set.all()) 
# print(d)#..........it will give in dict formate



# s1 = Student.objects.get(id = 1)
# print(s1.i)


# studs = Student.objects.all()
# stud_dept_dict = {}
# for i in studs:
#     stud_dept_dict[i.name] = i.department
# print(stud_dept_dict)


# studs = Student.objects.all()
# stud_dept_dict = {}
# for i in studs:
#     stud_dept_dict[i.name] = i.department.name
# print(stud_dept_dict)



# clg = College.objects.get(id = 1)#.........here we dont neet to do set.all()...bz we dedined related_name in models.py file
# print(clg.principle)


# clg = College.objects.get(id = 1)
# print(clg.dept.all())


# dept = Department.objects.get(id = 2)
# print(dept)
# print(dept.subjs.all())


# dept = Department.objects.all()
# for i in dept:
#     print(dept.Subjs.all())


# print([list(i.Subjects.all()) for i in Department.objects.all()])

# clg = College.objects.get(id = 1)
# print(clg)

# clg = College.objects.get(id = 1)
# print(clg.dept.all()[1].studs.all()[0])#....get single stud by [0].....practice for all department ...we have to do [2], [3]...in place of [1]



# clg = College.objects.get(id = 1)
# all_dept = clg.dept.all()
# for i in all_dept:
#     print(i.studs.all())#...get all students



# clg = College.objects.get(id = 1)
# for i in clg.dept.all():
#     print(i.studs.all())#.....get all students


# clg = College.objects.get(id = 1)
# stud_list = []
# for i in clg.dept.all():
#     stud_list.append(i.studs.all())

# print(stud_list)#....get all students in one list


# clg = College.objects.get(id = 1)
# stud_list = []
# for i in clg.dept.all():
#     stud_list.extend(i.studs.all())#......one one single elems go to list

# print(stud_list)


# stud_list = []
# for i in College.objects.get(id = 1):
#     stud_list.extend(i.studs.all())#.......same o/p as above.....this is shortcut


# s1 = Student.objects.get(id = 1)
# print(s1.dept.College.est_date)


# Addition

# College.objects.create(name = "MIT", adr = "kothrud")

# c1 = College.objects.get(id = 3)
# p1 = Principle(name = "xyz", exp = 15, qulifi = "phd", college = c1)#....as it is pass object of college c1
# p1.save()


# p1 = Principle(name = "xyz", exp = 15, qulifi = "phd", college_id = 3)#....pass clg id
# p1.save()



# Department.objects.create(name = "Production", dept_str = 45, college = c1)#.....college instance(college) ya college id(college_id).....make sure that college id is present in table


# Student.objects.create(name = "Anu", marks = 65, age = 21)
# Student.objects.create(name = "kiya", marks = 75, age = 23)
# Student.objects.create(name = "komu", marks = 85, age = 25)

# s1, s2, s3 = Student.objects.filter(id__gt = 9)
# print(s1)

# prod_dept = Department.objects.get(id = 4)


# prod_dept.studs.add(s1, s2, s3)#....one to many ---add students in department



# video no 106--

#prod_dept.studs.remove().....causes error


# studs = Student.objects.all()[0]
# print(studs)


# select related--

# studs = Student.objects.all()
# print(studs)
# for i in studs:
#     print(i.marks ,i.age , i.department)



# studs = Student.objects.select_related("department")
# for i in studs:
#     print(i.department)




# generate orm query for student and subject ---many to many relationship ...task


#... to create carmodel in database--

# c180 = Carmodel.objects.create(name = "C180")
# c200 = Carmodel.objects.create(name = "C200")
# print(Carmodel.objects.all())


#....to create fuel type in db--
# gas = FuelType.objects.create(name = "Gas")
# diseal = FuelType.objects.create(name = "Diseal")
# hybrid = FuelType.objects.create(name = "Hybrid")
# print(FuelType.objects.all())


#....to fetch data from db--
# c180 = Carmodel.objects.get(name = "C180")
# c200 = Carmodel.objects.get(name = "C200")

gas = FuelType.objects.get(name = "Gas")
diseal = FuelType.objects.get(name = "Diseal")
hybrid = FuelType.objects.get(name = "Hybrid")

# c180.fueltype.add(gas)
# c180.fueltype.add(diseal, hybrid)#...add more fuel type
# print(c180.fueltype.all())#.....fetch all fueltype


# c200.fueltype.create(name = "Bio diseal")
# print(c200.fueltype.all())

# print(gas.carmodel_set.all())#.......get carmodel from fuel
# print(hybrid.carmodel_set.all())#.......get carmodel from fuel

# print(gas.carmodels.all())#.......in model.py we added related_name so we don't need to do set.all

# print(Carmodel.objects.filter(fueltype__name__startswith = "G"))#.......it will give carmodel from fueltype startwith "G"

# print(FuelType.objects.filter(carmodels__name__startswith = "C"))


# c180.fueltype.clear()

# print(Student.objects.filter(dept_college__name = "MIT"))


# video no ----107

# 1st way-- raw sql

from django.db import connection
# cursor = connection.cursor()#.....for connection with db
# cursor.execute("Select * from student")#....from sql query we can fetch data....raw sql
# data = cursor.fetchall()
# print(data)


# 2nd way--

# data = Student.objects.raw("select * from Student")
# for i in data:
#     print(i)


# multiple database--

# print(Student.objects.all())
# exec(open(r'F:\code files\B8_django_web\first_project\app1\db_shell.py').read())



SECOND_DATABASE = "second_db"
print(Student.objects.using(SECOND_DATABASE).all())


#c1 = College.objects.using(SECOND_DATABASE).create(name = "Bajaj", adr = "Wardha")
# d1 = Department.objects.using(SECOND_DATABASE).create(name = "ENTC", dept_str = 65, college = c1)
# s1 = Student.objects.using(SECOND_DATABASE).cr
# 
# eate(name = "Gauri", marks = 75, age = 20, department = d1)
# s2 = Student.objects.using(SECOND_DATABASE).create(name = "payal", marks = 85, age = 24, department = d1)
# subj1 = Subjects.objects.using(SECOND_DATABASE).create(name = "control system", is_practical = True, dept = d1)
