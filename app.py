from flask import Flask
import os


app = Flask(__name__)


@app.get("/")
def home():
    return {
        "message": "Hello from Docker",
        "hint": "Edit app.py, then rebuild the image to see changes inside the container.",
    }


@app.get("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)