from datetime import datetime
from zoneinfo import ZoneInfo
import pandas
import random
import smtplib
import os
from urllib.parse import quote
from email.message import EmailMessage


MY_EMAIL = os.environ["MY_EMAIL"]
MY_PASSWORD = os.environ["MY_PASSWORD"]


# Pakistan local time
today = datetime.now(ZoneInfo("Asia/Karachi"))

today_tuple = (
    today.month,
    today.day
)


data = pandas.read_csv("birthdays.csv")


for (index, data_row) in data.iterrows():

    birthday = (
        int(data_row["month"]),
        int(data_row["day"])
    )

    if birthday == today_tuple:

        birthday_person = data_row

        file_path = (
            f"letter_templates/"
            f"letter_{random.randint(1, 3)}.txt"
        )

        with open(
            file_path,
            encoding="utf-8"
        ) as letter_file:

            contents = letter_file.read()

        contents = contents.replace(
            "[NAME]",
            str(birthday_person["name"])
        )

        birthday_link = (
            "https://muhammadgulsher11.github.io/"
            "Automated-Birthday-Wisher/?name="
            + quote(str(birthday_person["name"]))
        )

        message_body = f"""
{contents}

🎁 I have a special surprise for you!

Open your birthday surprise:

{birthday_link}

🎂 🎉 🎈
"""

        message = EmailMessage()

        message["Subject"] = "🎉 Happy Birthday!"
        message["From"] = MY_EMAIL
        message["To"] = birthday_person["email"]

        message.set_content(message_body)

        with smtplib.SMTP(
            "smtp.gmail.com",
            587
        ) as connection:

            connection.starttls()

            connection.login(
                MY_EMAIL,
                MY_PASSWORD
            )

            connection.send_message(message)

        print(
            f"Birthday email sent to "
            f"{birthday_person['name']}!"
        )


print("Finished!")
