import smtplib

class Mailer:
    # Enable google 2 factor authentication, or 2 step verification or whatever its called
    # After that you can create passwords for different things -> Just google "google app password"
    # email generated password: boniyauzuhxoedqj
    def send_mail(self, title, price, url):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login('panagiwtis.mitseas@gmail.com', 'boniyauzuhxoedqj') # If hadn't generated the email password described above, I would have to pass the actual email password

        subject = f'Product update'
        body = f'Title: {title}\n\nCurrent price: {price} GBP\n\nURL: {url}'
        message = f'Subject: {subject}\n\n{body}'

        server.sendmail(
            'panagiwtis.mitseas@gmail.com',
            'panagiwtis.mitseas@gmail.com',
            message
        )

        print('Email has been sent !!!')

        server.quit()

