class prime:
    def isprime(self):
        flag=True
        if self.a>1:
            for val in range(2,self.a):
                if self.a%val==0:
                    flag=False
                    break
        return flag
