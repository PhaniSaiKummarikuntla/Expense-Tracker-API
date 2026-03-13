from flask import Blueprint, request, jsonify
from .models import add_expense, get_all_expenses, delete_expense
from .analytics import generate_analytics

routes = Blueprint("routes", __name__)


@routes.route("/")
def home():
    return {"message": "Smart Expense Tracker API running"}


@routes.route("/expense", methods=["POST"])
def add():

    data = request.json

    add_expense(
        data["amount"],
        data["category"],
        data["date"]
    )

    return {"message": "Expense added"}


@routes.route("/expenses", methods=["GET"])
def get_expenses():

    rows = get_all_expenses()

    return jsonify(rows)


@routes.route("/expense/<int:id>", methods=["DELETE"])
def delete(id):

    delete_expense(id)

    return {"message": "Expense deleted"}


@routes.route("/analytics", methods=["GET"])
def analytics():

    rows = get_all_expenses()

    result = generate_analytics(rows)

    return jsonify(result)