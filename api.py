from flask import Flask, jsonify, request, abort
from langdetect import detect
import os

from core import translate

env_auth_key = ''

try:
    env_auth_key = os.environ['AUTH_KEY']
    print('AUTH_KEY: ' + env_auth_key)
except KeyError:
    print('No AUTH_KEY specified.')

app = Flask('NyaMT')


@app.route('/', methods=['POST'])
def post_translation():
    auth_key = request.args.get('auth_key')

    if env_auth_key != '' and auth_key != env_auth_key:
        abort(401)

    text = request.args.get('text')
    target_lang = request.args.get('target_lang').lower()
    source_lang = detect(text)
    return jsonify({
        "translations": [{
            "detected_source_language": source_lang.upper(),
            "text": translate(text, target_lang, source_lang)
        }]
    })


if __name__ == '__main__':
    app.run()
