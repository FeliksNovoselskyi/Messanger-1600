from .settings import main_app

# Импортировать функции отображения
from chat_app.views import render_chat
from chat_app.app import chat_app_blueprint


main_app.add_url_rule(
    rule = "/",
    view_func = render_chat
)

main_app.register_blueprint(blueprint = chat_app_blueprint)
