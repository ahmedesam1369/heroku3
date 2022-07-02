from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello'

@app.route('/api', methods = ['GET'])
def returnascii():
    d = {}
    inputchar = str(request.args['query'])
    # inputchar = 'a'
    # csac
    answer = str(ord(inputchar))
    d['output'] = answer
    
    return d



if __name__ == "__main__":
    app.run()


