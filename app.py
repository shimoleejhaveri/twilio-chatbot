import json
from flask import Flask, send_file, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World!'

@app.route('/dynamicsay', methods=['POST'])
def dynamic_say():
    return send_file('dynamicsay.json')

@app.route('/collect',  methods=['POST'])
def collect():
    memory = json.loads(request.form.get('Memory'))

    answers = memory['twilio']['collected_data']['collect_clothes_order']['answers']

    first_name = answers['first_name']['answer']
    clothes_type = answers['clothes_type']['answer']
    num_clothes = answers['num_clothes']['answer']

    message = (
        f'Ok {first_name}. Your order for {num_clothes} {clothes_type} is now confirmed.'
        f' Thank you for ordering with us'
    )

    return jsonify(actions=[{'say': {'speech': message}}])

if __name__ == "__main__":
    app.run()