class mtca:
    principal="Mr.Prabhakar Naidu"
    college="Mother teresa institute of computer applications"
    location="Melumoi,Palamaner"
    def __init__(self,sname,mbno,mail,sem,addr):
        self.studentname=sname
        self.mobilenumber=mbno
        self.email=mail
        self.semister=sem
        self.address=addr
        
    def update_mob(self,new):
        self.mobilenumber=new
        print("mobile number is updated")

    @classmethod
    def change_principal(cls,new):
        cls.principal=new

    @staticmethod
    def add(a,b):
        return a+b
    
sravan=mtca("sravan",12345555,"skr@gmail.com",1,"amrp")
skr=mtca("skr",000000000,"skb@gmail.com",4,"plmr")
