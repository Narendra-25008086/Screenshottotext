@app.route("/extract", methods=["POST"])
def extract():
    try:
        if "image" not in request.files:
            return render_template("index.html", result="No file uploaded")

        file = request.files["image"]

        if file.filename == "":
            return render_template("index.html", result="No file selected")

        # Open and normalize the image
        img = Image.open(file.stream)
        img = img.convert("RGB")

        text = pytesseract.image_to_string(img)

        return render_template("index.html", result=text)

    except Exception as e:
        return render_template("index.html", result=f"Error: {str(e)}")