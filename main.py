# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    return render_template('index.html')


# Dinamik beceriler
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
 

    return render_template('index.html', 
                           button_python=button_python,
                           button_discord=button_discord
                           )

@app.route('/form_submit', methods=['POST'])
def submit_form():
    email = request.form.get('email')
    text = request.form.get('text')
    print(email, text)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
