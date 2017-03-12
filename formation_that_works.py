import webapp2



page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>EncryptText</title>
</head>
<body>

"""

page_footer = """
</body>
</html>
"""

class Index(webapp2.RequestHandler):

    def get(self):
        add_form = """
        <form action="/encrypt" method="POST">
            <input type="text" name="text_to_encrypt"/>
            <input type="submit"/>
        </form>
        """
        response = page_header + add_form + page_footer
        self.response.write(response)

class EncryptText(webapp2.RequestHandler):

    def post(self):

        text_to_encrypt = self.request.get("text_to_encrypt")
        ecrypted_text = "<strong>" + text_to_encrypt + "</strong>"
        confirmation = "<p>" + ecrypted_text + "</p>"
        response = page_header + confirmation + page_footer
        self.response.write(response)

app = webapp2.WSGIApplication([
    ('/', Index),
    ('/encrypt', EncryptText)
], debug=True)
