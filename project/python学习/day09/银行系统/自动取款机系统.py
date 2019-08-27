# coding=utf-8
# 人
# 类名;Person
# 属性：姓名 身份证号 电话号 卡
# 行为：
#
# 卡
# 类名：Card
# 属性：卡号 密码 余额
# 行为：

#
#
# 取款机
# 类名：ATM
# 属性：用户字典
# 行为：开户 销户 取款 查询 解锁 锁定 改密 转账 存储 补卡  退出
#
#
# admin
# 类名：Admin
# 属性：
# 行为：管理员界面 管理员验证  系统功能界面

from admin import Admin
from atm import ATM
import time
import pickle
import os

def main():
   # 管理员对象
    admin=Admin()

    admin.printAdminView()

    if admin.adminOption():
        return -1
    # allUsers={}

    # 存储所以用户信息


    filepath = os.path.join(os.getcwd(), "allusers.txt")
    f = open(filepath, "rb")
    allUsers=pickle.load(f)
    atm = ATM(allUsers)



    time.sleep(1)
    while True:
        admin.printSysFunctionView()
        # 等待用户操作
        option=input("请输入您的操作:")
        if option == "1":
            atm.creatUser()
        if option == "2":
            atm.searchUserInfo()
        if option == "3":
            atm.getMonsy()
        if option == "4":
            atm.saveMoney()
        if option == "5":
            atm.transferMoney()
        if option == "6":
            atm.changePasswd()
        if option == "7":
            atm.lockUser()
        if option == "8":
            atm.unlockUser()
        if option == "9":
            atm.newCard()
        if option == "10":
            atm.killUser()
        if option == "q":
            if not admin.adminOption():
                filepath=os.path.join(os.getcwd(),"allusers.txt")
                f=open(filepath,"wb")
                pickle.dump(atm.allUsers,f)
                f.close()

                return -1


# def adminQuit()





if __name__ == '__main__':
    main()
