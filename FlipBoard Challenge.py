import flask
from flask import request, jsonify, render_template
import re

def sanitizestring(text):
    #replaces the characters with '_'
    text = re.sub('\$','_',text)
    text = re.sub('\%','_',text)
    text = re.sub('\&','_',text)
    text = re.sub('\\\\','_',text)
    text = re.sub('\|','_',text)
    text = re.sub('\[','_',text)
    text = re.sub('\]','_',text)
    text = re.sub('\{','_',text)
    text = re.sub('\}','_',text)
    
    #replaces emails with '(email_removed)'
    text = re.sub('[a-zA-Z0-9]+\@([a-zA-Z]+)\.[a-z]+','(email_removed)',text)
    
    #replaces phone numbers with '(phone_removed)'
    text = re.sub('[0-9]+\-[0-9]+\-[0-9]+','(phone_removed)',text)
    text = re.sub('[0-9]+\s[0-9]+\s[0-9]+','(phone_removed)',text)
    text = re.sub('\([0-9]+\)\s[0-9]+\-[0-9]+','(phone_removed)',text)
    
    #removes any http:// or https://
    text = re.sub('[a-z]+\:\/\/','',text)

    #replaces websites with '(website_removed)'
    text = re.sub('[a-zA-Z]+\.[a-zA-Z]+\.[a-zA-Z]+','(website_removed)',text)

    #replaces any number of sequential spaces with single space
    text = re.sub('\s+',' ',text)
    return text


app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def my_form():
    return render_template('my-form.html')
@app.route('/',methods = ['POST'])
def my_form_post():
    if request.method == 'POST':

        form_data = request.form
        param   = sanitizestring(form_data.to_dict()['text'])
        
        return render_template('result.html',form_data = {'text':param})
if __name__ == "__main__":
    app.run()