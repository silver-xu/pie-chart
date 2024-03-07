
import pandas as pd  
import matplotlib.pyplot as plt 
import smtplib 
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import parsedate_tz, mktime_tz, formatdate

import requests
from datetime import datetime
import schedule


import download_from_url as dl_url
import transform_to_df as transform_df
import email_sent as email

temp_filename = 'fname.png'

url ='https://queenie-python-assignment.s3.ap-southeast-2.amazonaws.com/customers-100.csv'


def plot(df):     
     plt.pie(df['Total'],labels =df['Country'] )
     plt.savefig(temp_filename, bbox_inches='tight')

def email_body(df):
    df2=df[:5]
    result = ""
    for i in  range(len(df2)) : 
        result += "{}.{} has {} customers\r\n".format(i+1,df2['Country'][i],df2['Total'][i]) 
    return "Here are the top 5 countries with large number of  customers: \r\n" + result 




 



# for i in range(urls):
#     url = urls[i]

#     tokens = url.split("/")
#     filename = tokens[len(tokens) - 1]
#     content = download_from_url(url, )
#     df = transform(content)
#     filename = plot(df)

#     send_email("subject", "body", filename)


  

file=dl_url.download_from_url(url)
df=transform_df.transform(file)
fname=plot(df)
body=email_body(df)
email.send_email("Greeting",body,temp_filename)
  
