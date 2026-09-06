import flask


def render_chat():
    return flask.render_template("chat.html")

def render_reg():
    # print(flask.request)
    if flask.request.method == "POST":
        email = flask.request.form.get("email")
        password = flask.request.form.get("password")
        confirm_password = flask.request.form.get("confirm_password")
        print(email, password, confirm_password)
    
    return flask.render_template("registration.html")