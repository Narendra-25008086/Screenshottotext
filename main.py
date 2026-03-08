from flask import Flask, render_template, request
import pytesseract
from PIL import Image
import os

# create flask app FIRST
app = Flask(__name__)

# Windows only tesseract path
if os.name == "nt":
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/extract", methods=["POST"])
def extract():

    if "image" not in request.files:
        return render_template("index.html", result="No file uploaded")

    file = request.files["image"]

    if file.filename == "":
        return render_template("index.html", result="No file selected")

    img = Image.open(file).convert("RGB")
    text = pytesseract.image_to_string(img)

    return render_template("index.html", result=text)


if __name__ == "__main__":
    app.run(debug=True)