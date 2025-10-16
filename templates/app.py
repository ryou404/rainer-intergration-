from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/hola")
def hola():
    return "hola"

@app.route('/user/string/<username>', methods=['GET'])
def show_user_profile(username):
    print('type(username) =>', type(username))
    return 'String => {}'.format(username)

@app.route('/user/int/<int:id>', methods=['GET'])
def show_user_id(id):
    print('type(id) =>', type(id))
    return 'Int => {}'.format(id)

@app.route('/user/float/<float:version>', methods=['GET'])
def show_user_version(version):
    print('type(version) =>', type(version))
    return 'Float => {}'.format(version)

vars = 'aaron_vars'

@app.route('/user/home')
def home():
    return render_template('home.html', text=vars)

@app.route('/user/appinfo')
def appInfo():
    appinfo = {
        'app_id': '314',
        'app_name': 'flask'
    }
    return render_template('home.html', appinfo=appinfo)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
