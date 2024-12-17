import smtplib

# Email details
sender_email = "smartshop.3765@gmail.com"
recipient_email = "shravelrishyan@gmail.com"
subject = "Test Email from Raspberry Pi"
body = "This is a test email sent from a Raspberry Pi."

# SMTP server configuration (for Gmail)
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "smartshop.3765@gmail.com"
smtp_password = "gzumvlddihunutku"  # Replace this with the 16-character App Password

# Send the email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(sender_email, recipient_email, f"Subject: {subject}\n\n{body}")
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
finally:
    if 'server' in locals():
        server.quit()
