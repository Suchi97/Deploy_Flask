from flask import Flask, render_template, request
#from .forms import LoginForm, AddForm, RegForm
#form = AddForm()
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('action1') == 'VALUE1':
            print('VALUE1')
        elif request.form.get('action2') == 'VALUE2':
            print('VALUE2')
        else:
            print("No buttons")
    elif request.method == 'GET':
        return render_template('index1.html')

    return render_template("index1.html")

if __name__ == "__main__":
    app.run()