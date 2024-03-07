import re
import json
import os
from datetime import datetime


def validateEmail(email):
    regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
    if re.fullmatch(regex, email):
        return True
    return False


def userExist(email):
    if os.path.exists("userData.json") and os.path.getsize("userData.json") > 0:
        with open("userData.json", "r") as file:
            try:
                data = json.load(file)
                users = data.get("userData", [])
                if users:
                    for user in users:
                        if user["email"] == email:
                            return True
            except json.JSONDecodeError as e:
                print(f"Error loading JSON: {e}")
    return False


def validatePhone(phone):
    egyptianPattern = r"^01[0125]\d{8}$"
    if re.match(egyptianPattern, phone):
        return True
    return False


def validateStrings(name):
    if not name or name[0].isdigit() or not re.match(r"^[a-zA-Z]+$", name):
        return False
    return True


def validatePassword(password):
    if len(password) < 8:
        return False, "Password must be more than 8 characters"
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter"
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter"
    if " " in password:
        return False, "Password cannot contain spaces"
    return True, ""


def validateDate(date_str):
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
        currentDate = datetime.now()
        return date > currentDate
    except ValueError:
        return False


def titleExist(title):
    if os.path.exists("projectsData.json"):
        with open("projectsData.json", "r") as file:
            data = json.load(file)
            for project in data["projectsData"]:
                if project["title"] == title:
                    return True
    return False
