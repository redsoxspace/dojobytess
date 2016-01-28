
from system.core.model import Model

class Restaurant(Model):
    def __init__(self):
        super(Restaurant, self).__init__()

    def add(self, info):
    	genre = info['genre']
    	restaurant_name = info['restaurant_name']
    	errors = []
    	success = []

    	if not restaurant_name: 
    		errors.append('Please include the name of the business.') 

    	if errors: 
    		return{'errors': errors}

    	compare = self.db.query_db("SELECT * FROM restaurants WHERE restaurant_name = '{}'".format(restaurant_name))
    	if compare: 
    		errors.append('That restaurant is already in the system. Try again.')
    	if errors: 
    		return{'errors': errors}    	
    	else:
    		query = "INSERT INTO restaurants (restaurant_name, genre, created_at, updated_at) VALUES ('{}', '{}', NOW(), NOW())".format(restaurant_name, genre)
    		self.db.query_db(query)
    		success.append('Restaurant added!')
    		return {"success": success}

    def search(self):
        new_stores = self.db.query_db("SELECT * FROM restaurants ORDER BY created_at DESC LIMIT 3")
        return {"new_stores" : new_stores}