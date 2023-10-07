
from app import create_app
# from app.extensions import db

if __name__ == '__main__':
    app = create_app()
    # db.init_app(app)
    
    print("inside run.py")
    app.run(debug=True)