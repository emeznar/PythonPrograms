import webapp2
import cgi

# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>FlickList</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h1>
        <a href="/">FlickList</a>
    </h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""


# a list of movies that nobody should be allowed to watch
terrible_movies = [
    "Gigli",
    "Star Wars Episode 1: Attack of the Clones",
    "Paul Blart: Mall Cop 2",
    "Nine Lives"
]


def getCurrentWatchlist():
    """ Returns the user's current watchlist """

    # for now, we are just pretending
    return [ "Star Wars", "Minions", "Freaky Friday", "My Favorite Martian" ]


class Index(webapp2.RequestHandler):
    """ Handles requests coming in to '/' (the root of our site)
        e.g. www.flicklist.com/
    """

    def get(self):

        edit_header = "<h3>Edit My Watchlist</h3>"

        # a form for adding new movies
        add_form = """
        <form action="/add" method="post">
            <label>
                I want to add
                <input type="text" name="new-movie"/>
                to my watchlist.
            </label>
            <input type="submit" value="Add It"/>
        </form>
        """

        # a form for crossing off movies
        # (first we build a dropdown from the current watchlist items)
        crossoff_options = ""
        for movie in getCurrentWatchlist():
            crossoff_options += '<option value="{0}">{0}</option>'.format(movie)

        crossoff_form = """
        <form action="/cross-off" method="post">
            <label>
                I want to cross off
                <select name="crossed-off-movie"/>
                    {0}
                </select>
                from my watchlist.
            </label>
            <input type="submit" value="Cross It Off"/>
        </form>
        """.format(crossoff_options)

        # if we have an error, make a <p> to display it
        error = self.request.get("error")
        error_element = "<p class='error'>" + error + "</p>" if error else ""

        # combine all the pieces to build the content of our response
        main_content = edit_header + add_form + crossoff_form + error_element
        response = page_header + main_content + page_footer
        self.response.write(response)


class AddMovie(webapp2.RequestHandler):
    """ Handles requests coming in to '/add'
        e.g. www.flicklist.com/add
    """

    def post(self):
        # look inside the request to figure out what the user typed
        new_movie = self.request.get("new-movie")

        # TODO 2
        # if the user typed nothing at all, redirect and yell at them
        #if new-movie == "":
        #    self.redirect("/nothing")


        # TODO 3
        # if the user wants to add a terrible movie, redirect and yell at them


        # TODO 1
        # 'escape' the user's input so that if they typed HTML, it doesn't mess up our site
        #def escape_html(new-movie):
        #    return cgi.escape(new-movie, quote = True)

        # build response content
        new_movie_element = "<strong>" + new_movie + "</strong>"
        sentence = new_movie_element + " has been added to your Watchlist!"
        response = page_header + "<p>" + sentence + "</p>" + page_footer
        self.response.write(response)

#added for redirect
#class RedirectHandler(webapp2.RequestHandler):
#    def get(self):
#        self.response.out.write("You did not type anything!")


class CrossOffMovie(webapp2.RequestHandler):
    """ Handles requests coming in to '/cross-off'
        e.g. www.flicklist.com/cross-off
    """

    def post(self):
        # look inside the request to figure out what the user typed
        crossed_off_movie = self.request.get("crossed-off-movie")

        if (crossed_off_movie in getCurrentWatchlist()) == False:
            # the user tried to cross off a movie that isn't in their list,
            # so we redirect back to the front page and yell at them

            # make a helpful error message
            error = "'{0}' is not in your Watchlist, so you can't cross it off!".format(crossed_off_movie)
            error_escaped = cgi.escape(error, quote=True)

            # redirect to homepage, and include error as a query parameter in the URL
            self.redirect("/?error=" + error_escaped)

        # if we didn't redirect by now, then all is well
        crossed_off_movie_element = "<strike>" + crossed_off_movie + "</strike>"
        confirmation = crossed_off_movie_element + " has been crossed off your Watchlist."
        response = page_header + "<p>" + confirmation + "</p>" + page_footer
        self.response.write(response)


app = webapp2.WSGIApplication([
    ('/', Index),
    ('/add', AddMovie),
    ('/cross-off', CrossOffMovie)#,
    #('/nothing', RedirectHandler)
], debug=True)
