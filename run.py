# Module Name : lec_flask_test.py

from flask import Flask, render_template

app = Flask(__name__)

# static 폴더 : 정적(css, img, js ..)
# templates : 디자인(html)

# http://localhost:8077/
@app.route('/')
def index():
    # return 'Hello Flask'
    return render_template("index.html")


# http://localhost:8077/info
@app.route('/info')
def info():
    return 'Info'

if __name__ == '__main__':
    app.run(host='localhost', port=8077, debug=True)
