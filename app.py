"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify, render_template

from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "secret"

connect_db(app)


@app.route('/')
def root():
    """Show homepage"""
    return render_template("index.html")

@app.route('/api/cupcakes')
def get_cupcakes_list():
    """Return of all existing cupcakes as JSON"""

    cupcakes = [Cupcake.serialize_to_dict() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)

@app.route('/api/cupcakes', methods=["POST"])
def create_cupcake():
    """Add a new cupcake and return data about it (as JSON) with proper status code."""

    data = request.json

    cupcake = Cupcake(flavor=data['flavor'], rating=data['rating'], size=data['size'], image=data['image'] or None)
    
    db.session.add(cupcake)
    db.session.commit()
    return (jsonify(cupcake=cupcake.serialize_to_dict()), 201)

@app.route('/api/cupcakes/<int:cupcake_id>')
def get_cupcake(cupcake_id):
    """Get data on specific cupcake and return JSON"""
    
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.serialize_to_dict())

@app.route('/api/cupcakes/<int:cupcake_id>', methods=["PATCH"])
def update_cupcake(cupcake_id):
    """Update info on specific cupcake"""

    data = request.json
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    
    cupcake.flavor = data['flavor']
    cupcake.rating = data['rating']
    cupcake.size = data['size']
    cupcake.image = data['image']

    db.session.add(cupcake)
    db.session.add()
    return jsonify(cupcake=cupcake.serialize_to_dict())

@app.route('/api/cupcakes/<int:cupcake_id>', methods=["DELETE"])
def delete_cupcake(cupcake_id):
    """Delete cupcake from database and return JSON confirming deletion"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message = "Deleted")