import flask_sqlalchemy
import flask_migrate
import os

from .settings import main_app

main_app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

DATABASE = flask_sqlalchemy.SQLAlchemy(app = main_app)


# Создать объект миграций
# Указать абсолютный путь к папке migrations/
MIGRATE = flask_migrate.Migrate(
    app= main_app, 
    db= DATABASE,
    directory = os.path.abspath(os.path.join(__file__, "..", "migrations"))
)
