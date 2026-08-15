from datetime import datetime
import pandas
import random
import smtplib
import os
from urllib.parse import quote


MY_EMAIL = os.environ["MY_EMAIL"]
MY_PASSWORD = os.environ["MY_PASSWORD"]


today = datetime.now()

today_tuple = (
    today.month,
    today.day
)


data = pandas.read_csv(
    "birthdays.csv"
)


for (index, data_row) in data.iterrows():

    birthday = (
        data_row["month"],
        data_row["day"]
    )


    if birthday == today_tuple:

        birthday_person = data_row


        file_path = (
            f"letter_templates/"
            f"letter_{random.randint(1,3)}.txt"
        )


        with open(file_path) as letter_file:

            contents = letter_file.read()


        contents = contents.replace(
            "[NAME]",
            birthday_person["name"]
        )


        birthday_link = (
            "https://muhammadgulsher11.github.io/"
            "birthday-wisher/?name="
            + quote(str(birthday_person["name"]))
        )


        message = f"""Subject: Happy Birthday! 🎂

{contents}

🎁 I have a special surprise for you!

Open your birthday surprise:

{birthday_link}

🎂 🎉 🎈
"""


        with smtplib.SMTP(
            "smtp.gmail.com",
            587
        ) as connection:

            connection.starttls()


            connection.login(
                MY_EMAIL,
                MY_PASSWORD
            )


       connection.sendmail(
    from_addr=MY_EMAIL,
    to_addrs=birthday_person["email"],
    msg=f"Subject:Happy Birthday!\n\n{contents}".encode("utf-8")
)

        print(
            f"Birthday email sent to "
            f"{birthday_person['name']}!"
        )


print("Finished!")
