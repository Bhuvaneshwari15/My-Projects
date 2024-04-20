from flask import Flask, render_template, redirect, url_for, request, jsonify

app = Flask(__name__)

# Hardcoded user credentials for demonstration (replace with your actual authentication logic)
USER_CREDENTIALS = {
    'admin': {'password': 'admin123', 'role': 'admin'},
    'customer': {'password': 'customer123', 'role': 'customer'}
}

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# About Us Page
@app.route('/about')
def about():
    return render_template('about.html')

# Contact Us Page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Feedback Page
@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username in USER_CREDENTIALS and USER_CREDENTIALS[username]['password'] == password:
            # Authentication successful, redirect to a dashboard or home page based on user role
            if USER_CREDENTIALS[username]['role'] == 'admin':
                return redirect(url_for('admin_dashboard'))
            elif USER_CREDENTIALS[username]['role'] == 'customer':
                return redirect(url_for('customer_dashboard'))
        else:
            # Invalid credentials
            return jsonify({"success": False, "error": "Invalid credentials"})
    else:
        return render_template('login.html')

    
@app.route('/admin_dashboard')
def admin_dashboard():
    return render_template('admin_dashboard.html', user=USER_CREDENTIALS)

@app.route('/customer_dashboard')
def customer_dashboard():
    return render_template('customer_dashboard.html')

@app.route('/product_management')
def manage_product():
    return render_template('product_management.html')

@app.route('/order_management')
def manage_order():
    return render_template('order_management.html')

@app.route('/customer_management')
def customer_management():
    return render_template('customer_management.html')

@app.route('/analytics')
def data_analytics():
    return render_template('analytics.html')

@app.route('/supplier_management')
def supplier_management():
    return render_template('supplier_management.html')

@app.route('/report_management')
def report_management():
    return render_template('report_management.html')

@app.route('/invoice_management')
def invoice_management():
    return render_template('invoice_management.html')

@app.route('/view_orders')
def view_orders():
    return render_template('view_orders.html')

@app.route('/update_profile')
def update_profile():
    return render_template('update_profile.html')

@app.route('/order_history')
def order_history():
    return render_template('order_history.html')

@app.route('/special_offers')
def special_offers():
    return render_template('special_offers.html')

@app.route('/logout')
def logout_page():
    global current_user
    current_user = None
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
