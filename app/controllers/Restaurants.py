
from system.core.controller import *

class Restaurants(Controller):
    def __init__(self, action):
        super(Restaurants, self).__init__(action)
        self.load_model('Restaurant')

    def add(self):
    	info = {
    	"restaurant_name" : request.form['restaurant_name'],
    	"genre" : request.form['genre'] 
    	}
    	bouncer = self.models['Restaurant'].add(info)

    	try: 
    		bouncer['errors'] 
    		for message in bouncer['errors']:
    			flash(message)
    	except: 
    		for message in bouncer['success']:
    			flash(message)
    	return redirect("/dashboard")

    def search(self):
        new_stores = self.models['Restaurant'].search()
        return self.load_view("search.html", new_stores=new_stores)

    def find(self):
        print request.form
        return redirect("/search")