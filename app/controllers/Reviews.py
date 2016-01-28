from system.core.controller import *

class Reviews(Controller):
	def __init__(self, action):
		super(Reviews, self).__init__(action)
		self.load_model('Review')

	def add(self):
		info = {
		"location" : request.form['location'],
		"review" : request.form['review'],
		"alias" : session['alias']
		}

		bouncer = self.models['Review'].add(info)

		try: 
			bouncer['errors']
			for message in bouncer['errors']:
				flash(message)
		except:
			for message in bouncer['success']:
				flash(message)
		return redirect ("/dashboard")