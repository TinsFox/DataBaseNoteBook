from application import app, manager
from flask_script import Server
import www
## web server
manager.add_command("runserver", Server(port=5000,use_debugger=True))




def main():
    app.run(debug=True)


if __name__ == '__main__':
    try:
        import sys

        sys.exit(main())
    except Exception as e:
        import traceback

        traceback.print_exc()
