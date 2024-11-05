import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, body, to_email):
    # اطلاعات ورود به حساب جیمیل
    from_email = "aradmirzaee12@gmail.com"
    password = "a13891226"

    # ایجاد پیام ایمیل
    msg = MIMEMultipart()
    msg['From'] = 'aradmirzaee12@gmail.com'
    msg['To'] = 'aradmirzaee12@gmail.com'
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # اتصال به سرور SMTP جیمیل و ارسال ایمیل
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.close()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# مثال استفاده
send_email("Subject of the Email", "Body of the Email", "recipient_email@gmail.com")
