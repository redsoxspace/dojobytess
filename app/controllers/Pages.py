
from system.core.controller import *

class Pages(Controller):
	def __init__(self, action):
		super(Pages
		, self).__init__(action)
		self.load_model('Review')

	def index(self):
		return self.load_view('index.html')

	def dashboard(self):
		try:
			session['alias']
		except: 
			message = "You need to be logged in to go that."
			flash(message)
			return redirect ("/")
		find = self.models['Review'].find()
		return self.load_view('dashboard.html', restaurants = find['all_restaurants'])

	def new(self):
		return self.load_view('new.html')