from project import db, create_app
from flask.cli import FlaskGroup

app = create_app()

# Creating Database Models
cli = FlaskGroup(app)

@cli.command('create_db')
def create_db():
    print("Hello")
    db.create_all()

if __name__ == '__main__':
    cli()