from application import app, manager
from flask_script import Server
from flask_sqlalchemy import SQLAlchemy
import www


## web server
# manager.add_command("runserver", Server(port=5000,use_debugger=True))


def main():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@47.106.155.159:3306/tinsfox'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.run(debug=True)


if __name__ == '__main__':
    try:
        import sys

        sys.exit(main())
    except Exception as e:
        import traceback

        traceback.print_exc()
