import json
import os
from flask import Flask, send_file, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello Shim!'

@app.route('/dynamicsay', methods=['POST'])
def dynamic_say():
    return send_file('dynamicsay.json')

@app.route('/dynamicsaynf', methods=['POST'])
def dynamic_say_nf():
    return send_file('dynamicsaynf.json')

@app.route('/collect',  methods=['POST'])
def collect():
    memory = json.loads(request.form.get('Memory'))

    answers = memory['twilio']['collected_data']['collect_user_info']['answers']

    first_name = answers['first_name']['answer'].title()
    genre_type = answers['genre']['answer']

    message = (
        f'Thank you for ordering with us. '
        f'I recommend Walk the Wire by David Baldacci as the perfect {genre_type} book for you to read today, {first_name}! '
        f'Someone from BookBot will reach out shortly to you to collect your personal details. '
        f'If you have any other questions, please feel free to reach out to us. '
    )

    return jsonify(actions=[{'say': {'speech': message}}])

if __name__ == "__main__":
    app.run()