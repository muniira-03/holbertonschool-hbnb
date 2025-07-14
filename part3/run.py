from hbnb.app import create_app, db
from hbnb.app.models import user, place, review, amenity  

app = create_app()

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
