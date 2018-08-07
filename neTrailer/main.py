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

class ComedyPage(webapp2.RequestHandler):
    def get(self):
        random_page_comedy = randint(0,2)
        print "Im in the comedy function"
        if random_page_comedy == 0:
            print "choice1"
            about_template = the_jinja_env.get_template('Templates/comedy.html')
            self.response.write(about_template.render())
        elif random_page_comedy == 1:
            print "choice2"
            about_template = the_jinja_env.get_template('Templates/comedy2.html')
            self.response.write(about_template.render())
        elif random_page_comedy == 2:
            print "choice3"
            about_template = the_jinja_env.get_template('Templates/comedy3.html')
            self.response.write(about_template.render())    
        
class ActionPage(webapp2.RequestHandler):
    def get(self):
        print "im in the action function"
        random_page_action = randint(0,2)
        if random_page_action == 0:
            print "im in choice 1"
            about_template = the_jinja_env.get_template('Templates/action.html')
            self.response.write(about_template.render())
        elif random_page_action == 1:
            print "im in choice 2"
            about_template = the_jinja_env.get_template('Templates/action2.html')
            self.response.write(about_template.render())
        elif random_page_action == 2:
            print "im in choice 3"
            about_template = the_jinja_env.get_template('Templates/action3.html')
            self.response.write(about_template.render())


            
class DramaPage(webapp2.RequestHandler):
    def get(self):
        print "im in the drama function"
        random_page_drama = randint(0,2)
        if random_page_drama == 0:
            print "im in action 1"
            about_template = the_jinja_env.get_template('Templates/drama.html')
            self.response.write(about_template.render())
        elif random_page_drama == 1:
            print "im in the drama 2"
            about_template = the_jinja_env.get_template('Templates/drama2.html')
            self.response.write(about_template.render())
        elif random_page_drama == 2:
            print "im in the drama 3"
            about_template = the_jinja_env.get_template('Templates/drama3.html')
            self.response.write(about_template.render())

class HorrorPage(webapp2.RequestHandler):
    def get(self):
        print "im in the horror function"
        random_page_horror = randint(0,2)
        if random_page_horror == 0:
            print "im in choice 1 for horror"
            about_template = the_jinja_env.get_template('Templates/horror.html')
            self.response.write(about_template.render())
        elif random_page_horror == 1:
            print "im in choice 2 for horror"
            about_template = the_jinja_env.get_template('Templates/horror2.html')
            self.response.write(about_template.render())
        elif random_page_horror == 2:
            print "im in choice 3 for horror"
            about_template = the_jinja_env.get_template('Templates/horror3.html')
            self.response.write(about_template.render())

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/SelectedComedy', ComedyPage),
    ('/SelectedAction', ActionPage),
    ('/SelectedDrama', DramaPage),
    ('/SelectedHorror', HorrorPage),
], debug=True)