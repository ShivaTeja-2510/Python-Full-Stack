import smtplib
from email.message import EmailMessage

# email details
sendermailid="www.shivateja11@gmail.com"
receivermailid="varunrajvarakala16@gmail.com"
apppassword="gccj zbxt zynu revv"

# email content
subject = "Birthday Invitation on 25th October 2026"
body = '''
Good Morning,
I hope you are doing well,
I would hearty like to invite you to my birthday,
You should attend the birthday party without fail,
while coming to my birthday, don't forget to bring my gift worth atleast 10000

Thanks and regards
Shiva
'''
msg = EmailMessage()
msg['Subject'] = subject
msg['From'] = sendermailid
msg['To'] = receivermailid
msg.set_content(body)
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sendermailid,apppassword)
        smtp.send_message(msg)
        print("Email has been sent sucessfully")
except Exception as e:
    print("Exception is:",e)