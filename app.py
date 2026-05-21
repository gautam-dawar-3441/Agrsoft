from flask import Flask, render_template, request

app = Flask(__name__)

from flask_mail import Mail, Message

# EMAIL CONFIG
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'khushi12981298@gmail.com'
app.config['MAIL_PASSWORD'] = 'qvyl luad kplf rksz'

mail = Mail(app)
mail.init_app(app)

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

# FIXED CONTACT ROUTE 
# @app.route('/contact', methods=['GET', 'POST'])
# def contact():
#     if request.method == 'POST':
#         name = request.form.get('name')
#         email = request.form.get('email')
#         message = request.form.get('message')

#         print("Name:", name)
#         print("Email:", email)
#         print("Message:", message)

#         return render_template(
#             'contact.html',
#             success="Your message has been sent successfully!"
#         )

#     return render_template('contact.html')

# FIXED CONTACT ROUTE 
# EMAIL CONFIG
# @app.route('/contact', methods=['GET', 'POST'])
# def contact():
#     if request.method == 'POST':
#         name = request.form.get('name')
#         email = request.form.get('email')
#         message = request.form.get('message')

#         # EMAIL SENDING PART 👇
#         msg = Message(
#             subject=f"Contact Form Message from {name}",
#             sender=app.config['MAIL_USERNAME'],
#             recipients=['khushi12981298@gmail.com']
#         )

#         msg.body = f"""
#         Name: {name}
#         Email: {email}
#         Message: {message}
#         """

#         # mail.send(msg)
#         try:
#             mail.send(msg)
#             print("EMAIL SENT SUCCESSFULLY")
#         except Exception as e:
#             print("EMAIL FAILED:", e)
    
#         return render_template(
#             'contact.html',
#             success="Message sent successfully!"
#         )

    # return render_template('contact.html')
    
# @app.route('/contact', methods=['GET', 'POST'])
# def contact():
#     if request.method == 'POST':
#         name = request.form.get('name')
#         email = request.form.get('email')
#         message = request.form.get('message')

#         msg = Message(
#             subject=f"Contact Form Message from {name}",
#             sender=app.config['MAIL_USERNAME'],
#             recipients=[app.config['MAIL_USERNAME']]
#         )

#         msg.body = f"""
# Name: {name}
# Email: {email}
# Message: {message}
# """

#         try:
#             mail.send(msg)
#             print("EMAIL SENT SUCCESSFULLY")
#             return render_template('contact.html', success="Message sent successfully!")
#         except Exception as e:
#             print("EMAIL FAILED:", e)
#             return render_template('contact.html', success=f"Error: {e}")

#     return render_template('contact.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # =========================
        # 1. EMAIL TO YOU (ADMIN)
        # =========================
        admin_msg = Message(
            subject=f"New Contact Form Message from {name}",
            sender=app.config['MAIL_USERNAME'],
            recipients=[app.config['MAIL_USERNAME']]
        )

        admin_msg.body = f"""
New message received:

Name: {name}
Email: {email}
Message: {message}
"""

        mail.send(admin_msg)

        # =========================
        # 2. AUTO REPLY TO USER
        # =========================
        user_msg = Message(
            subject="Thank you for contacting us!",
            sender=app.config['MAIL_USERNAME'],
            recipients=[email]
        )

        user_msg.body = f"""
Hi {name},

Thank you for contacting us. 🙌

We have received your message:
"{message}"

Our team will get back to you shortly.

Best regards,
Your Company Team
"""

        mail.send(user_msg)

        return render_template(
            'contact.html',
            success="Message sent successfully! Check your email."
        )

    return render_template('contact.html')

if __name__ == "__main__":
    # app.run()
    app.run(host="0.0.0.0", port=10000)