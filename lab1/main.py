import webapp2

class MainHandler(webapp2.RequestHandler):
	def get(self):
		self.response.write('Hello my name is ricardo')

app = webapp2.WSGIApplication([
	('/',MainHandler)
],debug = True)
