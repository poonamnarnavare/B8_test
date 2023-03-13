import pymysql
import random
import string
import csv

class Person:#.................person class defined
    def __init__(self, firstname, lastname, age):#.....init method or constructor
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def __str__(self):#.......str method
        return f"\n{self.__dict__}"

    def __repr__(self):
        return str(self)

p1 = Person("Poonam", "Narnavare", 24)#......multiple objects created
p2 = Person("Komal", "Manekar", 23)
p3 = Person("Kaveri", "Pande", 22)
p4 = Person("Akansha", "Kale", 25)

Person_list = [p1, p2, p3, p4]

lst = [[p.lastname, p.firstname, p.age] for p in Person_list]


HOST = "127.0.0.1"
USERNAME = "root"
PASSWORD = "Y1012jqkhkp"
DATABASE = "b8_test"

Create_table_Query = """Create table persons (ID int NOT NULL AUTO_INCREMENT,
                        LastName varchar(255) NOT NULL,
                        FirstName varchar(255) NOT NULL,
                        Age int,                                      #....................queries
                        PRIMARY KEY (ID));"""

Insert_query = "insert into persons(lastname, firstname, age) values (%s, %s, %s)"
Select_query = "select * from {}"
Select_query1 = "select * from {} where salary < 25000"
update_query = "update b8_test.persons set lastname = %s where ID = %s"
truncate_query = "truncate  table b8_test.{}"
delete_query = "DELETE FROM b8_test.persons WHERE firstname = %s"
alter_query = "alter table b8_test.persons add pincode varchar(255) NOT NULL default '411057'"
alter_query_add_sal = "alter table b8_test.persons add salary integer NOT NULL default 0"
update_query1 = "update b8_test.persons set salary = %s where ID = %s"

