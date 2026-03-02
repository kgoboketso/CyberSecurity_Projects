#Password-strength-checker

#Generate a randowm number between 1 and 10
import re

from datetime import datetime

banned_passwords = [
    "password",
    "123456",
    "12345678",
    "qwerty",
    "admin",
    "letmein",
    "welcome"
]

def longresults (strength): 
  timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  with open("password_results.txt", "a") as file:
      file.write(f"{timestamp} - Password strength: {strength}\n")

def password_checker(password):
    score = 0
    feedback = [] 

    if len(password)>= 8:
        score +=1 
    else :
        feedback.append("Password should be at least 8 characters long.")
    
    if re.search(r'[A-Z]', password):
        score +=1
    else: 
        feedback.append("Password should contain at least one uppercase letter.")
   
    if re.search(r'[a-z]', password):
        score +=1   
    else:
        feedback.append("Password should contain at least one lowercase letter.")
    if re.search(r'[0-9]', password):
        score +=1               
    else:
        feedback.append("Password should contain at least one digit.")
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score +=1       
    else:
        feedback.append("Password should contain at least one special character.")
    
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    if password.lower() in banned_passwords:
        strength = "Weak"
        feedback.append("Password is too common and easily guessable.")
    
    return strength, feedback

password = input("Enter your password: ")
strength, feedback = password_checker(password)
print(f"Password strength: {strength}")
if feedback:
    print("Feedback:")
    for item in feedback:
        print(f"- {item}")
longresults(strength)

     
