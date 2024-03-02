"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://joyfoodsunshine.com/wp-content/uploads/2021/12/best-vanilla-cupcakes-recipe-1x1-1.jpg" 

class Cupcake(db.Model):
    """Model for Cupcakes"""
    
    __tablename__ = "cupcakes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)

    def serialize_to_dict(self):
        """Serialize cupcake data into dictionary of info"""
        return {
            "id": self.id,
            "flavor": self.flavor,
            "size": self.size,
            "rating": self.rating,
            "image": self.image,
        }
    
def connect_db(app):
    """Connect to db"""
    db.app = app
    db.init_app(app)