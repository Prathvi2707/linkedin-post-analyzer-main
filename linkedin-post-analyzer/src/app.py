from flask import Flask, request, jsonify
from utils import analyze_post

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    post_content = data.get('post_content', '')
    analysis_result = analyze_post(post_content)
    return jsonify(analysis_result)

if __name__ == '__main__':
    app.run(debug=True)