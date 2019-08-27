# coding=gbk
from card import Card
from user import User
import random

class ATM(object):
    def __init__(self,allUsers):
        self.allUsers=allUsers
    def creatUser(self,):
        # Ŀ��;���û��ֵ������һ�Լ�ֵ�ԣ�����-�û���
        name=input("����������������")
        idCard=input("�������������֤���룺")
        phone=input("���������ĵ绰���룺")
        prestoreMoney=int(input("������Ԥ����"))
        if prestoreMoney < 0:
            print("Ԥ����������󣡣�������ʧ��")
            return -1

        onePasswd=input("���������룺")
        if not self.checkPasswd(onePasswd):
            print("�����������!!!����ʧ�ܡ���")
            return -1

        cardStr=self.randomCardId()

        card=Card(cardStr,onePasswd,prestoreMoney)
        user=User(name,idCard,phone,card)
        # �浽�ֵ�
        self.allUsers[cardStr]=user
        print("�����ɹ����������μ����Ŀ��ţ�"+cardStr)
        # print(self.allUsers)

    def searchUserInfo(self):
        cardNum=input("���������Ŀ���:")
        user=self.allUsers.get(cardNum)
        if not user:
            print("�ÿ��Ų����ڣ�������ѯʧ�ܡ���")
            return -1

        # �ж��Ƿ�����
        if user.card.cardLock:
            print("�ÿ��ѱ���������������������������������")
            return -1

        if not self.checkPasswd(user.card.cardPasswd):
            print("�����������!!!�ÿ��ѱ�������������������ȥ������������")
            user.card.cardLock=True
            return -1
        print("�˺ţ�%s   ��%d"%(cardNum,user.card.cardMoney))
    def getMonsy(self):
        cardNum=input("���������Ŀ���:")
        user=self.allUsers.get(cardNum)
        if not user:
            print("�ÿ��Ų����ڣ�����ȡ��ʧ�ܡ���")
            return -1

        # �ж��Ƿ�����
        if user.card.cardLock:
            print("�ÿ��ѱ���������������������������������")
            return -1

        if not self.checkPasswd(user.card.cardPasswd):
            print("�����������!!!�ÿ��ѱ�������������������ȥ������������")
            user.card.cardLock=True
            return -1
        money=int(input("������ȡ���"))
        if money>user.card.cardMoney:
            print("���㣡���������²�������")
            return -1
        if money <= 0:
            print("������󣡣��������²�������")
            return -1
        user.card.cardMoney -= money
        print("�˺ţ�%s   ��%d"%(user.card.cardId,user.card.cardMoney))
    def saveMoney(self):
        cardNum=input("���������Ŀ���:")
        user=self.allUsers.get(cardNum)
        if not user:
            print("�ÿ��Ų����ڣ�����ȡ��ʧ�ܡ���")
            return -1

        # �ж��Ƿ�����
        if user.card.cardLock:
            print("�ÿ��ѱ���������������������������������")
            return -1

        if not self.checkPasswd(user.card.cardPasswd):
            print("�����������!!!�ÿ��ѱ�������������������ȥ������������")
            user.card.cardLock=True
            return -1
        savemoney=int(input("���������"))
        if savemoney <= 0:
            print("������󣡣��������²�������")
            return -1
        user.card.cardMoney += savemoney
        print("�˺ţ�%s   ��%d"%(user.card.cardId,user.card.cardMoney))
    def transferMoney(self):
        cardNum=input("���������Ŀ���:")
        user=self.allUsers.get(cardNum)
        if not user:
            print("�ÿ��Ų����ڣ���������ʧ�ܡ���")
            return -1

        # �ж��Ƿ�����
        if user.card.cardLock:
            print("�ÿ��ѱ���������������������������������")
            return -1

        if not self.checkPasswd(user.card.cardPasswd):
            print("�����������!!!�ÿ��ѱ�������������������ȥ������������")
            user.card.cardLock=True
            return -1
        cardNum2=input("��������Ҫת�˵Ŀ��ţ�")
        user2=self.allUsers.get(cardNum2)
        if not user2:
            print("�ÿ��Ų����ڣ���������ʧ�ܡ���")
            return -1

        # �ж��Ƿ�����
        if user2.card.cardLock:
            print("�ÿ��ѱ���������������������������������")
            return -1

        if not self.checkPasswd(user2.card.cardPasswd):
            print("�����������!!!�ÿ��ѱ�������������������ȥ������������")
            user.card.cardLock=True
            return -1
        transmoney=int(input("��������Ҫת�˵Ľ��"))
        if transmoney>user.card.cardMoney:
            print("���㣡��1�����²�������")
        if transmoney < 0:
            print("������󣡣��������²�������")
        user.card.cardMoney -= transmoney
        user2.card.cardMoney +=transmoney
        print("�˺ţ�%s   ��%d"%(cardNum,user.card.cardMoney))
    def changePasswd(self):
        cardNum=input("���������Ŀ���:")
        user=self.allUsers.get(cardNum)
        if not user:
            print("�ÿ��Ų����ڣ���������ʧ�ܡ���")
            return -1
        if user.card.cardLock:
            print("�ÿ��ѱ�������������������ڲ�������")
            return -1
        if not self.checkPasswd(user.card.cardPasswd):
            print("�����������!!!����ʧ��... ...")
            return -1
        tempIdCard=input("�������������֤�ţ�")
        if tempIdCard != user.idCard:
            print("���֤����������󣡣�������ʧ��")
            return -1
        user.card.cardPasswd=input("�����������룺")
        if not self.checkPasswd(user.card.cardPasswd):
            print("�����������!!!����ʧ��... ...")
            return -1
        print("���ܳɹ�������")
    def lockUser(self):
        cardNum=input("���������Ŀ���:")
        user=self.allUsers.get(cardNum)
        if not user:
            print("�ÿ��Ų����ڣ���������ʧ�ܡ���")
            return -1
        if user.card.cardLock:
            print("�ÿ��ѱ�������������������ڲ�������")
            return -1
        if not self.checkPasswd(user.card.cardPasswd):
            print("�����������!!!����ʧ��... ...")
            return -1
        tempIdCard=input("�������������֤�ţ�")
        if tempIdCard != user.idCard:
            print("���֤����������󣡣�������ʧ��")
            return -1
        # ����
        user.card.cardLock=True
        print("�����ɹ�������")


    def unlockUser(self):
        cardNum=input("���������Ŀ���:")
        user=self.allUsers.get(cardNum)
        if not user:
            print("�ÿ��Ų����ڣ���������ʧ�ܡ���")
            return -1
        if not user.card.cardLock:
            print("�ÿ�û�б����������������������")
            return -1
        if not self.checkPasswd(user.card.cardPasswd):
            print("�����������!!!����ʧ�ܡ���")
            return -1
        tempIdCard=input("�������������֤�ţ�")
        if tempIdCard != user.idCard:
            print("���֤����������󣡣�������ʧ�ܡ���")
            return -1
        # ����
        user.card.cardLock=False
        print("�����ɹ�������")



    def newCard(self):
        cardNum=input("���������Ŀ���:")
        user=self.allUsers.get(cardNum)
        if not user:
            print("�ÿ��Ų����ڣ���������ʧ�ܡ���")
            return -1
        if  user.card.cardLock:
            print("�ÿ��ѱ�������������������������")
            return -1
        if not self.checkPasswd(user.card.cardPasswd):
            print("�����������!!!����ʧ�ܡ���")
            return -1
        tempIdCard=input("�������������֤�ţ�")
        if tempIdCard != user.idCard:
            print("���֤����������󣡣�������ʧ�ܡ���")
            return -1
        newCardId=self.randomCardId()
        # user.card.cardId=newCardId
        self.allUsers[newCardId]=self.allUsers.pop(user.card.cardId)
        print("���μ������¿��ţ�����"+newCardId)
    def killUser(self):
        cardNum=input("���������Ŀ���:")
        user=self.allUsers.get(cardNum)
        if not user:
            print("�ÿ��Ų����ڣ���������ʧ�ܡ���")
            return -1
        self.allUsers.pop(cardNum)
        print("�����ɹ�������")

    # ��֤����
    def checkPasswd(self,realPasswd):
        for i in range(3):
            tempPasswd=input("���������룺")
            if tempPasswd == realPasswd:
                return True
        return False

    # ���ɿ���
    def randomCardId(self):
        while True:
            str = ""
            for i in range(6):
                ch=chr(random.randrange(ord("0"),ord("9")+1))
                str += ch
            if not self.allUsers.get(str):
                return str

    def verification(self):
        cardNum=input("���������Ŀ���:")
        user=self.allUsers.get(cardNum)
        if not user:
            print("�ÿ��Ų����ڣ�����ȡ��ʧ�ܡ���")
            return -1

        # �ж��Ƿ�����
        if user.card.cardLock:
            print("�ÿ��ѱ���������������������������������")
            return -1

        if not self.checkPasswd(user.card.cardPasswd):
            print("�����������!!!�ÿ��ѱ�������������������ȥ������������")
            user.card.cardLock=True
            return -1
