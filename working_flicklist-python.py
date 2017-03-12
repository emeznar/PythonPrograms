import webapp2



page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Flicklist</title>
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
        <form action="/add" method="POST">
            <input type="text" name="added_movie"/>
            <input type="submit"/>
        </form>
        """

        response = page_header + add_form + page_footer
        self.response.write(response)

class AddMovie(webapp2.RequestHandler):

    def post(self):

        added_movie = self.request.get("added_movie")
        movie_element = "<strong>" + added_movie + "</strong>"
        confirmation = "<p>" + movie_element + " has been added to your watchlist!" + "</p>"
        response = page_header + confirmation + page_footer
        self.response.write(response)

app = webapp2.WSGIApplication([
    ('/', Index),
    ('/add', AddMovie)
], debug=True)
