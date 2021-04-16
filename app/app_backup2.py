
from flask import Flask, flash, send_from_directory, render_template, request, redirect, url_for
from waitress import serve
from src.utils import extract_feature_values, allowed_file
from src.models.predictor import get_prediction
from werkzeug.utils import secure_filename
import pandas as pd
import os

app = Flask(__name__, static_url_path="/static")
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 2048000
app.secret_key = 'key'

@app.route("/")
def index():
    """Return the main page."""
    return send_from_directory("static", "index.html")

@app.route("/make_prediction", methods=['POST'])
def upload_predict():
    if request.method == 'POST':
        #check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(url_for("index"))

        file = request.files['file']
        #if no file selected, browser submits an empty part without filename
        if file.filename != '':
            name = secure_filename(file.filename)           
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], name)
            file.save(file_path)

            data = pd.read_csv(file_path)
            feature_values = extract_feature_values(data)
            print(data) #debugging

            prediction = get_prediction(feature_values)

            return redirect(url_for("show_results", prediction=prediction))

        else:
            flash('No file selected! Try again.')
            return redirect(url_for("index"))
        
@app.route("/show_results")
def show_results():
    """ Display the results page with the provided prediction """
    
    # Extract the prediction from the URL params
    prediction = request.args.get("prediction")

    #prediction = round(float(prediction), 2)

    # Return the results pge
    return render_template("results.html", prediction=prediction)


if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=5000)
    
