import webapp2
import jinja2
import os
from random import randint


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('Templates/about.html')
        self.response.write(about_template.render())
        
class OldMainPage(webapp2.RequestHandler):
    def get(self):
        about_template =the_jinja_env.get_template('Templates/oldMain.html')
        self.response.write(about_template.render())
        
class HelpPage(webapp2.RedirectHandler):
    def get (self):
        about_template = the_jinja_env.get_template("Templates/help.html")
        self.response.write(about_template.render())
        
class MoviesPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template("Templates/main_movies.html")
        self.response.write(about_template.render())
        
class MusicPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template("Templates/main_music.html")
        self.response.write(about_template.render())
        
class TVPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template("Templates/main_TV.html")
        self.response.write(about_template.render())
        
class ComedyPage(webapp2.RequestHandler):
    def get(self):
        random_page_comedy = randint(0,4)
        print "Im in the comedy function"
        if random_page_comedy == 0:
            print "choice1"
            about_template = the_jinja_env.get_template('Templates/Movies/comedy.html')
            self.response.write(about_template.render())
        elif random_page_comedy == 1:
            print "choice2"
            about_template = the_jinja_env.get_template('Templates/Movies/comedy2.html')
            self.response.write(about_template.render())
        elif random_page_comedy == 2:
            print "choice3"
            about_template = the_jinja_env.get_template('Templates/Movies/comedy3.html')
            self.response.write(about_template.render())    
        elif random_page_comedy ==3:
            print "choice4"
            about_template = the_jinja_env.get_template('Templates/Movies/comedy4.html')
            self.response.write(about_template.render())
        elif random_page_comedy ==4:
            print "choice 5"
            about_template = the_jinja_env.get_template('Templates/Movies/comedy5.html')
            self.response.write(about_template.render()) 
            
class ActionPage(webapp2.RequestHandler):
    def get(self):
        print "im in the action function"
        random_page_action = randint(0,4)
        if random_page_action == 0:
            print "im in choice 1"
            about_template = the_jinja_env.get_template('Templates/Movies/action.html')
            self.response.write(about_template.render())
        elif random_page_action == 1:
            print "im in choice 2"
            about_template = the_jinja_env.get_template('Templates/Movies/action2.html')
            self.response.write(about_template.render())
        elif random_page_action == 2:
            print "im in choice 3"
            about_template = the_jinja_env.get_template('Templates/Movies/action3.html')
            self.response.write(about_template.render())
        elif random_page_action ==3:
            print "im in choice 4"
            about_template = the_jinja_env.get_template('Templates/Movies/action4.html')
            self.response.write(about_template.render()) 
        elif random_page_action == 4:
            print "im in choice 5"
            about_template = the_jinja_env.get_template('Templates/Movies/action5.html')
            self.response.write(about_template.render()) 
            
class DramaPage(webapp2.RequestHandler):
    def get(self):
        print "im in the drama function"
        random_page_drama = randint(0,4)
        if random_page_drama == 0:
            print "im in action 1"
            about_template = the_jinja_env.get_template('Templates/Movies/drama.html')
            self.response.write(about_template.render())
        elif random_page_drama == 1:
            print "im in the drama 2"
            about_template = the_jinja_env.get_template('Templates/Movies/drama2.html')
            self.response.write(about_template.render())
        elif random_page_drama == 2:
            print "im in the drama 3"
            about_template = the_jinja_env.get_template('Templates/Movies/drama3.html')
            self.response.write(about_template.render())
        elif random_page_drama == 3:
            about_template = the_jinja_env.get_template('Templates/Movies/drama4.html')
            self.response.write(about_template.render())
        elif random_page_drama == 4:
            about_template = the_jinja_env.get_template('Templates/Movies/drama5.html')
            self.response.write(about_template.render()) 

class HorrorPage(webapp2.RequestHandler):
    def get(self):
        print "im in the horror function"
        random_page_horror = randint(0,4)
        if random_page_horror == 0:
            print "im in choice 1 for horror"
            about_template = the_jinja_env.get_template('Templates/Movies/horror.html')
            self.response.write(about_template.render())
        elif random_page_horror == 1:
            print "im in choice 2 for horror"
            about_template = the_jinja_env.get_template('Templates/Movies/horror2.html')
            self.response.write(about_template.render())
        elif random_page_horror == 2:
            print "im in choice 3 for horror"
            about_template = the_jinja_env.get_template('Templates/Movies/horror3.html')
            self.response.write(about_template.render())
        elif random_page_horror == 3:
            about_template = the_jinja_env.get_template('Templates/Movies/horror4.html')
            self.response.write(about_template.render()) 
        elif random_page_horror ==4:
            about_template = the_jinja_env.get_template('Templates/Movies/horror5.html')
            self.response.write(about_template.render()) 

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/SelectedComedy', ComedyPage),
    ('/SelectedAction', ActionPage),
    ('/SelectedDrama', DramaPage),
    ('/SelectedHorror', HorrorPage),
    ('/About', HelpPage),
    ('/ClassicStyle', OldMainPage),
    ('/Movies', MoviesPage),
    ('/Music', MusicPage),
    ('/TVShows',TVPage),
], debug=True)