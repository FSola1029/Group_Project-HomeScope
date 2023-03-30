from flask_app import app
from flask import render_template, redirect, request, session, flash, url_for
from flask_app.models.home import Home
from flask_app.models.user import User
# from flask_app.config import mycloudinary
import cloudinary
import cloudinary.uploader
import cloudinary.api


# Config
cloudinary.config(
    cloud_name=app.config['CLOUDINARY_CLOUD_NAME'],
    api_key=app.config['CLOUDINARY_API_KEY'],
    api_secret=app.config['CLOUDINARY_API_SECRET']
)

@app.route('/homes/new')
def create_homes():
    if 'user_id' not in session:
        return redirect('/')
    user = User.fetch_id({"id":session['user_id']})
    if not user:
        return redirect('/user/logout')
    home_types = Home.home_types()
    return render_template('new.html', user=user, homes= User.fetch_id({"id":session['user_id']}), home_types = home_types)




@app.route('/homes/add', methods=['POST'])
def homes_process():
    if 'user_id' not in session:
        return redirect('/')
    if not request.files['image']:
        flash(u"You must upload an image", "home_info")
        return redirect('/homes/new')
    if not Home.validating_homes(request.form):
        return redirect('/homes/new')
    file = request.files['image']
    upload_result = cloudinary.uploader.upload(file)
    image_url = upload_result['url']
    data = {
        'user_id': session['user_id'],
        'name': request.form['name'],
        'street_address': request.form['street_address'],
        'city': request.form['city'],
        'state': request.form['state'],
        'zipcode': request.form['zipcode'],
        'description': request.form['description'],
        'bed': request.form['bed'],
        'bath': request.form['bath'],
        'sq_ft': request.form['sq_ft'],
        'price': request.form['price'],
        'type': request.form['type'],
        'image': image_url
        }
    print(data)
    Home.save(data)
    return redirect('/dashboard')


@app.route('/homes/view/<home_type>')
def view_homes(home_type):
    homes = Home.get_homes_by_type({'type': home_type})
    return render_template('view.html', homes=homes)

@app.route('/homes/details/<home_id>')
def view_home_details(home_id):
    if 'user_id' in session:
        user = User.fetch_id({"id":session['user_id']})
    else:
        user = None
    home = Home.get_home_by_id({'id': home_id})
    return render_template('details.html', user=user, home=home)

@app.route('/homes/edit/<home_id>')
def edit_homes(home_id):
    if 'user_id' not in session:
        return redirect('/')
    user = User.fetch_id({"id":session['user_id']})
    if not user:
        return redirect('/')
    home_types = Home.home_types()
    return render_template('edit.html',user=user, home=Home.get_home_by_id({'id': home_id}), home_types=home_types)


@app.route('/homes/update/<int:home_id>', methods=['POST'])
def update_homes(home_id):
    if 'user_id' not in session:
        return redirect('/')
    if not request.files['image']:
        flash(u"You must upload an image", "home_info")
        return redirect(url_for('edit_homes', home_id=home_id))
    if not Home.validating_homes(request.form):
        return redirect(url_for('edit_homes', home_id=home_id))
    file = request.files['image']
    upload_result = cloudinary.uploader.upload(file)
    image_url = upload_result['url']
    data = {
        'id': home_id,
        'user_id': session['user_id'],
        'name': request.form['name'],
        'street_address': request.form['street_address'],
        'city': request.form['city'],
        'state': request.form['state'],
        'zipcode': request.form['zipcode'],
        'description': request.form['description'],
        'bed': request.form['bed'],
        'bath': request.form['bath'],
        'sq_ft': request.form['sq_ft'],
        'price': request.form['price'],
        'type': request.form['type'],
        'image': image_url
        }
    Home.update(data)
    return redirect('/dashboard')


@app.route('/homes/delete/<int:id>')
def delete_homes(id):
    if 'user_id' not in session:
        return redirect('/')
    Home.delete({'id':id})
    return redirect('/dashboard')

