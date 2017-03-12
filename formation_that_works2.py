import webapp2
import cgi
from caesar import encrypt


class Index(webapp2.RequestHandler):
#create textarea for entering code to be encrypted
#add text box to accept rotation amount
    def get(self):
        add_form = """
        <form action="/encrypt" method="POST">
        <h3> Enter text to encrypt: </h3>

            <textarea name="text"> </textarea>

        <h3> Rotate by: </h3>
            <input type="text" name="rotnumber"/>
            <input type="submit"/>
        </form>
        """
        response = add_form
        self.response.write(response)

class EncryptText(webapp2.RequestHandler):
#escape html for text - then add it back before calling encrypt function(caesar)
    def post(self):
        text = cgi.escape(self.request.get("text"), quote=True)
        #TODO: add something to replace the ; here
        text = text.replace("&lt", "<")
        text = text.replace("&gt", ">")
        text = text.replace("&amp", "&")

        rotnumber = self.request.get("rotnumber")
        answer = encrypt(text, int(rotnumber))

        response = answer
        self.response.write(response)

app = webapp2.WSGIApplication([
    ('/', Index),
    ('/encrypt', EncryptText)
], debug=True)


#TODO:add redirect back to main page or when they click submit, convert it back?
