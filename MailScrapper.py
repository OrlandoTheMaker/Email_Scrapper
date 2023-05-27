import requests
from bs4 import BeautifulSoup
import re

url = input("Enter Your Site Here: ") # replace with the URL of the website you want to scrape
http_url = "https"+url
# make a GET request to the website
response = requests.get(http_url)

# parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# find all the links on the website
links = []
for link in soup.find_all("a"):
    href = link.get("href")
    if href:
        links.append(href)

# find all the email addresses on the website
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", str(soup))

# print the links and email addresses
print("Links:")
for link in links:
    print(link)

print("Emails:")
for email in emails:
    print(email)
