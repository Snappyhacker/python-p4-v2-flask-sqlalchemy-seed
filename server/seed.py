#!/usr/bin/env python3
# server/seed.py

from app import app
from models import db, Pet

with app.app_context():

    # Delete all rows in the "pets" table
    Pet.query.delete()

    # Create an empty list of pets
    pets = [
        Pet(name="Fido", species="Dog"),
        Pet(name="Whiskers", species="Cat"),
        Pet(name="Hermie", species="Hamster"),
        Pet(name="Slither", species="Snake")
    ]

    # Add all pets to the session
    db.session.add_all(pets)

    # Commit the transaction
    db.session.commit()
