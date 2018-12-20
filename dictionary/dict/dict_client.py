####/usr/bin/env python3
#coding=utf-8

from socket import *
import sys 
import getpass

def main():
    if len(sys.argv) < 3:
        print("argv is error")
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)

    s = socket()
    s.connect(ADDR)

    while True:
        print('''\n
            ===========Welcome=========
            --1.註冊    2.登錄    3.退出--
            ===========================
            ''')
        try:
            cmd = int(input("輸入選項>>"))
        except Exception:
            print("輸入命令錯誤")
            continue  

        if cmd not in [1,2,3]:
            print("對不起，沒有該命令")
            sys.stdin.flush() #清除輸入
            continue 
        elif cmd == 1:
            name = do_register(s)
            if name != 1:
                print("註冊成功，直接登錄！")
                login(s,name)
            else:
                print("註冊失敗！")
        elif cmd == 2:
            name = do_login(s)
            if name != 1:
                print("登錄成功！")
                login(s,name)
            else:
                print("登錄失敗！")
        elif cmd == 3:
            s.send(b"E")
            sys.exit("謝謝使用！")

def do_register(s):
    while True:
        name = input("用戶名：")
        passwd = getpass.getpass("密 碼：")
        passwd1 = getpass.getpass("確認密碼：")

        if (' ' in name) or (' ' in passwd):
            print("用戶名及密碼不允許為空格：")
            continue
        if passwd != passwd1:
            print("兩次密碼不一致！")
            continue

        msg = "R {} {}".format(name,passwd)
        #發送請求
        s.send(msg.encode())
        #接收回復
        data = s.recv(128).decode()

        if data == "OK":
            return name
        elif data == 'EXISTS':
            print("該用戶已存在！")
            return 1
        else:
            return 1
def do_login(s):
    name = input("用戶名：")
    passwd = getpass.getpass("密 碼：")
    msg = "L {} {}".format(name,passwd)
    s.send(msg.encode())
    data = s.recv(128).decode()

    if data == 'OK':
        return name
    else:
        print(data)
        return 1

def login(s,name):
    while True:
        print('''\n
            ===========查詢介面============
            1.查詞     2.歷史紀錄   3.註銷
            =============================
            ''')
        try:
            cmd = int(input("輸入選項>>"))
        except Exception:
            print("命令錯誤！")
            continue
        if cmd not in [1,2,3]:
            print("對不起，沒有該命令！")
            sys.stdin.flush() #清除輸入
            continue 
        elif cmd == 1:
            do_query(s,name)
        elif cmd == 2:
            do_history(s,name)
        elif cmd == 3:
            return

def do_query(s,name):
    while True:
        word = input("單 詞：")
        if word == "##":
            break 
        msg = "Q {} {}".format(name,word)
        s.send(msg.encode())
        data = s.recv(128).decode()
        if data == 'OK':
            data = s.recv(2048).decode()
            print(data)
        else:
            print(data)


def do_history(s,name):
    msg = "H {}".format(name)
    s.send(msg.encode())
    data = s.recv(128).decode()
    if data == 'OK':
        while True:
            data = s.recv(1024).decode()
            if data == "##":
                break
            print(data)
    else:
        print(data)


if __name__ == "__main__":
    main()
