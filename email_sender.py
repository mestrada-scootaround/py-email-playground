import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = "M E"
email['to'] = '' # email here
email['subject'] = "You won 1,000,000 dollars!"

email.set_content(html.substitute({'name': "ME"}), 'html') # or email.set_content(html.substitute(name="ME"))

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('', '') ## NOTE: found in App Password -> params: email and email's app password
  smtp.send_message(email)
  print('all good boss!')