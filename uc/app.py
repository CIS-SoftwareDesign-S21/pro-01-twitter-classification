# -*- coding: utf-8 -*-
import os
from spyre import server
from flask import Flask, request, render_template, redirect
import liveprediction


class SimpleApp(server.App):
	title = "Classifying Twitter Users"

	inputs = [{ "type" : "text",
		"key" : "words",
		"label" : "Enter Twitter handle",
		"value" : ""}
	]

	outputs = [{"type" : "html",
		"id" : "some_html",
		"control_id" : "button1"}
	]
    
	controls = [{"type" : "button",
		"label" : "classify",
		"id" : "button1"}
	]

	def getHTML(self, params):
		words = params['words']
		if words == '':
			return 'Enter Twitter handle and press classify to run'
		else:
			Result = liveprediction.get_prediction(words)
			Result = " <br> ".join(str(x) for x in Result)

		return "Twitter user classified as: "+words+"<br>"+Result

app = SimpleApp()
app.launch(host='127.0.0.1', port=int(os.environ.get('PORT', '8000')))
"""
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
    app.run(host="127.0.0.1", port=8000, debug=True)
"""