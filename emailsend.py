import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd

# Email server configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_EMAIL = 'yamini582006@gmail.com'
SENDER_PASSWORD = 'qemg fgtb lxzz ixbg'

TRACKING_URL = 'https://f19e-2405-201-e006-1075-f99e-7f9d-ccc2-cb66.ngrok-free.app/track-click?email='

recipients = pd.read_csv('email_list.csv')

def send_emails():
    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)

        for _, row in recipients.iterrows():
            recipient_email = row['Email']
            recipient_name = row['Name']  # Read the name from the CSV
            tracking_link = TRACKING_URL + recipient_email 

            subject = "Important: Payroll Account Update Required"
            body_html = f"""
            <html>
            <body>
                <p>Dear {recipient_name},</p>

                <p>Our finance team has identified discrepancies in the payroll system related to employee bank account details. 
                To avoid any delays in your upcoming salary payment, we require you to confirm and update your account information immediately.</p>

                <p>Please click the link below to access the payroll portal:</p>

                <p><a href="{tracking_link}" style="color: blue; text-decoration: underline;">Update Bank Details Here</a></p>

                <p>Ensure this is completed as soon as possible to avoid interruptions.</p>

                <p>Best regards,<br>
                [CFO Name]<br>
                Chief Financial Officer<br>
                TVS Mobility</p>
            </body>
            </html>
            """

            msg = MIMEMultipart()
            msg['From'] = SENDER_EMAIL
            msg['To'] = recipient_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body_html, 'html'))  # Send as HTML

            server.send_message(msg)
            print(f"Email sent to {recipient_email}")

        server.quit()
        print("All emails sent successfully.")

    except Exception as e:
        print(f"Error: {e}")


send_emails()
