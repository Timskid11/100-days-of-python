##################### Hard Starting Project ######################
import datetime as dt
import smtplib
import random
# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 
password = "xhrndhwtjozlfxqk"
# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
# HINT 1: Only the month and day matter.
month = now.month
day = now.day
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
import pandas
m_and_d = (month, day)
birthdays= pandas.read_csv('birthdays.csv')
birthdays_dict = {each_row['month'] : each_row['day'] for index,each_row in birthdays.iterrows()}


#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:
if m_and_d in birthdays_dict:
    birthday_person = birthdays_dict[m_and_d]
    file_path = f"./letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as f:
        content = f.read()
        content.replace("[NAME]",birthday_person["name"])
    connect = smtplib.SMTP('smtp-mail.outlook.com', 587)
    connect.starttls()
    connect.login(user='timilehinoyinlola3@gmail.com', password=password)
    connect.sendmail(from_addr='timilehinoyinlola3@gmail.com',to_addrs= oyinlolarobot@gmail.com,msg=f"Subject: Happy Birthday!!!\n\n{content}")
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



