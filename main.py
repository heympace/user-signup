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
                    <label for="user-name">Username</label>
                </td>
                <td>
                    <input type="text" name="user-name" value='{user_name}'/>
                        <p class='error'>{name_error}</p>
                </td>
            </tr>
            <tr>
                <td vAlign="top">
                    <label for="user-pass">Password</label>
                </td>
                <td>
                    <input type="password" name="user-pass" value='{user_pass}'/>
                        <p class='error'>{pass_error}</p>
                </td>
            </tr>     
            <tr>
                <td vAlign="top">
                    <label for="user-pass-verify">Verify Password</label>
                </td>
                <td>
                    <input type="password" name="user-pass-verify" value='{user_pass_verify}'/>
                        <p class='error'>{verify_error}</p>
                </td>
            </tr> 
            <tr>
                <td vAlign="top">
                    <label for="user-email">Email (optional)</label>
                </td>
                <td>
                    <input type="text" name="user-email" value='{user_email}'/>
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