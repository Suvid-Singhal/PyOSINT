import bs4
from requests import get

print("******************")
print("Welcome to PyOSINT")
print("******************\n")
print("Search if a user is present on Facebook, Instagram or Quora!\n")
username = input("Enter the username (Spaces will be replaced by dashes): ")
username = username.replace(' ', '-')
fb_url = "https://www.facebook.com/"+username
insta_url = "https://www.instagram.com/"+username
quora_url = "https://www.quora.com/profile/"+username

fb_response = get(fb_url)
if fb_response.status_code == 200:
    print("User is present on Facebook")

insta_response = get(insta_url)
if insta_response.status_code == 200:
    print("User is present on Instagram")
 
quora_response = get(quora_url)
if quora_response.status_code == 200:
    print("User is present on Quora")
