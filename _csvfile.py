#import csv
#with open('sample.csv','w',newline='') as file:
#    data=[
#        [1,'sravan',20],
#        [2,'karna',22],
#        [3,'bhanu',21]
#        ]
#    record=csv.writer(file)
#    record.writerow(['id','name','age'])
#    record.writerows(data)


#import csv
#with open('sample.csv','a',newline='') as file:
#
#    record=csv.writer(file)
#    record.writerow([4,'darshan','06'])


#import csv
#with open('sample.csv','r',newline='') as file:
#    record=csv.reader(file)
#    for i in record:
#        print(i)


#import csv
#with open('sample1.csv','w',newline='') as file:
#    fieldnames=['id','name','age']
#    record=csv.DictWriter(file,fieldnames)
#    record.writeheader()
#    data=[
#        {'id':1,'name':'darshan','age':20},
#        {'id':2,'name':'deevan','age':29},
#        {'id':3,'name':'dhruva','age':23},
#    ]
#    record.writerows(data)


import csv
with open('sample1.csv','r',newline='') as file:
    record=csv.DictReader(file)
    for i in record:
        print(i)