from flask import Flask, render_template, request

from calculator import Calculator


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('calculator.html')

    @app.route('/result', methods=['POST'])
    def result():
        first_term = request.form.get("first_term", type=int)
        second_term = request.form.get("second_term", type=int)
        operation = request.form.get("operation")
        c = Calculator(first_term, second_term)
        if operation == 'Add':
            res = c.add()
        elif operation == 'Subtract':
            res = c.subtract()
        elif operation == 'Multiply':
            res = c.multiply()
        elif operation == 'Divide':
            res = c.divide()
        else:
            res = 'INVALID CHOICE'
        return render_template('result.html', result=res)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(port=5000, debug=True)
