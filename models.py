import datetime

class User:
    def __init__(self,tel='',username='',password='',money=0):
        self.tel = tel
        self.username = username
        self.password = password
        self.money = money
    def getmoney(self):
        return self.money
    def setmoney(self,m):
        self.money = m
    def setusername(self,un):
        self.username=un
    def setpassword(self,pw):
        self.password=pw
    def setall(self,values):
        self.tel = values[0]
        self.setusername(values[1])
        self.setpassword(values[2])
        self.setmoney(values[3])


class Goods:
    def __init__(self,gid=0,gname='',pic='',price=0,introction=''):
        self.gid=gid
        self.gname=gname
        self.pic=pic
        self.price=price
        self.introduction=introction
    def setall(self,values):
        self.__init__(values[0],values[4],values[1],values[3],values[2])
    def getprice(self):
        return self.price

# class History:
#     def __init__(self,tel,gid,datetime):