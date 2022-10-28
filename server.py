from flask import Flask, redirect, session, render_template, request

app = Flask(__name__)
app.secret_key = "boingBoing"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/form', methods=['POST'])
def formAnswers():
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    print(request.form)
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('submitted.html')




if __name__ == "__main__":
    app.run(debug=True)