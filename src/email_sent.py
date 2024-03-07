from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import smtplib 
 


def send_email(subject,body, filename):
    msg = MIMEMultipart()
    date = datetime.today()
    msg['Subject'] = subject+ date.strftime('%Y-%m-%d')
    msg['From'] = 'silver.qing@outlook.com'
    msg['To'] = 'me@silverxu.au'
    msg.attach(MIMEText(body))

    with open(filename,'rb') as file:
        att = MIMEApplication(file.read(),_subtype="png")
        att.add_header('Content-Disposition','attachment',filename=filename)
        msg.attach(att)     

    smtp_client = smtplib.SMTP('smtp.outlook.com')
    smtp_client.starttls()
    smtp_client.login('silver.qing@outlook.com','Goldenstate624.')
    smtp_client.sendmail('silver.qing@outlook.com',['me@silverxu.au'], msg.as_string())
    smtp_client.quit()

    return  