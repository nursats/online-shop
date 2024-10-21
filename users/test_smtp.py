import smtplib

def test_smtp_connection():
    try:
        server = smtplib.SMTP_SSL('smtp.yandex.com', 465)
        server.login('seitovnursat@yandex.kz', 'mhzdbuceusrxmomq')
        print("Connection to SMTP server successful!")
        server.quit()
    except Exception as e:
        print(f"Failed to connect to SMTP server: {e}")

if __name__ == "__main__":
    test_smtp_connection()
