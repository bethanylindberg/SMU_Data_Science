#################################################
# Imports
#################################################
from flask import Flask, flash, request, redirect, url_for,render_template
import prediction
from keras.models import load_model
from datetime import datetime
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#################################################
# Flask Setup
#################################################
app = Flask(__name__,static_url_path='/static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#################################################
# Flask Routes
#################################################

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/about")
def about():
    """Return the about page."""
    return render_template("about.html")


@app.route("/details")
def details():
    """Return the details page."""
    return render_template("details.html")


@app.route("/home")
def home():
    """Return the homepage."""
    return redirect("/")

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # time_now = datetime.now().strftime('%Y-%m-%d%H%M%S')
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = (os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print(file_path)
            file.save(file_path)
            img = prediction.processImage(file_path)
            model = load_model("emotion_model_trained.h5")
            prediction = model.predict(img)

            pred_dict = {}

            pred_dict["Image_ID"] = filename
            # pred_dict["label"] = input_label
            pred_dict["angry_pred"] = round(prediction[0][0]*100,2)
            pred_dict["disgust_pred"] = round(prediction[0][1]*100,2)
            pred_dict["fear_pred"] = round(prediction[0][2]*100,2)
            pred_dict["happy_pred"] = round(prediction[0][3]*100,2)
            pred_dict["neutral_pred"] = round(prediction[0][4]*100,2)
            pred_dict["sad_pred"] = round(prediction[0][5]*100,2)
            pred_dict["surprise_pred"] = round(prediction[0][6]*100,2)

            # new_name = f"{time_now}{filename}"
            return render_template('predict.html', pred_dict=pred_dict, imagesource=file_path)

            # return redirect(url_for('uploaded_file',pred_dict=pred_dict, imagesource=filename))

from flask import send_from_directory

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

if __name__ == "__main__":
    app.run(debug=True)