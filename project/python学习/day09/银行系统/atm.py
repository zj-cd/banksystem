# coding=gbk
from card import Card
from user import User
import random

class ATM(object):
    def __init__(self,allUsers):
        self.allUsers=allUsers
    def creatUser(self,):
        # 目标;向用户字典中添加一对键值对（卡号-用户）
        name=input("请输入您的姓名：")
        idCard=input("请输入您的身份证号码：")
        phone=input("请输入您的电话号码：")
        prestoreMoney=int(input("请输入预存款金额："))
        if prestoreMoney < 0:
            print("预存款输入有误！！！开户失败")
            return -1

        onePasswd=input("请设置密码：")
        if not self.checkPasswd(onePasswd):
            print("密码输入错误!!!开户失败……")
            return -1

        cardStr=self.randomCardId()

        card=Card(cardStr,onePasswd,prestoreMoney)
        user=User(name,idCard,phone,card)
        # 存到字典
        self.allUsers[cardStr]=user
        print("开户成功！！！请牢记您的卡号："+cardStr)
        # print(self.allUsers)

    def searchUserInfo(self):
        cardNum=input("请输入您的卡号:")
        user=self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！！！查询失败……")
            return -1

        # 判断是否锁定
        if user.card.cardLock:
            print("该卡已被锁定！！！请解锁后进行其他操作……")
            return -1

        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误!!!该卡已被锁定！！！请解锁后进去其他操作……")
            user.card.cardLock=True
            return -1
        print("账号：%s   余额：%d"%(cardNum,user.card.cardMoney))
    def getMonsy(self):
        cardNum=input("请输入您的卡号:")
        user=self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！！！取款失败……")
            return -1

        # 判断是否锁定
        if user.card.cardLock:
            print("该卡已被锁定！！！请解锁后进行其他操作……")
            return -1

        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误!!!该卡已被锁定！！！请解锁后进去其他操作……")
            user.card.cardLock=True
            return -1
        money=int(input("请输入取款金额："))
        if money>user.card.cardMoney:
            print("余额不足！！！请重新操作……")
            return -1
        if money <= 0:
            print("输入错误！！！请重新操作……")
            return -1
        user.card.cardMoney -= money
        print("账号：%s   余额：%d"%(user.card.cardId,user.card.cardMoney))
    def saveMoney(self):
        cardNum=input("请输入您的卡号:")
        user=self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！！！取款失败……")
            return -1

        # 判断是否锁定
        if user.card.cardLock:
            print("该卡已被锁定！！！请解锁后进行其他操作……")
            return -1

        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误!!!该卡已被锁定！！！请解锁后进去其他操作……")
            user.card.cardLock=True
            return -1
        savemoney=int(input("请输入存款金额："))
        if savemoney <= 0:
            print("输入错误！！！请重新操作……")
            return -1
        user.card.cardMoney += savemoney
        print("账号：%s   余额：%d"%(user.card.cardId,user.card.cardMoney))
    def transferMoney(self):
        cardNum=input("请输入您的卡号:")
        user=self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！！！操作失败……")
            return -1

        # 判断是否锁定
        if user.card.cardLock:
            print("该卡已被锁定！！！请解锁后进行其他操作……")
            return -1

        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误!!!该卡已被锁定！！！请解锁后进去其他操作……")
            user.card.cardLock=True
            return -1
        cardNum2=input("请输入您要转账的卡号：")
        user2=self.allUsers.get(cardNum2)
        if not user2:
            print("该卡号不存在！！！操作失败……")
            return -1

        # 判断是否锁定
        if user2.card.cardLock:
            print("该卡已被锁定！！！请解锁后进行其他操作……")
            return -1

        if not self.checkPasswd(user2.card.cardPasswd):
            print("密码输入错误!!!该卡已被锁定！！！请解锁后进去其他操作……")
            user.card.cardLock=True
            return -1
        transmoney=int(input("请输入您要转账的金额"))
        if transmoney>user.card.cardMoney:
            print("余额不足！！1请重新操作……")
        if transmoney < 0:
            print("输入错误！！！请重新操作……")
        user.card.cardMoney -= transmoney
        user2.card.cardMoney +=transmoney
        print("账号：%s   余额：%d"%(cardNum,user.card.cardMoney))
    def changePasswd(self):
        cardNum=input("请输入您的卡号:")
        user=self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！！！改密失败……")
            return -1
        if user.card.cardLock:
            print("该卡已被锁定！！！请解锁后在操作……")
            return -1
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误!!!改密失败... ...")
            return -1
        tempIdCard=input("请输入您的身份证号：")
        if tempIdCard != user.idCard:
            print("身份证号码输入错误！！！改密失败")
            return -1
        user.card.cardPasswd=input("请输入新密码：")
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误!!!改密失败... ...")
            return -1
        print("改密成功！！！")
    def lockUser(self):
        cardNum=input("请输入您的卡号:")
        user=self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！！！锁定失败……")
            return -1
        if user.card.cardLock:
            print("该卡已被锁定！！！请解锁后在操作……")
            return -1
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误!!!锁定失败... ...")
            return -1
        tempIdCard=input("请输入您的身份证号：")
        if tempIdCard != user.idCard:
            print("身份证号码输入错误！！！锁定失败")
            return -1
        # 锁定
        user.card.cardLock=True
        print("锁定成功！！！")


    def unlockUser(self):
        cardNum=input("请输入您的卡号:")
        user=self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！！！解锁失败……")
            return -1
        if not user.card.cardLock:
            print("该卡没有被锁定！！！无需解锁……")
            return -1
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误!!!解锁失败……")
            return -1
        tempIdCard=input("请输入您的身份证号：")
        if tempIdCard != user.idCard:
            print("身份证号码输入错误！！！解锁失败……")
            return -1
        # 解锁
        user.card.cardLock=False
        print("解锁成功！！！")



    def newCard(self):
        cardNum=input("请输入您的卡号:")
        user=self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！！！操作失败……")
            return -1
        if  user.card.cardLock:
            print("该卡已被锁定！！！请解锁后操作……")
            return -1
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误!!!补卡失败……")
            return -1
        tempIdCard=input("请输入您的身份证号：")
        if tempIdCard != user.idCard:
            print("身份证号码输入错误！！！补卡失败……")
            return -1
        newCardId=self.randomCardId()
        # user.card.cardId=newCardId
        self.allUsers[newCardId]=self.allUsers.pop(user.card.cardId)
        print("请牢记您的新卡号！！！"+newCardId)
    def killUser(self):
        cardNum=input("请输入您的卡号:")
        user=self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！！！操作失败……")
            return -1
        self.allUsers.pop(cardNum)
        print("销户成功！！！")

    # 验证密码
    def checkPasswd(self,realPasswd):
        for i in range(3):
            tempPasswd=input("请输入密码：")
            if tempPasswd == realPasswd:
                return True
        return False

    # 生成卡号
    def randomCardId(self):
        while True:
            str = ""
            for i in range(6):
                ch=chr(random.randrange(ord("0"),ord("9")+1))
                str += ch
            if not self.allUsers.get(str):
                return str

    def verification(self):
        cardNum=input("请输入您的卡号:")
        user=self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！！！取款失败……")
            return -1

        # 判断是否锁定
        if user.card.cardLock:
            print("该卡已被锁定！！！请解锁后进行其他操作……")
            return -1

        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误!!!该卡已被锁定！！！请解锁后进去其他操作……")
            user.card.cardLock=True
            return -1
