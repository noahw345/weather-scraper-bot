from bs4 import BeautifulSoup
import requests
import smtplib
import ssl

#scraping HTML of weather page
page = requests.get("https://forecast.weather.gov/MapClick.php?lat=42.9334&lon=-72.2806#.XsMCQi-ZNQI")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]

#finding current report
period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()
img = tonight.find("img") 
desc = img['title']

#email constants
sender_email = "noahemailbot@gmail.com"  
receiver_email = sender_email
sender_password = "enter password here"
message = str(desc)

print(message)

port = 465

#establishing ssl context
context = ssl.create_default_context()

print("Starting to send")

#loging in and sending email
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, message)

print("Email sent")




