import re
import os
from datetime import date
 

def displayMainMenu():
    choice = input("Please Enter Your Choice:\nR: To Register\nL: To Login\n")
    if choice == "R" or choice == "r":
        register()
    elif choice == "L" or choice == "l":
        login()
    else:
        print("Wrong Choice")
        displayMainMenu()


def register():
    global email
    os.system("clear")
    try:
        fileObj = open("users.txt", "a")
    except Exception as e:
        print(e)
    else:
        while True:
            fName = input("Please Enter Your First Name:\n")
            if fName != "":
                break
        while True:
            lName = input("Please Enter Your Last Name:\n")
            if lName != "":
                break
        while True:
            email = input("Please Enter Your Email:\n")
            if re.match(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", email):
                break
        while True:
            password = input("Please Enter Your Password:\n")
            if password != "":
                break
        userInfo = f"{fName}:{lName}:{email}:{password}\n"
        fileObj.write(userInfo)
        fileObj.close()
        print("Registered Successfully")
        print("*" * 25)
        displayMainMenu()


def login():
    global email
    os.system("clear")
    try:
        fileObj = open("users.txt", "r")
    except Exception as e:
        print(e)
    else:
        email = input("Please Enter Your Email:\n")
        password = input("Please Enter Your Password:\n")
        allUsers = fileObj.readlines()
        for user in allUsers:
            userInfo = user.strip("\n")
            userInfo = userInfo.split(":")
            if userInfo[2] == email and userInfo[3] == password:
                print("Logged in Successfully")
                print("*" * 25)
                displaymain1Menu()
                break
        print("Unknown User")
        displayMainMenu
     
def displaymain1Menu():

    choice = input(
        "Please Enter Your Choice:\nC: To Create a project\nD: To Display All Projects\nE: To Edit Project\nX: To Delete Project\nQ: To Exit\n"
    )

    if choice == "C" or choice == "c":
        create()
    elif choice == "D" or choice == "d":
        allprojects = displayAllprojects()
        print("Email:Title:Details:Total Target:Start date:End Date")
        for pro in allprojects:
            projectInfo = pro.strip("\n")
            projectInfo = projectInfo.split(":")
            print(f"{projectInfo[0]}:{projectInfo[1]}:{projectInfo[2]}:{projectInfo[3]}:{projectInfo[4]}:{projectInfo[5]}")
        print("*" * 25)
        displaymain1Menu()

    elif choice == "E" or choice == "e":
        editpro()
    elif choice == "X" or choice == "x":
        deletepro()
    elif choice == "Q" or choice == "q":
        exit()
    else:
        print("Wrong Choice")
        displaymain1Menu()


def create():
    os.system("clear")
    try:
        fileObj = open("projects.txt", "a")
    except Exception as e:
        print(e)
    else:
        while True:
            Title = input("Enter Title Of Project:\n")
            if Title != "":
                break
        while True:
            Details = input("Enter Details Of Project:\n")
            if Details != "":
                break
        while True:
            try:
                Total_target =int (input ("Enter Total Target Of Project by egp:\n"))
                break
            except:
                print("Enter Total Target Of Project by egp")    
        while True:
            try:
                date_components = input('Enter Project start date formatted as YYYY-MM-DD: ').split('-')
                print(date_components)
                year, month, day = [int(item) for item in date_components]
                Start_date = date(year, month, day)
                break
            except:
                print("Enter Project start date formatted as YYYY-MM-DD")
        while True:
            try :
                date_components = input('Enter Project end date formatted as YYYY-MM-DD: ').split('-')
                print(date_components)
                year, month, day = [int(item) for item in date_components]
                End_date = date(year, month, day)

                break
            except:
                print("Enter end date formatted as YYYY-MM-DD")

        projectInfo = f"{email}:{Title}:{Details}:{Total_target}:{Start_date}:{End_date}\n"
        fileObj.write(projectInfo)
        fileObj.close()
        print("Registered Successfully")
        print("*" * 25)
        displaymain1Menu()

def displayAllprojects():
    os.system("clear")
    try:
        fileObj = open("projects.txt", "r")
    except Exception as e:
        print(e)
    else:
        allprojects = fileObj.readlines()
        return allprojects


def deletepro():
    os.system("clear")
    allprojects = displayAllprojects()
    deletepro_email = input("Please Enter The email of The Project You Want to Delete:\n")
    for pro in allprojects:
        projectInfo = pro.strip("\n")
        projectInfo = projectInfo.split(":")
        if projectInfo[0] == deletepro_email:
            print("project Deleted")
            print("*" * 25)
            allprojects.remove(pro)
            break
    else:
        print("Unknown project")
    try:
        fileObj = open("projects.txt", "w")
    except Exception as e:
        print(e)
    else:
        fileObj.writelines(allprojects)
        fileObj.close()
        displaymain1Menu()


def editpro():
    os.system("clear")
    allprojects = displayAllprojects()
    editpro_email = input("Please Enter The Email of The Project You Want to Edit:\n")
    for pro in allprojects:
        projectInfo = pro.strip("\n")
        projectInfo = projectInfo.split(":")
        if projectInfo[0] == editpro_email:
            choice = input(
                "Please Enter Your Choice:\nT: To Edit project Title\nD: To Edit Project Details\nG: To Edit Total Target\nS: To Edit Project start date\nE: To Edit project end date\nA: To Edit All Projects\n"
            )
            if choice == "T" or choice == "t":
                while True:
                    Title = input("Enter Title Of Project:\n")
                    if Title != "":
                        break
                projectInfo[1] = Title
            elif choice == "D" or choice == "d":
                 while True:
                    Details = input("Enter Details Of Project:\n")
                    if Details != "":
                        break
                 projectInfo[2] = Details
                
            elif choice == "G" or choice == "g":
                 while True:
                    try:
                        Total_target =int (input ("Enter Total Target Of Project by egp:\n"))
                        break
                    except:
                        print("Enter Total Target Of Project by egp")    
                 projectInfo[3] = Total_target
            elif choice == "S" or choice == "s":
                while True:
                    try:
                        date_components = input('Enter Project start date formatted as YYYY-MM-DD: ').split('-')
                        print(date_components)
                        year, month, day = [int(item) for item in date_components]
                        Start_date = date(year, month, day)
                        projectInfo[4] = Start_date
                        break
                    except:
                        print("Enter Project start date formatted as YYYY-MM-DD")
            elif choice == "E" or choice == "e":
                while True :
                    try:
                        date_components = input('Enter Project end date formatted as YYYY-MM-DD: ').split('-')
                        print(date_components)
                        year, month, day = [int(item) for item in date_components]
                        End_date = date(year, month, day)
                        projectInfo[5] = End_date
                        break
                    except:
                        print("Enter Project end date formatted as YYYY-MM-DD")
            elif choice == "A" or choice =="a":  
                Title = input("Enter Title Of Project:\n")
                projectInfo[1] = Title
                Details = input("Enter Details Of Project\n")
                projectInfo[2] = Details
                while True:
                        try:
                            Total_target =int (input ("Enter Total Target Of Project by egp:\n"))
                            break
                        except:
                            print("Enter Total Target Of Project by egp")    
                projectInfo[3] = Total_target
                while True:
                    try:
                        date_components = input('Enter Project start date formatted as YYYY-MM-DD: ').split('-')
                        print(date_components)
                        year, month, day = [int(item) for item in date_components]
                        Start_date = date(year, month, day)
                        break
                    except: 
                        print("Enter Project start date formatted as YYYY-MM-DD")
                projectInfo[4] = Start_date
                while True:
                    try:
                        date_components = input('Enter Project end date formatted as YYYY-MM-DD: ').split('-')
                        print(date_components)
                        year, month, day = [int(item) for item in date_components]
                        End_date = date(year, month, day)
                        break
                    except:
                        print("Enter Project end date formatted as YYYY-MM-DD")
                projectInfo[5] = End_date  
            updatedpro = ":".join(str(v) for v in projectInfo)
            updatedpro = f"{updatedpro}\n"
            proIndex = allprojects.index(pro)
            allprojects[proIndex] = updatedpro
            break
    else:
        print("Unknown project")
    try:
        fileObj = open("projects.txt", "w")
    except Exception as e:
        print(e)
    else:
        fileObj.writelines(allprojects)
        fileObj.close()

    displaymain1Menu()


displayMainMenu()     
