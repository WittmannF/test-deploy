from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('segundo_app.html')

@app.route('/greet', methods=['POST'])
def cumprimentar():
    nome = [el for el in request.form.values()]
    return render_template('segundo_app.html', text='Olá '+nome[0])

if __name__=='__main__':
    app.run()
