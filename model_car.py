from abc import ABC,abstractmethod
class modelcar():
    @abstractmethod
    def break1():
        pass

    @abstractmethod
    def speed_up():
        pass

    @abstractmethod
    def speed_down():
        pass

class Nexon(modelcar):
    def __init__(self,speed=0,stop=True):
        self.speed=speed
        self.speeddown=speed
        self.stop=stop

    def speed_up(self):
        self.speed+=5
        self.stop=False
        print(f"accelerated by 5kmph and current speed is {self.speed}")

    def speed_down(self):
        if not self.stop:
            self.speed-=5
            print(f"accelerated decrease by 5kmph and current speed is {self.speed}")
            if self.speed==0:
                self.stop=True
        else:
            print("car in off mode")

    def break1(self):
        self.speed=0
        self.stop=True

class Tesla(modelcar):
    def __init__(self,speed=0,stop=True):
        self.speed=speed
        self.speeddown=speed
        self.stop=stop

    def speed_up(self):
        self.speed+=2
        self.stop=False
        print(f"accelerated by 2kmph and current speed is {self.speed}")

    def speed_down(self):
        if not self.stop:
            self.speed-=2
            print(f"accelerated decrease by 2kmph and current speed is {self.speed}")
            if self.speed==0:
                self.stop=False
        else:
            print("car in stop mode")

    def break1(self):
        self.speed=0
        self.stop=True