import webapp2
import re

#github url=
#https://github.com/emeznar/signup.git
#---create a signup webpage with 4 text boxes that accepts
#username - blank or including spaces - keep text but throw error message - "^[a-zA-Z0-9_-]{3,20}$"
#password - blank - erase text box and throws error - "^.{3,20}$"
#verify password - if not match - error - "your passwords did not match"
#email(optional) - blank ok, but invalid throws error - ^[\S]+@[\S]+.[\S]+$"
#---- then submit button
# Proper submit redirects to welcome page "Welcome, [username] !"
form = """
        <form method="POST">
        <h3> Signup Page: </h3>
            <label> Username </label>
            <input type="text" name="username" value="%(username)s"/><br>
            <div style="color:red">%(error_username)s</div>

            <label> Password </label>
            <input type="text" name="password" value=""/><br>
            <div style="color:red">%(error_password)s</div>

            <label> Verify Password </label>
            <input type="text" name="verify" value=""/><br>
            <div style="color:red">%(error_verify)s</div>

            <label> Email(Optional) </label>
            <input type="text" name="email" value="%(email)s"/><br>
            <div style="color:red">%(error_email)s</div>
            <input type="submit"/>
        </form>
        """
welcome_form = """
        <form action="/welcome" method="POST">
        <h3> Welcome %(new_username)s !</h3>


        </form>
        """
#TODO: add styling(CSS) to this form to be more like example on LC website

#functions to validate signup page variablesdev_appserver.py .
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)
PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)
EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
def valid_email(email):
    return not email or EMAIL_RE.match(email)

class Index(webapp2.RequestHandler):
#add text and rotnumber from html input above to webpage - variable substitution %s
    def write_form(self, username="",error_username="",password="",error_password="",verify="",
                         error_verify="",email="",error_email=""):
        self.response.out.write(form % {"username":username,
                                        "password":password,
                                        "verify":verify,
                                        "email":email,
                                        "error_username":error_username,
                                        "error_password":error_password,
                                        "error_verify":error_verify,
                                        "error_email":error_email})

#get or draw the main page
    def get(self):
        self.write_form()
#draw coded information on a page
    def post(self):
        error = False #if not to specs set to true - if make it through load success page

        #TODO create if else statements to confirm input for reg exps above

        username = self.request.get("username")
        if not valid_username(username):
            error_username = "That's not a valid username"
            error = True
        else:
            error_username = ""

        password = self.request.get("password")
        if not valid_password(password):
            error_password = "That's not a valid password"
            error = True
        else:
            error_password = ""

        verify = self.request.get("verify")
        if password != verify:
            error_verify = "Your passwords didn't match"
            error = True
        else:
            error_verify = ""


        email = self.request.get("email")
        if not valid_email(email):
            error_email = "That's not a valid email"
            error = True
        else:
            error_email = ""

        if error == True:
            self.write_form(username,error_username,password, error_password, verify,
                            error_verify,email,error_email)
        else:
            self.redirect("/welcome?username=" + username)


class Welcome_handler(webapp2.RequestHandler):
    def write_welcome_form(self, new_username=""):
                self.response.out.write(welcome_form % {"new_username":new_username})

    def get(self):
        new_username = self.request.get('username')
        self.write_welcome_form(new_username)

#route information to the ap/webpage
app = webapp2.WSGIApplication([
    ('/', Index),
    ('/welcome', Welcome_handler)
], debug=True)

#TODO create two html pages - Index for the signup page and welcome(suceess page)
