from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World!'

@app.route('/dynamicsay', methods=['POST'])
def dynamic_say():
    return send_file('dynamicsay.json')

if __name__ == "__main__":
    app.run()