from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/vue')
def vue():
    return render_template('组件化应用构建.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=80)
