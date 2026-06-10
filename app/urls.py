from .settings import main_app

# Импортировать функции отображения
from chat_app.views import render_chat
from chat_app.app import chat_app_blueprint

from chat_app.views import render_Nikita
from chat_app.views import render_Egor
from chat_app.views import render_Nazar
from chat_app.views import render_Polina
from chat_app.views import render_Rostik

# Кирилл

main_app.add_url_rule(
    rule = "/",
    view_func = render_chat
)

main_app.add_url_rule(
    rule = "/Nikita",
    view_func = render_Nikita
)

main_app.add_url_rule(
    rule = "/Egor",
    view_func = render_Egor
)

main_app.add_url_rule(
    rule = "/Nazar",
    view_func = render_Nazar
)

main_app.add_url_rule(
    rule = "/Polina",
    view_func = render_Polina
)

main_app.add_url_rule(
    rule = "/Rostik",
    view_func = render_Rostik
)


# По аналогии со страницой /, написать маршрутизацию для всех страниц
# /Nikita, /Rostik...

main_app.register_blueprint(blueprint = chat_app_blueprint)
