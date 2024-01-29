import cx_Oracle
dbconn=cx_Oracle.Connection('system/manager@mother')
cursor=dbconn.cursor()

def createtable():
    query='create table mcabhav15(id number(3) primary key,name varchar(70))'
    cursor.execute(query)
    print('table created')
#createtable()

def insert_data():
    query='insert into mcabhav15 values(7,bhanu)'
    cursor.execute(query)
    dbconn.commit()
    print("data inserted")
def insert_record(sid,name):
    record={'id':str(sid),'name':name}
    query='insert into mcabhav15 values(:id,:name)'
    cursor.execute(query,record)
    dbconn.commit()
    print('data inserted')
#insert_record(2,'bhanu')
#insert_record(3,'hari')
#insert_record(4,'bindu')
#insert_record(5,'chandu')
#insert_record(6,'janu')
#insert_record(7,'charan')
#nsert_record(8,'DD')

def read_records():
    query='select * from mcabhav15'
    cursor.execute(query)
    records=cursor.fetchall()
    for row in records:
        print(row)
#read_records()
def get_record(sid):
    record={'id':str(sid)}
    query='select * from mcabhav15 where id=:id'
    cursor.execute(query,record)
    record=cursor.fetchone()
    print(record)
    #for row in record:
    #    print(row)
#get_record(2)
#get_record(3)
#get_record(4)

def update_name(sid):
    get_record(sid)
    name=input('enter new name to update:')
    record={'id':str(sid),'name':name}
    query='update mcabhav15 set name=:name where id=:id'
    cursor.execute(query,record)
    dbconn.commit()
    get_record(sid)
#update_name(2)
def delete_record(sid):
    record={'id':str(sid)}
    query='delete from mcabhav15 where id=:id'
    cursor.execute(query,record)
    dbconn.commit()
    print('record is deleted')
#delete_record(4)
def truncate():
    query='truncate table mcabhav15'
    cursor.execute(query)
    dbconn.commit()
    print('empty')
truncate()
def get_tables():
    query='select * from tab'
    cursor.execute(query)
    tables=cursor.fetchall()
    for table in tables:
        print(table[0])
#get_tables()
def desc_table():
    query='desc mcabhav15'
    cursor.execute(query)
    records=cursor.fetchall()
    for i in records:
        print(i)



    

    