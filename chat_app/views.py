import flask

# Женя


def render_chat():
    return flask.render_template("chat.html")

# Написать функции отображения для всех шаблонов
# Egor.html, Nazar.html, Polina.html, Rostik.html, Nikita.html
def render_Egor():
    return flask.render_template("Egor.html")

def render_Nazar():
    return flask.render_template("Nazar.html")

def render_Polina():
    return flask.render_template("Polina.html")

def render_Rostik():
    return flask.render_template("Rostik.html")

def render_Nikita():
    return flask.render_template("Nikita.html")
