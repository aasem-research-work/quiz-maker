import requests

url = "https://raw.githubusercontent.com/aasem-research-work/quiz-maker/main/public/quiz01.json"

response = requests.get(url)
data = response.json()

# Save the JSON data to a local file
filename = "quiz01.json"
with open(filename, "w") as file:
    file.write(response.text)

print("File saved as", filename)
