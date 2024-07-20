from app import app, db

# Menginisialisasi database
with app.app_context():
    db.create_all()
    print("Database telah diinisialisasi.")
