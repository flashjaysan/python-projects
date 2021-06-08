import smtplib


class BirthdayEmailSender:

    def __init__(self):
        self.sender_email = 'sender@gmail.com'
        self.receiver_email = 'receiver@gmail.com'
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=self.sender_email, password='XXXXXXXX')
            connection.sendmail(from_addr=self.sender_email, to_addrs=self.receiver_email, msg='Subject:Title\n\nMessage')


if __name__ == '__main__':
    BirthdayEmailSender()
