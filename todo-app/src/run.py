import os
import sys
from src.todo_app.app import app, db

def init_db():
    with app.app_context():
        db.create_all()
        print("✓ Database tables created successfully!")

if __name__ == '__main__':
    # Set the FLASK_APP environment variable
    os.environ['FLASK_APP'] = 'src.todo_app.app:app'
    
    # Initialize the database
    init_db()
    
    # Run the application
    app.run(debug=True)
