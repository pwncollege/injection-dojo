import flask

app = flask.Flask(__name__)

@app.route("/post", methods=["POST"])
def post():
    username = flask.request.form.get("user")
    message = flask.request.form.get("message").replace("\n", "<br>")
    messages =  f"""{username},{message}\n""" + open("messages.txt").read()
    open("messages.txt", "w").write(messages)
    return flask.redirect(f"/?user={username}")

@app.route("/", methods=["GET"])
def index():
    page = """<h1>The Chat</h1>"""

    user = flask.request.args.get("user", None)
    if not user:
        page += """
            <h2>Login</h2>
            <form method="get">
                Username: <input name="user">
                <input type=submit value="Login">
            </form>
        """
    elif "teacher" in user.lower():
        page += """
        <h1>Posting as the teacher is strictly prohibited!</h1>
        <a href="/">Logout</a>
        """
    else:
        page += f"""
            <h2>Post as {user}</h2>
            <form action="post" method="post">
                Message: <input name="message">
                <input name="user" type=hidden value="{user}">
                <input type=submit value="Post">
            </form>
            <a href="/">Logout</a>
        """

    for entry in open("messages.txt"):
        username, message = entry.split(",", 1)
        page += f"<hr><b>{username}:</b> {message}"


    return page

open('messages.txt', 'w').close()
app.run("0.0.0.0", 8082)
