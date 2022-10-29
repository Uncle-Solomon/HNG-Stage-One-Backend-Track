from flask import Flask,jsonify,request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods = ['GET'])
def anApi():
	if(request.method == 'GET'):
		data = {
			"slackUsername": "Uncle-Solomon",
            "backend": True,
            "age" : 20,
            "bio": "A Nigerian Prince trying to find his way in the tech industry."
		}

		return jsonify(data)

if __name__=='__main__':
	app.run(debug=True)
