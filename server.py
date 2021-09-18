from flask import Flask  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response
@app.route('/dojo')
def dojo():
    return 'Dojo!'
@app.route('/say/<string:name>')
def hello(name):
    return 'Hello ' + name + "!"
@app.route('/repeat/<int:number>/<string:word>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show(number, word):
    output = ""
    for i in range(int(number)):
        output += f"<h2>{word}<h2>"
    return output
@app.route('/<path:path>')
def error(path=None):
    return "Sorry! No response. Try again."
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.