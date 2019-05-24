from application import app, manager
# 引入入口文件
import www

from flask_script import Server

# web Server
manager.add_command("runserver", Server(port=5000))


def main():
    app.run(debug=True)


if __name__ == '__main__':
    try:
        import sys

        sys.exit(main())
    except Exception as e:
        import traceback

        traceback.print_exc()
