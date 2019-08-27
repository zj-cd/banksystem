# coding=gbk
import time
class Admin(object):
    # def __init__(self,admin):
    #     self.admin=admin
    admin="1"
    passwd="1"
    def printAdminView(self):
        print("*" * 35)
        print("*                                 *")
        print("*                                 *")
        print("*                                 *")
        print("*       欢迎登陆银行系统           *")
        print("*                                 *")
        print("*                                 *")
        print("*                                 *")
        print("*" * 35)

    def printSysFunctionView(self):
        print("*" * 35)
        print("*   开户（1）   查询（2）         *")
        print("*   取款（3）   存款（4）         *")
        print("*   转账（5）   改密（6）         *")
        print("*   锁定（7）   解锁（8）         *")
        print("*   补卡（9）   销户（10）        *")
        print("*          退出(q)                *")
        print("*" * 35)
    def adminOption(self):
        inputAdmin = input("请输入管理员账号：")
        if self.admin != inputAdmin:
            print("账号输入错误！")
            return -1
        inputPasswd = input("请输入管理员密码：")
        if self.passwd != inputPasswd:
            print("密码输入错误！")
            return -1
        print("操作成功！请稍后... ... ")
        time.sleep(1)
        return 0

# v1=View()
# v1.printAdminView()
# v1.printSysFunctionView()
