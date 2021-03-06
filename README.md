# User Classification in Twitter (UCT)
### Group Members: Tarekegne Aboye, Yang Bo, Gannon Traynor, Soobin Kim, Keshav Saraogi

# Project Overview 
User accounts in Twitter can be categorized in many different ways. For example, whether they are humans or bots, individuals or organizations. The goal of this project is to create a program that can identify what type of user a Twitter account is based on different features, whether it's a bot, an advertisement page, a corporate/company page, a social media influencer/celebrity or just an everyday average joe. User Classification in Twitter is going to build upon a few older projects that had a similar idea. There are many research and open-source projects that attempted to achieve this task. Most open projects (see References) have several issues:

-The code is not maintained and contains components that are outdated and need some debugging.  
-The project is not documented well.  
-The project doesn't perform real-time classification.   

However, while looking through the other respositories I noticed a few things that will make a good starting point. There are already a few training models buiot out in jupyterlabs although they are outdated and will need to be outfitted. Before we do that we will have to do some tests to determine which features are the best predictor of a Twitter account's user type.

# UML 
![UML](https://github.com/CIS-SoftwareDesign-S21/pro-01-twitter-classification/blob/Web-App-Convert/UML.png)

# Base Repository 

https://github.com/zafargilani/uc/issues



## How to install Follower Display
1. Download FDSetup.exe
2. Go through install process
3. Enter the follower_display_revised folder
4. Run follower_display.exe application

## UCT Basic Web Application

https://uct-basic.ue.r.appspot.com/

## How to run UCT Basic web app locally via Command Prompt: 
1. Download UCT Basic Week Two zip file
2. In terminal, import Tweepy and Flask (**pip install tweepy**, then **pip install flask**)
3. Run main.py (**python main.py**)
4. In browser, navigate to http://127.0.0.1:8080/

# Link to Trello Board

https://trello.com/b/lV43sIEe/user-classification-in-twitter

# Vision

For people who work in marketing and advertising who utilize social media monitoring who want a way to sort Twitter users, The UCT program is a tool for Twitter that classifies users based on categories such as whether they're influencers, consumers, or politicans. Unlike other apps developed through Twitter's developer portal that show portions of data, our program provides a simple to use interface that displays a lot of data about individual users that show whether they're relevant for collecting marketing information.

# Personas

## Marketing Persona (Soobin Kim)
Jim is a 30 year old that lives near the World Trade Center in New York City, New York. He has a Bachelor's Degree in Market Research from New York University. Lately he works for Kantar, a market research company founded in London, England but with locations in many other countries. He spends most of his day online, but likes to go out for walks to enjoy the architecture and art in the city in his free time. 

Jim not only uses social media for personal entertainment, he also analyzes data from these sites as his job. He utilizes social media monitoring to develop an understanding of consumer wants and needs and delivers this information to his clients. He would find the UCT program useful when monitoring Twitter to classify companies vs. consumers and see the interactions of both of these categories of users. 

## Athlete Persona (Yang Bo)
Kento is a 26 years old Japanese badminton player. He has won several major badminton tournaments including two World Championships titles. Momota entered into Guinness Book of World Records for "The most badminton men's singles titles in a season", for his achievements by winning 11 titles in the 2019 season. He usually has no time to rest, he is usually training.

## Recruiting Persona (Gannon Traynor)
Tony is a hr manager and recruiter at a software development company in Silicon Valley. He is responsible for finding and contacting potential employee. Tony is able to use the User Classification program in twitter (uct) to assist his work. With the program he is able to narrow down to specify standard users and avoid wasting time looking at twitter accounts that are run by companies, or are bots. He is also able to find users that are active in the tech community and often talk about software development and other topics on their twitter account. UCT helps Tony find suitable candidates from a pool of a billion people.  

## Exporter Persona (Tarekegne Aboye)
Samuel is 44 years old and works in the international relations department of a private exporter company. He holds a degree in Business Administration from the country's educational institution. He also has some experience in technology and was born in Ethiopia. Samuel's company exports its products to different countries through its brokers, but since Samuel came to this company, he has been using various social media to communicate directly with the company's existing and new customers to make their services more reliable. 

As social networking helps different companies to express their products, services, and ideas, Samuel also uses a Twitter account in the company to promote his company's products and strengthen his relationship with various sections of the community to make the organization more profitable. However, to make the company???s product accessible to buyers in different countries and to strengthen the relationship between seller and buyer, he found the importance of the UCT program (user classification in Twitter) as a key to play a role in the company.

## Teacher Persona (Keshav Saraogi)
During the timeline of the project, I would like to implement the persona of a teacher. Mr Richard Walker is a currently a 32 year old high-school teacher, living in Pennsylvania for the past 7 years. Since the year 2020, he has been teaching online and has been using the internet to get hold of the resources that are in need of the teaching process. 

Mr Richard is being able to use the program as he is able to identify more teachers from the similar teaching interests, similar teaching background, and also people who were previously in the teaching position,  and is able to communicate in order to create a better teaching experience for the students.


## Repository Exploration (Tarekegne)
https://github.com/CodeBreakPP/TwitterUserType

For this week, I Picked a (CodeBreakPP/TwitterUserType) repository to add/fix and run the code. However, when I tried to run TwitterUserType (test.py) python code, the code needs to fix before I run it, and under the line 39, 44, 51, and 66 the written code should be put under parenthesis and in the bracket. So, I fixed that before I run it. Also, I added the NumPy library to make the code be working properly. 

In addition, when I tried to run test2.py TwitterUserType, I got the same problem and the code needs "sklearn.SVM" library so, I fixed that the same way as in the above. 

## Repository Exploration (Soobin)
https://github.com/zafargilani/uc/

This repository is the base that we chose to work with. There are many issues with the project in its current state, mainly because it is outdated. Installing the correct combination of libraries was difficult to do, and it involves a lot of trial and error. 

The issue I personally tackled was the conversion of the web app from Spyre to Flask. I had minimal trouble making the conversion, but the classification code itself either wasn't running correctly (with tensorflow backend) or was running very slowly (with theano backend) and ultimately it was what prevented me from being able to fully test if the web app was successfully converted.

Tests where the classification result was omitted worked ok (html and basic returns, such as the username inputted by the user).
