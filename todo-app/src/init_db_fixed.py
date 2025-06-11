import sys
import os

# Add the current directory to the Python path
sys.path.insert(0, os.path.abspath('.'))

# Now import the app and db
from src.todo_app.app import app, db

# Create the database tables
with app.app_context():
    db.create_all()
    print("✓ Database tables created successfully!")
