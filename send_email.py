# standar email library
import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "hajni0490@gmail.com"
password = "clzxvutfncelnbpy"

receiver = "hajni0490@gmail.com"
# to send emails securely
context = ssl.create_default_context()

# subject should be in first line
message = """\
Subject: Hi!
Hi there
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)