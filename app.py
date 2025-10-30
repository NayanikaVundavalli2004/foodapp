from flask import Flask, render_template, request

app = Flask(__name__)

# Sample food menu
menu = {
    "Pizza": 250,
    "Burger": 150,
    "Pasta": 200,
    "Sandwich": 120,
    "Coffee": 80
}

@app.route('/')
def home():
    return render_template('index.html', menu=menu)

@app.route('/order', methods=['POST'])
def order():
    item = request.form['item']
    quantity = int(request.form['quantity'])
    total = menu[item] * quantity
    return f"You ordered {quantity} {item}(s). Total bill: ₹{total}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
