from flask import Flask, jsonify, render_template, send_file, request
import flask_cors
import csv
import random  # 追加

app = Flask(__name__)
flask_cors.CORS(app)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/manifest.json')
def serve_manifest():
    return send_file('manifest.json', mimetype='application/manifest+json')

@app.route('/sw.js')
def serve_sw():
    return send_file('sw.js', mimetype='application/javascript')

@app.route('/service-worker.js')
def service_worker():
    return send_file('sw.js', mimetype='application/javascript')

@app.route('/random', methods=['GET'])
def get_random():
    # 各パラメータを boolean に変換（未指定なら true とする）
    niku_param = request.args.get('niku', 'true').lower() == 'true'
    jutan_param = request.args.get('jutan', 'true').lower() == 'true'
    bin_param  = request.args.get('bin', 'true').lower() == 'true'
    color_param = request.args.get('color', 'true').lower() == 'true'
    food_param = request.args.get('food', 'true').lower() == 'true'

    with open('database.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    # falseとなったパラメータに応じたカテゴリーを除外（例: jutan は CSV上は 'zyutan' として扱う）
    filtered = []
    for row in data:
        category = row['Category'].strip().lower()
        if category == 'niku' and not niku_param:
            continue
        if category == 'zyutan' and not jutan_param:
            continue
        if category == 'bin' and not bin_param:
            continue
        if category == 'color' and not color_param:
            continue
        if category == 'food' and not food_param:
            continue
        filtered.append(row)
        
    print(filtered)

    if not filtered:
        return jsonify({'error': 'No matching data found'}), 404

    row = random.choice(filtered)
    return jsonify(row)

@app.route("/test")
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(port=9000, host="0.0.0.0", debug=True)