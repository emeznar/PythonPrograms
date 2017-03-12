import webapp2
import cgi
import re

#create a signup webpage with 4 text boxes that accepts
#username - blank or including spaces - keep text but throw error message - "^[a-zA-Z0-9_-]{3,20}$"
#password - blank - erase text box and throws error - "^.{3,20}$"
#verify password - if not match - error - "your passwords did not match"
#email(optional) - blank ok, but invalid throws error - ^[\S]+@[\S]+.[\S]+$"
# - then submit button
# Proper submit redirects to welcome page "Welcome, [username] !"
form = """
        <form method="POST">
        <h3> Signup Page: </h3>
            <label> Username </label>
            <input type="text" name="username" value="%(username)s"/><br>
            <label> Password </label>
            <input type="text" name="password" value="%(password)s"/><br>
            <label> Verify Password </label>
            <input type="text" name="verify" value="%(verify)s"/><br>
            <label> Email(Optional) </label>
            <input type="text" name="email" value="%(email)s"/><br>
            <input type="submit"/>
        </form>
        """
#TODO: add styling(CSS) to this form to be more like example on LC website

class Index(webapp2.RequestHandler):
#add text and rotnumber from html input above to webpage - variable substitution %s
    def write_form(self, username="",password="",verify="",email=""):
        self.response.out.write(form % {"username":username,
                                        "password":password,
                                        "verify":verify,
                                        "email":email})
#get or draw the main page
    def get(self):
        self.write_form()

#draw coded information on a page
    def post(self):
        username_input = self.request.get("username")
        #"^[a-zA-Z0-9_-]{3,20}$"

        password_input = self.request.get("password")
        #"^.{3,20}$"
        verify_input = self.request.get("verify")

        email_input = self.request.get("email")
        #"^[\S]+@[\S]+.[\S]+$"

        self.write_form(username_input,password_input,verify_input,email_input)

'''class Welcome(webapp2.RequestHandler):
    def get(self):
        username_input = self.request.get("username")
        if valid_username(username_input):
            self.render("welcom.html", username = username_input)
        else:
            self.redirect("Index")'''


#route information to the ap/webpage
app = webapp2.WSGIApplication([
    ('/', Index),
    #('welcome', Welcome)
], debug=True)

#TODO write functions to make variables conform to specs
#TODO create two html pages - Index for the signup page and welcome(suceess page)
#TODO add handler for redirect page - if all valid, redirect
