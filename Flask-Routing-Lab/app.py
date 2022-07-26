from flask import Flask, redirect, request, render_template, url_for


app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/product1')
def product1():
    return render_template('product.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')



if __name__ == "__main__": 
    app.run(debug=True)
