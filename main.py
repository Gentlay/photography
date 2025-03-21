from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def serve_pdf():
    return send_file("document.pdf", mimetype="application/pdf")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)