import smtplib


def sendEmail(subject: str, message: str, to: str):
    gmail_user = 'moneyndat2@gmail.com'
    gmail_password = 'storfedpik'

    sent_from = gmail_user
    # to = ['jufa2401@gmail.com']
    body = message + "\n\n- Bob from the HR Department"

    email_text = """
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from,to, subject, body)
    emailtext = "From:", sent_from, "To:", to, "Subject:", subject, body
    try:
        print("Trying sending message(s) to", str(to) + "...")
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        print(email_text)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print('Email sent!')
    except smtplib.SMTPException:
        print('Something went wrong...')


if __name__ == "__main__":
    sendEmail("lort", "hello you are fired", 'jufa2402@gmail.com')
