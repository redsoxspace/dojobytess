
from system.core.controller import *

class Sessions(Controller):
    def __init__(self, action):
        super(Sessions, self).__init__(action)
        self.load_model('Session')

    def login(self):
    	info = {
    	"email" : request.form['email'],
    	"password" : request.form['password']
    	}

    	bouncer = self.models['Session'].login(info)

    	try:
    		bouncer['errors']
    		for message in bouncer['errors']:
    			flash(message)
    		return redirect("/")
    	except: 
            session['alias'] = bouncer['alias']
            session['location'] = bouncer['location']
    	return redirect("/dashboard")

    def logoff(self):
        session.clear()
        return redirect("/")