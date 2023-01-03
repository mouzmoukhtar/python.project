import re
import os
from datetime import date
 
def displaymainMenu():
    choice = input(
        "Please Enter Your Choice:\nC: To Create a project\nD: To Display All Projects\nE: To Edit Project\nX: To Delete Project\nQ: To Exit\n"
    )

    if choice == "C" or choice == "c":
      create()
    elif choice == "D" or choice == "d":
        allprojects = displayAllprojects()
        print("Title:Details:Total Target:Start date:End Date")
        for pro in allprojects:
            projectInfo = pro.strip("\n")
            projectInfo = projectInfo.split(":")
            print(f"{projectInfo[0]}:{projectInfo[1]}:{projectInfo[2]}:{projectInfo[3]}:{projectInfo[4]}")
        print("*" * 25)
        displaymainMenu()

    elif choice == "E" or choice == "e":
        editpro()
    elif choice == "X" or choice == "x":
        deletepro()
    elif choice == "Q" or choice == "q":
        exit()
    else:
        print("Wrong Choice")
        displaymainMenu()


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
            Total_target = input("Enter Total Target Of Project:\n")
            if Total_target != "":
                 break
        while True:
            date_components = input('Enter Project start date formatted as YYYY-MM-DD: ').split('-')
            print(date_components)
            year, month, day = [int(item) for item in date_components]
            Start_date = date(year, month, day)
            if Start_date !="":
                break
        while True:
            date_components = input('Enter Project end date formatted as YYYY-MM-DD: ').split('-')
            print(date_components)
            year, month, day = [int(item) for item in date_components]
            End_date = date(year, month, day)
            if End_date != "":
                break
        projectInfo = f"{Title}:{Details}:{Total_target}:{Start_date}:{End_date}\n"
        fileObj.write(projectInfo)
        fileObj.close()
        print("Registered Successfully")
        print("*" * 25)
        displaymainMenu()

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
    deletepro_title = input("Please Enter The Title of The Project You Want to Delete:\n")
    for pro in allprojects:
        projectInfo = pro.strip("\n")
        projectInfo = projectInfo.split(":")
        if projectInfo[0] == deletepro_title:
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
        displaymainMenu()


def editpro():
    os.system("clear")
    allprojects = displayAllprojects()
    editpro_title = input("Please Enter The Title of The Project You Want to Edit:\n")
    for pro in allprojects:
        projectInfo = pro.strip("\n")
        projectInfo = projectInfo.split(":")
        if projectInfo[0] == editpro_title:
            choice = input(
                "Please Enter Your Choice:\nT: To Edit project Title\nD: To Edit Project Details\nG: To Edit Total Target\nS: To Edit Project start date\nE: To Edit project end date\nA: To Edit All Projects\n"
            )
            if choice == "T" or choice == "t":
                Title = input("Enter Title Of Project:\n")
                projectInfo[0] = Title
            elif choice == "D" or choice == "d":
                Details = input("Enter Details Of Project\n")
                projectInfo[1] = Details
            elif choice == "E" or choice == "g":
                Total_target = input("Enter Total Target Of Project:\n")
                projectInfo[2] = Total_target
            elif choice == "P" or choice == "s":
                date_components = input('Enter Project start date formatted as YYYY-MM-DD: ').split('-')
                print(date_components)
                year, month, day = [int(item) for item in date_components]
                Start_date = date(year, month, day)
                projectInfo[3] = Start_date
            elif choice == "A" or choice == "e":
                date_components = input('Enter Project end date formatted as YYYY-MM-DD: ').split('-')
                print(date_components)
                year, month, day = [int(item) for item in date_components]
                End_date = date(year, month, day)
                projectInfo[4] = End_date
            elif choice == "A" or choice =="a":  
                Title = input("Enter Title Of Project:\n")
                projectInfo[0] = Title
                Details = input("Enter Details Of Project\n")
                projectInfo[1] = Details
                Total_target = input("Enter Total Target Of Project:\n")
                projectInfo[2] = Total_target
                date_components = input('Enter Project start date formatted as YYYY-MM-DD: ').split('-')
                print(date_components)
                year, month, day = [int(item) for item in date_components]
                Start_date = date(year, month, day)
                projectInfo[3] = Start_date
                date_components = input('Enter Project end date formatted as YYYY-MM-DD: ').split('-')
                print(date_components)
                year, month, day = [int(item) for item in date_components]
                End_date = date(year, month, day)
                projectInfo[4] = End_date  
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

    displaymainMenu()


displaymainMenu()


