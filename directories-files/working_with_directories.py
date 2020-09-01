#!/usr/bin/env python3.8

import os # this module helps with delete,rename,move directory and much more
          #whid module provides a layer of abstraction Python and the OS
          #the scrip can run in any OS supported by Python but we need pay atencion
          #to the path that can be different across different operanting systems
          # as windowns cd ~\users..... linux cd ~/users... (one use \ other use /)
          #when using absolute path in our code we nned to make sure we can provide
          #alternatives  for the pçlataforms we want to support

def create():
    directory_name = input("\nType the directory name:")
    if os.path.exists(directory_name):#if directory exists the funcition will return True
        print("\ndirectory already exists")
        main()
    else:
        os.mkdir(directory_name)#create a new directory
        print("\nThe directory {} was created\n".format(directory_name))


def delete():
    delete = input("\nWant delete the directory?(y/n): ")
    if delete =="y":
        try:
            dir = input("\nType directory name: ")
            os.rmdir(dir)#this function will only work if the directory is empty
            print("\nThe directory was deleted")
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

            main()

def rename():
    ask = input("\nWant rename the directory?(y/n): ")
    if ask =="y":
        try:
            name = input("\nType the directory name: ")
            rename = input("\nType the new directory name: ")
            os.rename(name, rename)#function will rename the directory
            print("\nThe directory was renamed by {}".format(rename))
        except:
            print("\ndirectory dele_me was not renamed")
            main()

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
        main()



def main():

    while True:

        choose = input(
        "\nType 1 for create a directory\n"
        "\nType 2 to delete the directory\n"
        "\nType 3 to rename the directory\n"
        "\nType 4 for check directory info\n"
        "\nType 5 for to exit\n"
        "\n"
        )
        try:
            choose = int(choose)
        except:
            choose = -1

        if choose == 1:
            create()

        elif choose == 2:
            delete()

        elif choose == 3:
            rename()
        elif choose == 4:
            info_directory()
        elif choose == 5:
            quit()
        else:
            print("Not a number")


main()
