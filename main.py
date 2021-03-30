import schedule
import os
import time
import requests
from smtplib import SMTP

# Tg function


def telegram_bot_sendtext(bot_message):

    bot_token = os.environ.get("BOT_TOKEN", "")
    bot_chatID = os.environ.get("CHAT_ID", "")
    send_text = 'https://api.telegram.org/bot' + bot_token + \
        '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

# Mail function


def sendmail():
    with SMTP("smtp.mail.yahoo.com", 587) as connection:
        msg = 'Its been 10 days now, i think you should call me.'
        pswrd = os.environ.get("YAHOO_PSWRD", "")
        connection.starttls()
        connection.login("callgrandma@yahoo.com", pswrd)
        connection.sendmail("callgrandma@yahoo.com", "anshumanpathak4@gmail.com",
                            "Subject:CALL ME!!\n\n"+msg)
        telegram_bot_sendtext(msg)
        connection.quit()


# Cron job for sending email every 10 days

schedule.every(10).days.do(sendmail)
while 1:
    schedule.run_pending()
    time.sleep(1)
