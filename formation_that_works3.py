import webapp2
import cgi
from caesar import encrypt


form = """
        <form method="POST">
        <h3> Enter text to encrypt: </h3>
            <textarea name="text">%(text)s</textarea>
        <h3> Rotate by: </h3>
            <input type="text" name="rotnumber" value="%(rotnumber)s"/>
            <input type="submit"/>
        </form>
        """


class Index(webapp2.RequestHandler):
#create textarea for entering code to be encrypted
#add text box to accept rotation amount
    def write_form(self, text="",rotnumber=""):
        self.response.out.write(form % {"text":text,
                                        "rotnumber":rotnumber})

    def get(self):
        self.write_form()

    def post(self):
        text = cgi.escape(self.request.get("text"), quote=True)
        #TODO: add something to replace the ; here
        text = text.replace("&lt", "<")
        text = text.replace("&gt", ">")
        text = text.replace("&amp", "&")
        text = text.replace(";", "")

        rotnumber = self.request.get("rotnumber")
        text = encrypt(text, int(rotnumber))

        self.write_form(text,rotnumber)


app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
