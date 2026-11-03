from flask import Flask, jsonify, render_template, request
from passages import PASSAGES
from scoring import analyze_result
import random

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index.html')

@app.get('/api/passage')
def passage():
    level = request.args.get('level', 'medium').lower()
    category = request.args.get('category', 'general').lower()
    if level not in PASSAGES: level = 'medium'
    pool = PASSAGES[level]
    matches = [x for x in pool if x['category'] == category]
    if not matches: matches = pool
    chosen = random.choice(matches)
    return jsonify({'text': chosen['text'], 'level': level, 'category': chosen['category'], 'title': chosen['title']})

@app.post('/api/analyze')
def analyze():
    data = request.get_json(silent=True) or {}
    try:
        target = data.get('target', '')
        typed = data.get('typed', '')
        seconds = float(data.get('elapsed', 0))
        if not isinstance(target, str) or not isinstance(typed, str) or len(target)>5000 or len(typed)>7000:
            return jsonify({'error':'Invalid typing data.'}),400
        if not target or seconds <= 0 or seconds > 3600:
            return jsonify({'error':'Test duration or passage is invalid.'}),400
        return jsonify(analyze_result(target,typed,seconds))
    except (TypeError,ValueError):
        return jsonify({'error':'Invalid numeric time.'}),400

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=False)
