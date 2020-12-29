import sys
print("中文")
str1 = "this is srring"
print(str1.isalpha())
print(max(str1))

while 1 :
    user = input("輸入你的姓名：")
    pwd = input("passwd:")
    if user == "badman" and pwd == "123" :
        print("login success")
        break
    else :
        print("login fail")
        continue
print(sys.getdefaultencoding())


list