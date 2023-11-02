from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "<h1>Добрый вечер, уважаемые студенты!</h1>" \
"<a href='/info'>Обо мне</a><br>" \
"<a href='/calc/1/5'>Калькулятор</a>"

@app.route("/info")
def info():
    return "<b>Меня создала компания GeekBrains!</b>"

@app.route("/calc/<x>/<y>")
def calc(x, y):
    return f"{x} + {y} = {int(x) + int(y)}"


if __name__ == '__main__':
    app.run()