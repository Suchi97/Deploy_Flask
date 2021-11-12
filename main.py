from flask import Flask, flash, request, redirect, render_template

app = Flask(__name__)


@app.route('/', methods=['POST'])
def deploy():
    if request.method == 'POST':
        if request.form.get("action1") == "Submit":
            print("Entered")
            model_path = ""
            input_path = ""
            #return redirect(request.url)

        else:
            pass  # unknown
        return render_template("index.html")


if __name__ == "__main__":
    app.run()
