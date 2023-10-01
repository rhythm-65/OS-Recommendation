# Import the OS module
import os

# Define a dictionary of questions and features
questions = {
    "Do you prefer a user-friendly interface?": "user-friendly interface",
    "Do you need customizability?": "customizability",
    "Do you prioritize stability?": "stability",
    "Do you need compatibility with a wide range of software?": "compatibility",
    "Do you prefer open-source software?": "open-source software",
    "Do you need support for gaming?": "gaming support",
    "Do you prioritize security?": "security",
    "Do you need support for touchscreens?": "touchscreen support",
    "Do you prefer a lightweight OS?": "lightweight",
    "Do you need support for virtualization?": "virtualization support"
}

# Define a dictionary to map features to OSes
os_map = {
    "Windows": 0,
    "Linux": 0,
    "macOS": 0
}

# Ask the user 10 questions and update the OS map accordingly
for question, feature in questions.items():
    print(question)
    answer = input().lower()
    if answer == "yes":
        os_map["Windows"] += 1 if feature == "user-friendly interface" else 0
        os_map["Linux"] += 1 if feature == "customizability" or feature == "open-source software" else 0
        os_map["macOS"] += 1 if feature == "stability" or feature == "security" else 0
    elif answer == "no":
        os_map["Windows"] += 0 if feature == "user-friendly interface" else 1
        os_map["Linux"] += 0 if feature == "customizability" or feature == "open-source software" else 1
        os_map["macOS"] += 0 if feature == "stability" or feature == "security" else 1

# Check which OS has the highest score
recommended_os = max(os_map, key=os_map.get)

# Print the recommended OS
print("Based on your answers, we recommend using", recommended_os + ".")