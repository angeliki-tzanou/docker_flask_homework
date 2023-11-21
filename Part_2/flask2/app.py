from flask import Flask

app = Flask(__name__)
access_count = 0

@app.route('/')
def hello():
    global access_count
    access_count += 1
    return f'Hello this is my second Flask App!<br><br><strong>Cool feature:</strong> This app has been accessed {access_count} times.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8008)
