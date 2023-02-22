from flask import Flask, jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.engine.row import RowMapping

app = Flask(__name__)
engine = create_engine("sqlite:///paymepal.db")

def to_dict(row):
    """
    This function will convert rows or lists of rows to dictionaries of list of
    dictionaries respectively
    """
    if type(row) == RowMapping:
        return dict(row)
    elif type(row) == list:
        return [dict(row) for row in row]

@app.route("/users")
def list_users():
    query = """
    SELECT *
    FROM users
    """

    with engine.connect() as connection:
        result = connection.execute(query)
        users = result.mappings().all()

        return jsonify(to_dict(users))
    
@app.route("/users/<int:user_id>")
def get_user(user_id):
    query = f"""
    SELECT *
    FROM users
    WHERE id={user_id}
    """

    with engine.connect() as connection:
        result = connection.execute(query)
        user = result.mappings().one()

        return jsonify(to_dict(user))

@app.route("/users", methods=["POST"])
def create_user():
    user = request.get_json()

    query = f"""
    INSERT INTO users (username, email, password)
    VALUES (
        '{user["username"]}',
        '{user["email"]}',
        '{user["password"]}'
    )
    """

    with engine.connect() as connection:
        connection.execute(query)

        return jsonify(user), 201

        

app.run(debug=True, port=8080)