from flask_app import app
from flask import redirect, send_from_directory, url_for, request, redirect, render_template, session
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

class UploadForm(FlaskForm):
    photo = FileField(
        validators=[
            FileAllowed(photos, 'Only images are allowed'),
            FileRequired('File Field should not be empty')
        ]
    )
    submit = SubmitField('Upload')

@app.route('/homes/uploads/<filename>')
def get_file(filename):

    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], filename)



@app.route('/', methods=['GET', 'POST'])
def upload_image():
    form = UploadForm()
    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        file_url = url_for('get_file', filename=filename)
    else:
        file_url = None
    return redirect('homes/new', form=form, file_url = file_url)