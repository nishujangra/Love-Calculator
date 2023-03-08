from flask import Flask,render_template,request
from love import find, message, pass_value
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/', methods=["GET","POST"])
def hello_world_post():
    if request.method == 'POST':
        boy = str(request.form['name1'])
        girl = str(request.form['name2'])
        pass_value(boy,girl)
        love = find(boy,girl)
        message2 = message(love)
    return render_template('sucess.html',love=love,message=message2,boy=boy,girl=girl)
    # return render_template('index.html')
    


if __name__ == '__main__':
    app.run(debug=True)