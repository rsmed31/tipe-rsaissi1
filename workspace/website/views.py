from flask import Blueprint, render_template, request, flash

views = Blueprint('views', __name__)

@views.route('/', methods=['GET' , 'POST'])
def home():
    if request.method == 'POST':
        checkbox = request.form.get('checkbox.value')
        if checkbox == True :
            flash('successfully done' , category='success')
    return render_template("home.html")
