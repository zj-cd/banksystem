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
        print("*       ��ӭ��½����ϵͳ           *")
        print("*                                 *")
        print("*                                 *")
        print("*                                 *")
        print("*" * 35)

    def printSysFunctionView(self):
        print("*" * 35)
        print("*   ������1��   ��ѯ��2��         *")
        print("*   ȡ�3��   ��4��         *")
        print("*   ת�ˣ�5��   ���ܣ�6��         *")
        print("*   ������7��   ������8��         *")
        print("*   ������9��   ������10��        *")
        print("*          �˳�(q)                *")
        print("*" * 35)
    def adminOption(self):
        inputAdmin = input("���������Ա�˺ţ�")
        if self.admin != inputAdmin:
            print("�˺��������")
            return -1
        inputPasswd = input("���������Ա���룺")
        if self.passwd != inputPasswd:
            print("�����������")
            return -1
        print("�����ɹ������Ժ�... ... ")
        time.sleep(1)
        return 0

# v1=View()
# v1.printAdminView()
# v1.printSysFunctionView()
