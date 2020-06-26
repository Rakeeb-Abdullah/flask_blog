from flask import Blueprint,render_template,redirect,request
from flask_login import UserMixin,LoginManager,current_user,login_user,logout_user
from flask_admin.contrib.sqla import ModelView
from blog_app import db,admin,login
from blog_app.models import BlogPost,User

admin_con = Blueprint("admin_con", __name__, template_folder='template',static_folder='static')

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class UserView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

admin.add_view(UserView(BlogPost, db.session))
admin.add_view(UserView(User, db.session))

@admin_con.route('/admin', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if User.query.filter_by(username=username).all():
            user = User.query.filter_by(username=username).all()
            if user[0].password == password:
                current_userr = user[0]
                login_user(current_userr)
                return render_template('loggedin.html')
            else:
                return render_template('login_fail.html')
        else:
            return render_template('login_fail.html')
    else:
        return render_template('admin_login.html')

@admin_con.route('/logout')
def method_name():
   logout_user()
   return render_template('log_out.html')