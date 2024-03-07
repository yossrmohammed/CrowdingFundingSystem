import json
import os.path
import validations


class Project:
    def __init__(self, title, details, totalTarget, startDate, endDate, email):
        self.title = title
        self.details = details
        self.totalTarget = totalTarget
        self.startDate = startDate
        self.endtDate = endDate
        self.email = email


def addProject(email):
    title = input("Enter Title: ")
    if not validations.validateStrings(title):
        print("Title cannot be empty.")
        return
    if validations.titleExist(title):
        print("Title is exist")
        return
    details = input("Enter Details: ")
    if not validations.validateStrings(details):
        print("details cannot be empty.")
        return
    totalTarget = input("Enter Total target")
    try:
        totalTarget = int(totalTarget)
    except ValueError:
        print("Total target must be an integer.")
        return
    startDate = input("Enter start Date format: YYYY-MM-DD \n")
    if not startDate or not validations.validateDate(startDate):
        print("Invalid start date format. Please use YYYY-MM-DD.")
        return

    endDate = input("Enter end Date format: YYYY-MM-DD \n")
    if not startDate or not validations.validateDate(startDate):
        print("Invalid end date format. Please use YYYY-MM-DD.")
        return
    if endDate <= startDate:
        print("End date must be after start date.")
        return
    newProject = Project(title, details, totalTarget, startDate, endDate, email)
    projectData = {
        "title": newProject.title,
        "details": newProject.details,
        "totalTarget": newProject.totalTarget,
        "startDate": newProject.startDate,
        "endDate": newProject.endtDate,
        "email": newProject.email,
    }
    file_path = "projectsData.json"
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
    else:
        data = {"projectsData": []}

    data["projectsData"].append(projectData)

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


def getAll():
    if not os.path.exists("projectsData.json"):
        print("JSON file does not exist.")
        return
    with open("projectsData.json", "r") as f:
        data = json.load(f)
        for project in data["projectsData"]:
            print("Title:", project["title"])
            print("Details:", project["details"])
            print("Total Target:", project["totalTarget"])
            print("Start Date:", project["startDate"])
            print("End Date:", project["endDate"])
            print("Email:", project["email"])
            print()


def editProject(email):
    title = input("Enter Title of project: ")
    file_path = "projectsData.json"
    with open(file_path, "r") as f:
        data = json.load(f)
    for project in data["projectsData"]:
        if project["title"] == title and project["email"] == email:
            print(
                "1. Title \n2. Details \n3. Total target \n4. Start date \n5. End date"
            )
            choice = input("Enter your choice: ")
            try:
                if choice == "1":
                    newUpdate = input("Enter new Title: ")
                    project["title"] = newUpdate
                elif choice == "2":
                    newUpdate = input("Enter Details: ")
                    project["details"] = newUpdate
                elif choice == "3":
                    newUpdate = input("Enter Total target: ")
                    project["totalTarget"] = newUpdate
                elif choice == "4":
                    newUpdate = input("Enter Start date: ")
                    project["startDate"] = newUpdate
                elif choice == "5":
                    newUpdate = input("Enter End date: ")
                    project["endDate"] = newUpdate
                else:
                    print("Invalid choice.")
            except Exception as e:
                print(f"An error occurred: {e}")
            else:
                with open(file_path, "w") as f:
                    json.dump(data, f, indent=4)
                print("Project updated successfully!")
            break
    else:
        print("Project not found")


def deleteProject(email):
    title = input("Enter Title of project to delete: ")
    file_path = "projectsData.json"
    if not os.path.exists(file_path):
        print("No projects exist")
        return
    with open(file_path, "r") as f:
        data = json.load(f)
    for project in data["projectsData"]:
        if project["title"] == title and project["email"] == email:
            data["projectsData"].remove(project)
            print("Project deleted successfully!")
            break
    else:
        print("Project not found.")
        return
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
