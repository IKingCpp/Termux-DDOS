import time
import os

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

host = input("[*]\033[01;31mIP OR HOSTNAME :\033[01;37m ")
port = input("[*]\033[01;31mPORT : \033[01;37m ")

print("[*]\033[01;31mAttacking : \033[01;37m", host, " ")
time.sleep(2)
print("[*]\033[01;31mERROR")
