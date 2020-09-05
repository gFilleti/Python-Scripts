#!/usr/bin/env python3.8
#!"C:\Python33\python.exe"

import os # this module helps with delete,rename,move directory and much more
          #whid module provides a layer of abstraction Python and the OS
          #the scrip can run in any OS supported by Python but we need pay atencion
          #to the path that can be different across different operanting systems
          # as windowns cd ~\users..... linux cd ~/users... (one use \ other use /)
          #when using absolute path in our code we nned to make sure we can provide
          #alternatives  for the pçlataforms we want to support
import pathlib


def create():
    ask = input(
    "For a single or a branch type 1\n"
    "For multiple chields directories type 2"
    )

    if ask == "1":

        directory_name = input("\nType the directory(ies) name(s):")

        if os.path.exists(directory_name):#if directory exists the funcition will return True
            print("\ndirectory already exists")
            refresh()
        else:
            pathlib.Path(directory_name).mkdir(parents=True, exist_ok=True)#create a new directory
            print("\nThe directory {} was created\n".format(directory_name))
            refresh()
    else:
        ask = input(
        "For enumereted in loop type 1\n"
        "For choose the names type 2\n"
        "type: "
        )

        if ask == "1":
            parents = input("How many parents? ")

            for p in range(1,int(parents)+1):
                parent = input("\nWhats {}º the parent name: ".format(p))
                pathlib.Path(parent).mkdir(parents=True, exist_ok=True)
                chields = input("\nHow many chield in parent{}? ".format(p))
                chield = input("\nWhats chields name: ")
                os.chdir(parent)
                for c in range(1,int(chields)+1):
                    pathlib.Path(chield+str(c)).mkdir(parents=True, exist_ok=True)
                os.chdir("..")
        refresh()





def delete():
    delete = input("\nWant delete the directory?(y/n): ")
    if delete =="y":
        try:
            dir = input("\nType directory name: ")
            os.rmdir(dir)#this function will only work if the directory is empty
            print("\nThe directory was deleted")
            refresh()
        except:

            dir_content = os.listdir(dir)
            if len(content) > 0:
                print("\nIts not possible delete the file with this methos because its not empty\n")
                for name in dir_content:
                    fullname = os.pathj.join(dir ,name)#permit to use this program independet the current Os
                    if os.path.isdir(fullname):
                        print("{} is a directory\n".format(fullname))
                    else:
                        print("{} is a file\n".format(fullname))
            else:
                print("Theres no directory to be deleted")

            refresh()

def rename():
    ask = input("\nWant rename the directory?(y/n): ")
    if ask =="y":
        try:
            name = input("\nType the directory name: ")
            rename = input("\nType the new directory name: ")
            os.rename(name, rename)#function will rename the directory
            print("\nThe directory was renamed by {}".format(rename))
            refresh()
        except:
            print("\ndirectory dele_me was not renamed")
            refresh()

def info_directory():
    try:
        name = input("\nType the directory name: ")
        size = os.path.getsize(name)#function return directory size
        timestamp = os.path.getmtime(name)#funcion return a Unix timestamp it represents the number of seconds since january 1st, 1970
        import datetime # this module has a function that makes timestamp more readable
        time = datetime.datetime.fromtimestamp(timestamp)
        print(
        "\nThe directory info is: \n"
        "size = {}\n"
        "timestamp = {}\n"
        "time = {}\n".format(size,timestamp,time)
        )
    except:
        print("\ndirectory doesnt exist")
        refresh()



def main():

    while True:
        try:
            where = input("Choose start directory: ")
            os.chdir(where)
        except:
            refresh()
        ask = input(
        "\nType 1 for create a directory\n"
        "\nType 2 to delete the directory\n"
        "\nType 3 to rename the directory\n"
        "\nType 4 for check directory info\n"
        "\nType 5 for to exit\n"
        "\n"
        "choose:"
        )
        try:
            ask = int(ask)
            choose(ask)
        except:
            refresh()


def choose(number):
    dict = {1: create, 2: delete, 3: rename, 4: info_directory}
    dict[number]()


def refresh():
    while True:
        escolha = input("\nPress Y to continue the script\n"
                            "Press anything else to exit:")

        if escolha.strip().lower() == "y":
            os.system('cls' if os.name == 'nt' else 'clear')
            main()

        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            quit()



main()
