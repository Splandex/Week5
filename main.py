import requests
import json

url = "https://michaelgathara.com/api/python-challenge"

response = requests.get(url)

challenges = response.json()

print("Name: Alex Angle")
print("BlazerId: Splandex")
print(challenges)

# split = challenges.split("'problem'")

for problemData in challenges:
    problem = problemData["problem"][0: -1]
    if problem.find("+") != -1:
        split = problem.split("+")
        print(int(split[0]) + int(split[1]))
    elif problem.find("-") != -1:
        split = problem.split("-")
        print(int(split[0]) - int(split[1]))
    elif problem.find("*") != -1:
        split = problem.split("*")
        print(int(split[0]) * int(split[1]))
    elif problem.find("/") != -1:
        split = problem.split("/")
        print(int(split[0]) / int(split[1]))

