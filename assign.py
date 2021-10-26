
#  Enter the table name you want to create
# Enter the no. of files to create

import os
import time
import shutil
import mysql.connector as connector

# to connect mysql to python prog 
con = connector.connect(host = "localhost", 
                                    port = "3306", 
                                    user = "root", 
                                    password = "root", 
                                    database = "testdatabase")

# to insert status in table 

def create_table():
    query = f'create table if not exists {table_create}(Queue int)'
    cur1 = con.cursor()
    cur1.execute(query)

def queue_value(status):
    query1 = f"insert into {table_create}(Queue) values({status})"
    cur = con.cursor()
    cur.execute(query1)
    con.commit()


# user inputs
table_create = input('Enter the name of table to create a table :- ')
file_no = int(input('Enter the no of files :- '))

seconds = 1

# func to create files in processing folder 
def file_create(x):
    for i in range (1,x+1):
        global seconds
        path = 'Processing'
        file = f'{i}.txt'
        with open(os.path.join(path,file), 'w') as fp:
            time.sleep(1)
        if seconds == 5:
            move_files()
            # time.sleep(1)
            move_files_to_processed()
        elif i==x:
            move_files()
            # time.sleep(1)
            move_files_to_processed()
        else:
            seconds += 1

# func to move file from processing to queue folder 
def move_files():
    global seconds
    file_names = os.listdir('Processing')
    for file_name in file_names:
        shutil.move(os.path.join('Processing', file_name), 'Queue')
        seconds = 1
    queue_value(1)

# func to move file from queue to processed folder 
def move_files_to_processed():
    file_names = os.listdir('Queue')
    for file_name in file_names:
        shutil.move(os.path.join('Queue', file_name), 'Processed')
    queue_value(0)
        

create_table()
file_create(file_no)




        














