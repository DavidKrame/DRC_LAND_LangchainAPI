from flask import Blueprint, request, jsonify
from models import process_user_query
import openai

query_blueprint = Blueprint("query_blueprint", __name__)


@query_blueprint.route("/query", methods=["POST"])
def process_query():
    try:
        # Get the user's question from the POST request
        user_question = request.json.get("question", "")

        # Process the query using the model
        response = process_user_query(user_question)

        # Return the response as JSON
        return jsonify({"response": response})

    except openai.error.RateLimitError:
        return jsonify({"error": "Rate Limit with GPT models Exceeded"}), 429

    except Exception as e:
        return jsonify({"error": str(e)}), 500
