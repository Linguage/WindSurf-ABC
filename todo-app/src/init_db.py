import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from todo_app.app import app, db

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("✓ Database tables created successfully!")
