from flask import Flask, jsonify, request
import json
from bs4 import BeautifulSoup
import urllib.request
import urllib
import urllib.error

html = urllib.request.urlopen('https://time.com/').read()
soup = BeautifulSoup(html, 'html.parser')

main_div = soup.find('div', class_='latest-stories')
links = main_div.find_all('a')
texts = main_div.find_all('h3')
linkAndText = {}
i = 0
array = []
for a, b in zip(links, texts):
    i += 1
    array.append(
        {'title : ' + b.text: 'link: https://time.com' + a.get('href')})

    if(i == 5):
        break


# Serializing json
json_object = json.dumps(array)
print(json_object)


app = Flask(__name__)


@app.route('/getTimeNews', methods=['GET', 'POST'])
def home():
    if(request.method == 'GET'):

        # data = linkAndText
        return json_object
    if(request.method == 'POST'):

        # data = linkAndText
        return json_object


# driver function
if __name__ == '__main__':

    app.run(debug=True)
