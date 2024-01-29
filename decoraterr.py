import time

def duration(func):
    def inner():
        start=time.time()
        func()
        end=time.time()
        print(f"the total time taken to answer the question is {end-start} in sec")
    return inner

@duration
def question1():
    print("who is principal of MCA in MTCA")
    response=input("enter ur response: ")
@duration
def question2():
    print("who is prime minister of india")
    response=input("enter ur response: ")
@duration
def question3():
    print("what is the capital of andhrapradesh")
    response=input("enter ur response: ")
question1()
question2()
question3()