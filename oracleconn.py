import cx_Oracle
import csv
conn=cx_Oracle.Connection("system/manager@mother")
cur=conn.cursor()

def createtable():
    query='''create table sravan_78(
    id number(5) primary key,
    name varchar(20)
    )
    '''
    cur.execute(query)
def insertrecord(sid,name):
    record={'id':str(sid),'name':name}
    cur.execute("insert into sravan_78(id,name) values(:id,:name)",record)
    conn.commit()
# insertrecord(1,"SRAVAN")
# insertrecord(2,"KARNA")
# insertrecord(3,"BHANU") 
# insertrecord(4,"DARSHAN")  
# insertrecord(5,"DIA") 
    
def read_records():
    query="select * from sravan_78"
    cur.execute(query)
    records=cur.fetchall()
    # with open("records.csv","w",newline="") as csvfile:
    #     data=csv.writer(csvfile)
    #     data.writerow(['id','name'])
    #     for row in records:
    #         data.writerow(row)
read_records()

def update_record():
    query='''update sravan_78 set name='DIA REDDY' WHERE ID=5'''
    cur.execute(query)
    conn.commit()
update_record()

def fetch_records():
    query="select * from sravan_78 where id=5"
    cur.execute(query)
    records=cur.fetchall()
    for row in records:
        print(row)
fetch_records()

def delete_record():
    query='''delete from sravan_78 WHERE ID=5'''
    cur.execute(query)
    conn.commit()
delete_record()

def truncate():
    query="truncate table sravan_78"
    cur.execute(query)

def insert_from_csv():
    with open('records.csv','r') as csvfile:
        record=csv.reader(csvfile)
        record=list(record)
        for row in range(1,len(record)):
            insertrecord(*record[row])
insert_from_csv()
    