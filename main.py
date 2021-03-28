import schedule
import time
from smtplib import SMTP

# Mail function


def sendmail():
    with SMTP("smtp.mail.yahoo.com", 587) as connection:
        connection.starttls()
        connection.login("callgrandma@yahoo.com", "axeykttuiihpzjdh")
        connection.sendmail("callgrandma@yahoo.com", "anshumanpathak4@gmail.com",
                            "Subject:CALL ME!!\n\nIts been 10 days now, i think you should call me.")
        connection.quit()


# Cron job for sending email every 10 days

schedule.every(10).days.do(sendmail)
while 1:
    schedule.run_pending()
    time.sleep(1)
