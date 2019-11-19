from flask import Flask, request, abort, jsonify
from difflib import SequenceMatcher

app = Flask(__name__)


@app.route('/similarity/api', methods=['POST'])
def similarity():
    if not request.json:
        abort(400)
    string1 = request.json['string1']
    string2 = request.json['string2']
    result = round(SequenceMatcher(None, string1, string2).ratio(), 4)
    return jsonify({'similarity': result})


if __name__ == '__main__':
    app.run(debug=True)
