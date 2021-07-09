#coded by hasan (@hopeleskid2.0)
#speacial thanks to cyber jeevi
#modules Needed
from instabot import Bot
import requests
import time
import os
import sys
# define clear
def clear():
    if os.name == "at":
        os.system("cls")
    else:
        os.system("clear")
#define countdaown
def coundown(counter_time):
    while counter_time:
        mins, secs = divmod(counter_time, 60)
        timer = '{0.2d}:{0.2d}'.format(mins, secs)
        print("sleeping......." ,timer)
        time.sleep(1)
        counter_time -= 1
# banner
def banner():
    print('''
    .___  ________     _____         .__  .__       ___________    .__  .__                                     
    |   |/  _____/    /     \ _____  |  | |  |  __ _\_   _____/___ |  | |  |   ______  _  __ ___________  ______
    |   /   \  ___   /  \ /  \\__  \ |  | |  | |  |  \    __)/  _ \|  | |  |  /  _ \ \/ \/ // __ \_  __ \/  ___/
    |   \    \_\  \ /    Y    \/ __ \|  |_|  |_|  |  /     \(  <_> )  |_|  |_(  <_> )     /\  ___/|  | \/\___ \ 
    |___|\______  / \____|__  (____  /____/____/____/\___  / \____/|____/____/\____/ \/\_/  \___  >__|  /____  >
                \/          \/     \/                    \/                                     \/           \/


       created and devoloped by HASAN  @hopeleskid.20 (speacial thanks to cyberjeevi)
        ''')




          ## Instabot Module Vars
bot = Bot(
    max_follows_per_day=500,
    max_unfollows_per_day=500,
    follow_delay=10, #for Test
    unfollow_delay=10 #also Test
    )
# Define Follow Unfollow Bot
def ig_mallu_followers():
    userdata = input("target account")
    print ("Start Lines---------------------------")
    while True:
        try:
            bot.follow(userdata)
            print ("After Follow Breake Line---------------------------")
            countdown(144)
            bot.unfollow(userdata)
            print ("After Unfollow Brake-------------------------------")
            countdown(10)
            print ("After Count-------------------------------")
       except KeyboardInterrupt:
            break
    ig_mallu_followers() #for loop


#define Login
def Login():
    time.sleep(2)
    print ("Login Page")
    USERNAME = input("Input UserName:- ")
    PASSWORD = input("Password:- ")
    bot.login(username=USERNAME,password=PASSWORD)

#MULTIPPLE LOGINS

def InstaBot():
    os.system("rm -r config")
    banner()
    Login()
    ig_mallu_followers()
