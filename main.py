from flask import Flask, render_template, request
import smtplib

app=Flask(__name__)

@app.route('/')
def registration_input():
    return render_template('registration_input.html')

@app.route('/submit_form_data', methods=['POST'])
def submit_form_data():
    name = request.form['Name']
    email = request.form['Email']
    phone = request.form['Phone']
    age = request.form['Age']
    city = request.form['City']
    # Send confirmation email to user
    sender_email = 'senders email' #enter sender email address
    sender_password = 'senders google app generated password' #enter google app password here, steps to generate password are mentioned in readme.md file
    receiver_email = email
    message = f'Hi {name}, thank you for registering with us!'
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, message)
    
    # Send notification email to admin
    admin_email = 'admin@example.com' #enter admin email here
    message = f'A new user has registered:\nName: {name}\nEmail: {email}\nPhone: {phone}\nAge: {age}\nCity: {city}'
    
    server.sendmail(sender_email, admin_email, message)
    server.quit()
    return render_template('submit.html', name=name)

if __name__=='__main__':
    app.run()