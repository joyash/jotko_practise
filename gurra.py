"""from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate_average', methods=['POST'])
def calculate_average():
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        average = (num1 + num2) / 2
        return render_template('result.html', num1=num1, num2=num2, average=average)


if __name__ == '__main__':
    app.run(debug=True)"""



