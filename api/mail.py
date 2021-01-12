import smtplib


def sendemail(email, text):
    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.login("purplecakeboutique2020@gmail.com", "@zxc21sr92")
    subject = "Yeni sifaris var"
    message = 'Subject:{}\n\n{}'.format(subject, text)
    mail.sendmail("purplecakeboutique2020@gmail.com", email, message)
    mail.quit()