class MySqloperation:
    def get_db_connection(self):#.............for building an connection with database
        try:
            conn = pymysql.connect(host = HOST , user = USERNAME , password = PASSWORD, database = DATABASE)
            return conn
        except pymysql.err.OperationalError as msg:
            if "Access denied" in str(msg):
                return("Invalid name and Password")
            elif "Unknown database" in str(msg):
                return("given database is not present.")

    def get_databases(self):
        conn = self.get_db_connection() #....for connection
        Query = "show databases"
        communication_channel = conn.cursor()
        communication_channel.execute(Query)
        result = communication_channel.fetchall()
        all_dbs = list(map(lambda x : x[0], result))#......to get all database in single list
        #print(all_dbs)

    def get_tables(self):
        conn = self.get_db_connection() #....for connection
        Query = "show databases"
        communication_channel = conn.cursor()
        communication_channel.execute(Query)
        result = communication_channel.fetchall()
        all_tables = list(map(lambda x : x[0], result))
        #print(all_tables)
        
    def create_table(self, tablename):   #......tablename
        conn = self.get_db_connection()
        communication_channel = conn.cursor()
        try:
            communication_channel.execute(Create_table_Query.format(tablename))
        except pymysql.err.OperationalError as msg:#.........error handle
            if "already exists" in str(msg):
                 return("Table is already exists")
        return("Table Created Successfully..")

    def insert_records(self):
        conn = self.get_db_connection()
        communication_channel = conn.cursor()
        try:
            for person in Person_list:
                communication_channel.execute(Insert_query.format(person.lastname, person.firstname, person.age))
        except Exception as msg:
            print(str(msg))
            conn.commit()
            return("Data Inserted successfully..")

    def insert_records(self):
        conn = self.get_db_connection()
        communication_channel = conn.cursor()
        try: 
            person_list = [["Poonam", "Narnavare", 24], ["Komal", "Manekar", 23], ["Kaveri", "Pande", 22], ["Akansha", "Kale", 25]]
            communication_channel.executemany(Insert_query, lst)
        except Exception as msg:
            print(str(msg))
        conn.commit()
        return("Data Inserted Successfully..")

    
    def get_records(self, tablename):
        list_of_person = []
        conn = self.get_db_connection()
        communication_channel = conn.cursor()
        #communication_channel.execute(Select_query.format(tablename))
        communication_channel.execute(Select_query1.format(tablename))#...............for salary less than 25000
        resultset = communication_channel.fetchall()
        print(resultset)
        for person in resultset:
            obj = Person(person[2], person[1], person[3])
        #print(list_of_person)

    
    def update_record(self, lastname, ID):      # id, lastname
        conn = self.get_db_connection()
        communication_channel = conn.cursor()   
        input_data = (lastname, ID)#...............input as a lastname and id        
        communication_channel.execute(update_query, input_data)                   
        conn.commit()
        return("Data updated successfully..")

    
    
    def truc(self, tablename):      
        conn = self.get_db_connection()
        communication_channel = conn.cursor()  
        communication_channel.execute(truncate_query.format(tablename))                   
        conn.commit()
        return("Table truncated successfully..")

    
    
    def delete(self, firstname):   #...........delete firstname   
        conn = self.get_db_connection()
        communication_channel = conn.cursor()         
        communication_channel.execute(delete_query, firstname)                   
        conn.commit()
        return("Record deleted successfully..")

    
    
    def altertable(self):      
        conn = self.get_db_connection()
        communication_channel = conn.cursor()         
        communication_channel.execute(alter_query)                   
        conn.commit()
        return("Table altered successfully..")
    
    
    
    def generate_name():#.....to generate random name
        name = ""
        for i in range(0,random.randint(4,7)):
           s = chr(65 + random.randint(0,25))
           name += s
        return name.title()

    def insert_records_100(self, no):#...............to generate random records
        person_list = []
        conn = self.get_db_connection()
        communication_channel = conn.cursor()
        for i in range(1, no + 1):
         Firstname_inp = ''.join(random.choices(string.ascii_uppercase, k  = random.randint(4, 7))).title()
         lastname_inp = ''.join(random.choices(string.ascii_uppercase, k  = random.randint(4, 7))).title()
         age_inp = random.randint(18, 20)
         input_data=(Firstname_inp, lastname_inp, age_inp)     
         communication_channel.execute(Insert_query, input_data)
         conn.commit()
         return("record Inserted successfully..")


    
    
    def read_table_and_load_csv(self, tablename):#..........for generating csv file
        list_of_person = []
        conn = self.get_db_connection()
        communication_channel = conn.cursor()
        communication_channel.execute(Select_query.format(tablename))
        resultset = communication_channel.fetchall()
        print(resultset)
        for person in resultset:
            with open(r"F:\code files\table_extracted_csv.csv.txt", 'a', newline ='') as file:
                 writer = csv.writer(file)
                 writer.writerow([person[0], person[1], person[2], person[3], person[4], person[5]])

    
    
    def alter_table_salary(self):     
        conn = self.get_db_connection()
        communication_channel = conn.cursor()         
        communication_channel.execute(alter_query_add_sal)                   
        conn.commit()
        return("Table altered successfully..")

    
    
    def update_sal_get_25000(self, tablename):     
        conn = self.get_db_connection()
        communication_channel = conn.cursor()
        communication_channel.execute(Select_query1.format(tablename))
        resultset = communication_channel.fetchall()
        print(resultset)
        for person in resultset:
            id = person[0]
            sal = person[6]
            updated_sal = sal + sal * 10/100
            print(id, sal, updated_sal)
            communication_channel.execute(update_query1, (updated_sal, id))
            return("salary of " , id  ,"incremented by 10 percent from " , sal , "to" ,updated_sal)
           
            
            
if __name__ == "__main__":
    obj = MySqloperation()
    # obj.get_db_connection()
    # obj.get_databases()
    # obj.get_tables()
    # obj.create_table("Persons")
    # obj.insert_records()
    # obj.get_records("persons")
    # obj.update_record("dharane",2)
    # obj.truc("persons")
    # obj.delete("Poonam")
    # obj.altertable()
    # obj.insert_records_100(100)
    # obj.read_table_and_load_csv("persons")
    # obj.alter_table_salary()
    # obj.update_sal_get_25000("persons")

    




# 1. def update_record(self, id, last_name):       # id, lasname
    #     # conn.commit()
    #     pass

    # 2. def update_record(self, id, d):       # id, lasname
        # conn.commit()
        # pass

    # 3. truncate table -- pass tablename

    # 4. def delete(self, id) -- id, -- type int -- single object delete, multiple delete id u pass list, id -- str -- "All" -- delete all
    # 5. alter table add column with default value, not null 
    # 6. insert records -- using generate _persons -- 100 records -- 
    # 7. read data and create a csv of all records -- 
    
    # delete([2,4,7,8])
    # above all with pep8, exception handling, proper comments, return statement, no any print statement

    # salary column while defining table, 
    # salary 25000 less, 10 % increment  -- resultset = SELECT id, salary FROM b8_test.persons where salary<25000;
    # update query -- update table set salary=salary + salary*10% where id=id
    



