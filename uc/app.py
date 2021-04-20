# -*- coding: utf-8 -*-
import os
from flask import Flask, request, render_template, redirect
import liveprediction

app = Flask(__name__, template_folder="templates")


@app.route('/', methods = ["GET", "POST"])

def SimpleApp():
    if request.method == "POST":
        words = request.form.get("user")
        
        return result(words)
    return render_template("form.html", pageTitle='User Classification in Twitter')
   
def result(username):
    Result = liveprediction.get_prediction(username)
    Result = " \n".join(str(x) for x in Result)
    return "Twitter user classified as: "+username+"\n"+Result
    
#"+words+"<br>"
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
