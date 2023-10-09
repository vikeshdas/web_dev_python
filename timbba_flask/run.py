
from app import create_app

if __name__ == '__main__':
    app = create_app()

    
    print("inside run.py")
    app.run(debug=True)