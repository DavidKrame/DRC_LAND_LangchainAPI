from flask import Flask
from routes import query_blueprint

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(query_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
