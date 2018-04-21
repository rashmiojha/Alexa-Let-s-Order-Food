from flask import Flask, render_template, request
from process import Data, queryAmazon, mostPopular, getRecoForUser
import sys

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def welcome():
    # popular = mostPopular(20)
    # return render_template('index.html', popular=popular)
    return render_template('index.html')


@app.route("/recommend", methods=['GET','POST'])
def main():
    username = request.form['username']
    reco = getRecoForUser([username], 10)
    return render_template('recommendations.html', user=username, reco=reco)

if __name__ == '__main__':
    if len(sys.argv)==2 and sys.argv[1] == 'create':
        Data().createModels()
    elif len(sys.argv)==2 and sys.argv[1] == 'debug':
        app.debug = True
        app.run()
    else:
        app.run()