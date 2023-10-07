import os
from taskmanager import app, db


if __name__ == "__main__":
# Create database tables
    with app.app_context():
        db.create_all()
    
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )
