

visualize = Blueprint('visualize', __name__)

@visualize.route('/visualize', methods=['GET', 'POST'])
def home():
    if 'username' in session:
        return render_template("home.html")
    else:
        return redirect(url_for('auth.login'))