import requests


parameters = {
    "name": "jack",
}
response_gender = requests.get(url="https://api.genderize.io", params=parameters)
response_gender.raise_for_status()


gender_data = response_gender.json()
gender = gender_data['gender']
print(gender)




parameters = {
    "name": "jack",
}
response_age = requests.get(url="https://api.agify.io", params=parameters)
response_age.raise_for_status()

age_data = response_age.json()

age = age_data['age']
count = age_data['count']
