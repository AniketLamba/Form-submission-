Registration Form Web App
!!!
This is a simple web app built with Flask that collects registration details from user and sends confirmation email to user and notification email to the admin.
!!!

!!!
Requirements: Python 3.x, Flask 2.1.0 or later
!!!

!!!
Installation
Navigate to the project directory in your terminal.
Install the required packages by running 'pip install -r requirements.txt'
!!!

!!!
Set up your email credentials in the main.py file. You'll need to replace the sender_email and sender_password variables with your own email address and Google generated app password
!!!

!!!
How to generate Google App password:
Step 1. Go to https://myaccount.google.com
Step 2. Click on 'security' on the left sidebar
Step 3. Go to '2 step verification' under 'how you sign in to Google'
Step 4. You'll be prompted to enter your google password, enter your password and proceed
Step 5. Scroll down to 'App passwords' and click on it
Step 6.  Select the app and select 'Other (Custom name)' from dropdown and enter 'Python SMTP' in required text field
Step 7. Click on generate and your app password will be generated
!!!

!!!
Run the app with the command python main.py
!!!

!!!
Usage
Open a web browser and go to http://localhost:5000/
Fill out the registration form with your details and click the "Submit" button
You will be redirected to a thank you page and receive a confirmation email
The admin will receive a notification email with your registration details
!!!

Contact if you have any questions or suggestions, feel free to contact me at Aniketlamba100@gmail.com