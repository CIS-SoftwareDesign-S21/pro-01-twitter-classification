# Tweepy is a Python library for accessing the Twitter API
import tweepy

# reportlab is for making pdf
import reportlab
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
# Using app keys and tokens from my developer app
auth = tweepy.OAuthHandler("I8du75AluHGuyepB7O14ZNJyu", "Jg0IN5JiAOt684Ust0rQ5nNhpJYUUoRy1iRfbCVYEjTYX0rQ7i")
auth.set_access_token("371302729-2qF49kYJRElsDGxXUH3mAZlJCRiuDEuNIeHnPrEY", "0Z5bvtg5ogPbfNrRyUDiBpfLZo8RwuNRvucXk9Ip0tToc")

api = tweepy.API(auth)

# Program asks for a Twitter username and prints the username as well as their follower count 
# to the terminal

def print_pdf(user):
    doc = SimpleDocTemplate("UTC_print.pdf")
    styles = getSampleStyleSheet()
    style = styles['Normal']
    output = []
    output.append(Paragraph("Username: "+ str(user.name)))
    output.append(Paragraph("Description: "+ str(user.description)))
    doc.build(output)

userInput = input("\nPlease enter a Twitter username: ")
user = api.get_user(userInput)

print (user)

if_print = input("\nDo you want to print?(Y/N)")
if (if_print=="Y"):
    print_pdf(user)

