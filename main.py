# Config from txt

import pickle
import mysql.connector
import pandas as pd
import os

def create_credentials(passw,name,ocp):
    with open('Content\\config.dat','wb') as file:
        pickle.dump('pass='+str(passw)+',nam='+str(name)+',op='+str(ocp),file)

def get_credentials():
    with open('Content\\config.dat','rb') as file:
        data=pickle.load(file)
    credentials={}
    split_content=data.split(',')
    passw,nam,op=split_content[0].split('pass=')[1],split_content[1].split('nam=')[1],split_content[2].split('op=')[1]
    credentials['Name'],credentials['Ocup'],credentials['Pass']=nam,op,passw
    return credentials


def check_credentials():
    try:
        get_credentials()
        return True
    except:
        return False

def create_database(paswd):
    mycon=mysql.connector.connect(host='localhost',user='root',password=paswd)
    cur=mycon.cursor()
    cur.execute('create database Fizzy;')
    mycon.commit()

def user_script(name):
    script=('''Hello '''+name+''',
This is from the developer who created this software.The name of the software is Fizzy.
It is used for fast and simple way of inputing data into mysql database.
In The latest version of Fizzy,Fizzy  Ver-0.01 , It has only one option and 
it is for school purposes, like saving students data.
I hope you liked the software....Thank you for using this software
Your Sincerely
Developer
Pica Poweer
:)''')
    with open('Content\\Introduction.txt','w') as file:
        file.write(script)

def create_table_studnet(paswd):
    mycon=mysql.connector.connect(host='localhost',user='root',password=paswd,database='fizzy')
    cur=mycon.cursor()
    cur.execute('create table Students_details(Roll_no varchar(4) NOT NULL,Name varchar(30) NOT NULL,Gender varchar(3) NOT NULL,Blood_Group varchar(5) NOT NULL,Family_Members varchar(3) NOT NULL);')
    mycon.commit()

def student_details(roll,name,gender,bg,fam,paswd):
    mycon=mysql.connector.connect(host='localhost',user='root',password=paswd,database='fizzy')
    cur=mycon.cursor()
    cur.execute("insert into Students_details VALUES('"+str(roll)+"','"+str(name)+"','"+str(gender)+"','"+str(bg)+"','"+str(fam)+"');")
    mycon.commit()

def show_student_details(paswd):
    mycon=mysql.connector.connect(host='localhost',user='root',password=paswd,database='fizzy')
    cur=mycon.cursor()
    cur.execute("select*from Students_details;")
    roll=[]
    name=[]
    gen=[]
    bg=[]
    fam=[]
    for i in cur:
        roll.append(i[0])
        name.append(i[1])
        gen.append(i[2])
        bg.append(i[3])
        fam.append(i[4])
    data={'Roll No':roll,'Name':name,'Gender':gen,'Blood Group':bg,'Family Members':fam}
    dp=pd.DataFrame(data)
    content=dp.to_string()
    with open('Content\\Students Details.txt','w') as file:
        file.write(content)

def create_folders():
    directory='Content'
    parent_dir=''
    path=os.path.join(parent_dir,directory)
    os.mkdir(path)



