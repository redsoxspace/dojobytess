
from system.core.model import Model
import random 

class Restaurant(Model):
    def __init__(self):
        super(Restaurant, self).__init__()

    def add(self, info):
    	genre = info['genre']
    	restaurant_name = info['restaurant_name']
    	errors = []
    	success = []

        newname = ""

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
            new_restaurant = self.db.query_db("SELECT id FROM restaurants WHERE restaurant_name = '{}'".format(restaurant_name))
            success.append('Restaurant added!')
            return {"success": success, "new_restaurant": new_restaurant}

    def search(self):
        new_stores = self.db.query_db("SELECT * FROM restaurants ORDER BY created_at DESC LIMIT 3")
        new_list = ""
        for item in new_stores:
            temp = ""
            for letter in item['restaurant_name']:
                if letter == "~":
                    letter = "'"
                temp = temp + letter
            item['restaurant_name'] = temp



        return {"new_stores" : new_stores}

    def find(self, info):
        errors = []
        findings = []
        print info['restaurant_name']
        if info['genre'] == "No Genre": 
            findings = self.db.query_db("SELECT * FROM restaurants WHERE restaurant_name LIKE '%{}%'".format(info['restaurant_name']))
        elif not info['restaurant_name'] and info['genre'] != "No Genre": 
            findings = self.db.query_db("SELECT * FROM restaurants WHERE genre = '{}'".format(info['genre']))
        else: 
            findings = self.db.query_db("SELECT * FROM restaurants WHERE genre = '{}' AND restaurant_name LIKE '%{}%'".format(info['genre'], info['restaurant_name']))
        if not findings:
            errors.append("No results. Please try again.")
            return{'errors': errors}
        return{'findings' : findings}


    def profile(self, id):
        errors = []
        findings = self.db.query_db("SELECT * FROM restaurants WHERE id = '{}'".format(id))
        if not id:
            errors.append("Oops, we didn't have a valid id. Try again!")
            return{'errors': errors}
        if not findings:
            errors.append("Oops, we didn't have a valid id. Try again!")
            return{'errors': errors}
        else: 
            reviews = self.db.query_db("SELECT * FROM reviews LEFT JOIN users on reviews.user_id = users.id WHERE restaurant_id ='{}'".format(id))
            if reviews:
                checked = "" 
                checker = "~"
                for item in reviews[0]['review_text']:
                    if item == checker:
                        item = "'"
                    checked = checked + item
                reviews[0]['review_text'] = checked

            return{'findings' : findings, 'reviews' : reviews}


    def decider(self):
        contestants = self.db.query_db("SELECT id FROM restaurants")
        listify = []
        for item in contestants:
            listify.append(item['id'])
        target = random.randint(1,len(listify)-1)
        choice = self.db.query_db("SELECT * FROM restaurants WHERE id = '{}'".format(target))
        return{'choice':choice}



