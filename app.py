""" aplikacja kalkulator"""

from flask import Flask, request

app = Flask(__name__)


@app.route('/calculate')
def calculate():

    """
    dodawanie argumentow
    """


    arg1 = request.args.get('arg1', type=int)
    arg2 = request.args.get('arg2', type=int)

    return f'{arg1} + {arg2} = {arg1 + arg2}'


if __name__ == '__main__':
    app.run()
