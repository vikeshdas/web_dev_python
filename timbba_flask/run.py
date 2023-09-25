
from app import create_app
# from app.extensions import db

if __name__ == '__main__':
    app = create_app()
    # db.init_app(app)
    app.run(debug=True)