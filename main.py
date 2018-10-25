from flask import Flask, request, redirect, render_template
import cgi      # for auto_escaping
import os       # for file paths, jinja 
import jinja2   

# set up path to templates, activate jinja
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
# displays runtime errors in the browser
app.config['DEBUG'] = True      

# /// PROCESS /// 
# 01 - Build form structure

signup_form = """
<style>
    .error {{ color: red; }}
</style>
<h1>Signup</h1>
<form method='POST'>
    <table>
        <tbody>
            <tr>
                <td vAlign="top">
                    <label for="user_name">Username</label>
                </td>
                <td>
                    <input type="text" name="user_name" value='{user_name}'/>
                        <p class='error'>{name_error}</p>
                </td>
            </tr>
            <tr>
                <td vAlign="top">
                    <label for="user_pass">Password</label>
                </td>
                <td>
                    <input type="password" name="user_pass" value=''/>
                        <p class='error'>{pass_error}</p>
                </td>
            </tr>     
            <tr>
                <td vAlign="top">
                    <label for="user_pass_verify">Verify Password</label>
                </td>
                <td>
                    <input type="password" name="user_pass_verify" value=''/>
                        <p class='error'>{verify_error}</p>
                </td>
            </tr> 
            <tr>
                <td vAlign="top">
                    <label for="user_email">Email (optional)</label>
                </td>
                <td>
                    <input type="text" name="user_email" value='{user_email}'/>
                        <p class='error'>{email_error}</p>
                </td>
            </tr>     
            <tr>
                <td colspan="2">
                    <input type="submit" value="Submit"/>
                </td>
            </tr>           
        </tbody>
    </table>
</form>
"""
# /// PROCESS /// 
# 02 - Display form

@app.route('/signup')
def display_signup_form():
    return signup_form.format(user_name = '', name_error = '', user_pass = '', pass_error = '', user_pass_verify = '', verify_error = '', user_email = '', email_error = '')

# /// PROCESS /// 
# 03 - Process form

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

    if not u_name_error and not u_pass_error and not u_verify_error and not u_email_error:
        return "Success"
    else: 
        return signup_form.format(
            name_error=u_name_error,
            pass_error=u_pass_error, 
            verify_error=u_verify_error, 
            email_error=u_email_error, 
            user_name=user_name, 
            user_pass=user_pass, 
            user_pass_verify=user_verify, 
            user_email=user_email)

app.run()







# render signup form at localhost/signup
# DON'T NEED THIS ?
#@app.route("/signup")
#def display_signup():
#    template = jinja_env.get_template('signup.html')
#    return render_template('signup.html')

#@app.route("/signup", methods=['POST'])
#def validate_form():
    
    # look inside the request to figure out what the user typed, assign variables
#    user_name = request.form['user-name']
#    user_pass = request.form['user-pass']
#    verify_pass = request.form['user-pass-verify']
#    user_email = request.form['user-email']

    # ERROR: no data entry
#    if user_name == "":
#        un_error = "Enter a valid username"
#        return redirect("/signup/?error", user_name_error=un_error)

    # if we didn't redirect by now, then all is well
#    return render_template('welcome.html', crossed_off_movie=crossed_off_movie)

#@app.route("/")
#def index():
#    encoded_error = request.args.get("error")
#    return render_template('signup.html', error=encoded_error and cgi.escape(encoded_error, quote=True))

#app.run()