import os
import liveprediction

user = str(input("Enter a twitter username: "))
Result = liveprediction.get_prediction(user)
Result = " <br> ".join(str(x) for x in Result)
