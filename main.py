from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def get_client_info():
    client_ip = request.remote_addr
    client_port = request.environ.get('REMOTE_PORT')
    
    return jsonify({
        'ip': client_ip,
        'port': client_port
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
