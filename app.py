from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dynamics365')
def dynamics365():
    return render_template('dynamics365.html')

@app.route('/powerplatforms')
def powerplatforms():
    return render_template('powerplatforms.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/industries')
def industries():
    return render_template('industries.html')

# ✅ FIXED CONTACT ROUTE (IMPORTANT)
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        print("Name:", name)
        print("Email:", email)
        print("Message:", message)

        return render_template(
            'contact.html',
            success="Your message has been sent successfully!"
        )

    return render_template('contact.html')

if __name__ == "__main__":
    app.run()