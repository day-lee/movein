
import pandas
import datetime as dt
import random
import smtplib

PLACEHOLDER = "[NAME]"
sentby = "Dayeon"

now = dt.datetime.now()
now_month = now.month
now_day = now.day
today = (now_month, now_day)
print(today)

#fetch the data
df = pandas.read_csv("birthdays.csv")
birthday_df = df.to_dict(orient='records')
print(birthday_df)

for person in birthday_df:
    if today == (person['month'], person['day']):
        name = person['name']
print(name)
#random pick letter format

letter = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
picked_letter = random.choice(letter)
print(picked_letter)

#replace name on the txt.file
#can use comprehension
with open(f"letter_templates/{picked_letter}", "r") as letter:
    letter_template = letter.read()
    new_letter = letter_template.replace(PLACEHOLDER, name)

# you don't need this bits
# with open(f"letter_templates/Birthday_wish_to_{name}.txt", mode="w") as f_letter:
#     f_letter.write(new_letter)
#
# with open(f"letter_templates/Birthday_wish_to_{name}.txt", mode="r") as f:
#     content = f.read()

#send letter
my_email = "testpythondy@gmail.com"
my_password = "deleted"
yahoo_email = "testpythondy@yahoo.com"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=yahoo_email,
        msg=f"Subject: Happy Birthday\n\n {new_letter}".encode('utf-8'))

#HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
birthdays_dict = {
     (birthday_month, birthday_day): data_row
 }
#Dictionary comprehension template for pandas DataFrame looks like this:
# new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
#e.g. if the birthdays.csv looked like this:
# name,email,year,month,day
# Angela,angela@email.com,1995,12,24
#Then the birthdays_dict should look like this:# birthdays_dict = {
 #    (12, 24): Angela,angela@email.com,1995,12,24}

#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
 if (today_month, today_day) in birthdays_dict:

