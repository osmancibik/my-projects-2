from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "hello world from osman flask"


@app.route("/second")
def second():
    return"bize her yer denizli"




@app.route("/third/subthird")
def third():
    return"bu ucuncu sayfanın alt sayafasınır"



@app.route("/forth/<string:id>")
def forth(id):
    return f'Id number of this page is {id}'
    
if __name__== "__main__":
    app.run(debug=True)









# from flask import Flask 

# app = Flask(__name__)

# @app.route("/")
# def stevie():
#     return "Hi Mehmet, we'll handle your problem in the break time"

# @app.route("/second")
# def second():
#     return "This is the second page"

# @app.route('/third/subthird')
# def third():
#     return "I think Kamshat understood this topic"

# @app.route("/forth/<string:id>")
# def forth(id):
#     return f"Id of this page is {id}"

# if __name__=="__main__":
#     app.run(host='0.0.0.0', port=80)
#     # app.run(debug=True)