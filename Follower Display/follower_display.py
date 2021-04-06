# Tweepy is a Python library for accessing the Twitter API
import tweepy

# Using app keys and tokens from my developer app
auth = tweepy.OAuthHandler("I8du75AluHGuyepB7O14ZNJyu", "Jg0IN5JiAOt684Ust0rQ5nNhpJYUUoRy1iRfbCVYEjTYX0rQ7i")
auth.set_access_token("371302729-2qF49kYJRElsDGxXUH3mAZlJCRiuDEuNIeHnPrEY", "0Z5bvtg5ogPbfNrRyUDiBpfLZo8RwuNRvucXk9Ip0tToc")

api = tweepy.API(auth)

# Program asks for a Twitter username and prints the username as well as their follower count 
# to the terminal


userInput = input("\nPlease enter a Twitter username to see their follower count: ")
user = api.get_user(userInput)

print("\nUser: " + user.screen_name)
print(user.screen_name + " has " + str(user.followers_count) + " followers.")

input("\nPress enter to close program.")
