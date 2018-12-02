from flask_example import app
from flask_script import Manager

manager = Manager(app)

@manager.command
def hello():
    return "Hello World!"

if __name__ == '__main__':
    manager.run()
