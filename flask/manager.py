from flask_example import app, db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def init_db():
    print('init_db')

if __name__ == '__main__':
    manager.run()
# xx