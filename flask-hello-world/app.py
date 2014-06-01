# import the Flask class from the flask module
from flask import Flask

# create the application object
app = Flask(__name__)

# error handling
app.config["DEBUG"] = True

# use decorators to link the function to a url
@app.route("/")
@app.route("/hello")

# define the view using a function, which returns a string
def hello_world():
    return "Hello, World!?!?!?!"

# dynamic route
@app.route("/test/<search_query>")
def search(search_query):
    return search_query

# dynamic route with an int type
@app.route("/integer/<int:value>")
def type(value):
    print value + 1
    return "correct"

# dynamic route with an float type
@app.route("/float/<float:value>")
def type(value):
    print value + 1
    return "correct"

# dynamic route that accepts slashes
@app.route("/path/<path:value>")
def type(value):
    print value
    return "correct"
http://localhost:5000/path/just/a/random/path

# dynamic route with explicit status codes
@app.route("/name/<name>") 
def  index(name): 
    if name.lower() == "michael" : 
        return "Hello, {}".format(name)
    else : 
        return "Not Found", 404

# start the development server using the run() method
if __name__ == "__main__":
    app.run()
