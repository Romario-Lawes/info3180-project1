"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os, datetime
from app import app, db
from app.models import UserProfile
from flask import render_template, request, redirect, url_for, flash, session, abort
from werkzeug.utils import secure_filename
from forms import ProfileForm


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/profile', methods=['POST', 'GET'])
def profile():
    profileForm = ProfileForm()
    
    if request.method == 'POST' and profileForm.validate_on_submit():
        firstname = profileForm.firstname.data
        lastname = profileForm.lastname.data
        email = profileForm.email.data
        location = profileForm.location.data
        gender = profileForm.gender.data
        bio = profileForm.biography.data
        
        photo = profileForm.photo.data
        imageName = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], imageName))
        
        created_on = datetime.datetime.now().strftime("%B, %d %Y")
        
        user = UserProfile(firstname, lastname, email, location, gender, bio, imageName, created_on)
        db.session.add(user)
        db.session.commit()
        
        flash('Profile Successfully Added', 'success')
        return redirect(url_for("profiles"))
    flash_errors(profileForm)
    return render_template('profile.html', form=profileForm)


@app.route('/profiles')
def profiles():
    users = db.session.query(UserProfile).all()
    return render_template('profiles.html', users=users)


@app.route('/profile/<userid>')
def userProfile(userid):
    user = UserProfile.query.filter_by(id=userid).first()
    return render_template('user_profile.html', user=user)



###
# The functions below should be applicable to all Flask apps.
###

# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
