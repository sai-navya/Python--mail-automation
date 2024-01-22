
import smtplib
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

#Next login into server
server.login("navyatadisetti99@gmail.com","Daddy665")
#Send the mail
msg = "Hello! My First mail using python"
server.sendmail("navyatadisetti99@gmail.com","navyyasrinivas67@gmail.com",msg)
