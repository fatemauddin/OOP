from flask import Flask, request, jsonify
from services.category_service import CategoryService
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow frontend to access backend

service = CategoryService()

@app.route("/categories", methods=["GET"])
def get_categories():
    return jsonify(service.get_categories())

@app.route("/categories", methods=["POST"])
def add_category():
    data = request.json
    service.create_category(data["name"])
    return jsonify({"message": "Category added"}), 201

if __name__ == "__main__":
    app.run(debug=True)
