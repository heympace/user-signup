from flask import Flask, request, redirect, render_template
import cgi      # for auto_escaping
import os       # for file paths, jinja 
import jinja2   

# set up file system path to templates, activate jinja
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
# displays runtime errors in the browser
app.config['DEBUG'] = True      

# /// PROCESS /// 
# 01 - Build form structure

# /// PROCESS /// 
# 02 - Display form

@app.route('/signup')
def display_signup_form():
    template = jinja_env.get_template('signup_form.html')
    return template.render()
    
# /// PROCESS /// 
# 03 - Process form
# Created two functions to check for empty string, spaces
# Create /signup app.route to validate input
# Create variables for user input
# Create error variables w/ empty string to catch error messages
# Use if / elif / elif to create levels of errors for each field, no return statements

def empty_string(response):
    if response == "":
        return True

def space_check(userfield):
    for i in userfield:
        if i == ' ':
            return True
        else:
            return False

@app.route('/signup', methods = ['POST'])
def validate_signup():

    # get data out of request:                  
    # make sure request is imported up top
    user_name = request.form['user_name']
    user_pass = request.form['user_pass']
    user_verify = request.form['user_pass_verify']
    user_email = request.form['user_email']

    # variables to hold errors
    u_name_error = ''
    u_pass_error = ''
    u_verify_error = ''
    u_email_error = ''

    # TODO: 
    # Username tests
    if empty_string(user_name):
        u_name_error = 'Sad day. Blank username field.'
    elif len(user_name) < 3 or len(user_name) > 20:
        u_name_error = 'Come on bro, 3-20 characters.'
    elif space_check(user_name) == True:
        u_name_error = 'No spaces allowed. Try again...'

    # PW tests
    if empty_string(user_pass):
        u_pass_error = 'Sad day. Blank password field.'
    elif len(user_pass) < 3 or len(user_pass) > 20:
        u_pass_error = '3-20 characters por favor.'
    elif space_check(user_pass) == True:
        u_pass_error = "There's just too much space between us."        

    # PW VERIFY tests
    if empty_string(user_verify):
        u_verify_error = 'Sad day. Please enter password from above.'
        # compare password to verify field
    elif user_verify != user_pass:
        u_verify_error = "Dang. Your two passwords don't match."


    # EMAIL tests
    if len(user_email) != 0:
        if len(user_email) < 3 or len(user_email) > 20:
            u_email_error = 'Must be 3-20 characters. Or you need to rethink your whole email situation.'
        elif user_email.count('@') != 1:
            u_email_error = "Holler @t me. One '@' symbol is required."
        elif user_email.count('.') < 1:
            u_email_error = "Please double check email format"
        elif space_check(user_email) == True:
            u_email_error = "Let's get cozy &mdash; no spaces allowed."  

    # CHECK for PASS / Redirect to welcome
    if not u_name_error and not u_pass_error and not u_verify_error and not u_email_error:
        user_name = str(user_name)
        return redirect('/welcome?user_name={0}'.format(user_name))
        # this connects with app.route path below, line 167

    # CHECK for ERRORS / activate errors in html
    else: 
        template = jinja_env.get_template('signup_form.html')
        return template.render(
            name_error=u_name_error,
            pass_error=u_pass_error, 
            verify_error=u_verify_error, 
            email_error=u_email_error, 
            user_name=user_name, 
            user_pass=user_pass, 
            user_pass_verify=user_verify, 
            user_email=user_email)

# /// PROCESS /// 
# 04 - SET route to WELCOME confirmation page
@app.route('/welcome')
def form_validated():
    user_name = request.args.get('user_name')
    template = jinja_env.get_template('welcome.html')
    return template.render(user_name=user_name)

app.run()
