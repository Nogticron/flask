from flask import (
    Flask,
    render_template,
    url_for,
    request,
    current_app,
    g,
)

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello"


@app.route("/hello/<name>",
           methods=["GET", "POST"],
           endpoint="hello-endpoint")
def hello(name):
    return f"Hello {name}"


@app.get("/name/<name>")
def show_name(name):
    return render_template("index.html", name=name)


with app.test_request_context():
    # /
    print(url_for("index"))
    # /hello/world
    print(url_for("hello-endpoint", name="world"))
    # /name/ichiro?page=1
    print(url_for("show_name", name="ichiro", page="1"))


with app.test_request_context("/users?updated=true"):
    print(request.args.get("updated"))

# アプリケーションコンテキストを取得してスタックにpush
ctx = app.app_context()
ctx.push()

print(current_app.name)

# グローバルなtmp領域に値を設定
g.connection = "connection"
print(g.connection)
