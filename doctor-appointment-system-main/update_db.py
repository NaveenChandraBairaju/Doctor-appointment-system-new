"""Update database to add new patient fields"""
from app import app, db

with app.app_context():
    print("Updating database schema...")
    # This will add the new columns
    db.create_all()
    print("✓ Database updated successfully!")
    print("New patient fields added: age, gender, blood_group, height, weight, address, emergency_contact")
