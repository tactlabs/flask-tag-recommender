from flask import Flask, render_template
import os
import sys
from flask import request
from random import randint

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    
    link  = request.form.get('link')
    
    # You can validate the car brands. If someone is telling the wrong brand name, reply them with the wrong answer
    
    tags = get_tags(link)
    
    result = {
        'link' : link,
        'tags' : tags
    }
    
    #return content
    return render_template('result.html', result=result)

'''
    can throw:
        page not reachable
        can't tag this page due to limitation/violation issue
        
    Business: (to do)
        will read the 
'''
def get_tags(link):
    return '#dummy1 #dummy2'

def get_ticket_amount():
    return 45

if __name__ == '__main__':
    host = os.environ.get('IP', '127.0.0.1')
    port = int(os.environ.get('PORT', 5000))
    
    app.run(host= host, port = port, use_reloader = False)
    
    
'''
Sources:
    Sample tags:
        https://blogs.nvidia.com/blog/2018/04/11/ai-fashion/
'''