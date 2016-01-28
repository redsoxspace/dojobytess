
from system.core.controller import *

class Restaurants(Controller):
    def __init__(self, action):
        super(Restaurants, self).__init__(action)
        self.load_model('Restaurant')

    def add(self):
    	info = {
    	"restaurant_name" : request.form["restaurant_name"],
    	"genre" : request.form['genre'] 
    	}
        if "'" in info['restaurant_name']:
            info['restaurant_name'] = info['restaurant_name'].replace("'", "''")        
    	bouncer = self.models['Restaurant'].add(info)

    	try: 
            bouncer['errors'] 
            for message in bouncer['errors']:
                flash(message)
            return redirect("/new")
    	except: 
    		for message in bouncer['success']:
    			flash(message)
                new_id = bouncer['new_restaurant'][0]['id']
                address = "/profile/%s" %(new_id)
                print address
                return redirect(address)

    def search(self):
        new_stores = self.models['Restaurant'].search()
        return self.load_view("search.html", new_stores=new_stores)

    def find(self):
        info = {
        "restaurant_name" : request.form['name'],
        "genre" : request.form['genre']
        }
        if "'" in info['restaurant_name']:
            info['restaurant_name'] = info['restaurant_name'].replace("'", "''")
        bouncer = self.models['Restaurant'].find(info)
        try: 
            bouncer['errors']
            for message in bouncer['errors']:
                flash(message)
            session['findings'] = []
            return redirect("/search")
        except:
            session['findings'] = bouncer['findings'] 
            return redirect("/search")

    def profile(self, id):
        populate = self.models['Restaurant'].profile(id)
        try:
            populate['errors']
            for message in populate['errors']: 
                flash(message)
            return redirect("/search")
        except: 
            findings = populate['findings']
            reviews = populate['reviews'] 
        return self.load_view("profile.html", findings = findings, reviews = reviews)


    def decider(self):
        finder = self.models['Restaurant'].decider()
        results = "/profile/%s" %(finder['choice'][0]['id'])
        return redirect(results)

