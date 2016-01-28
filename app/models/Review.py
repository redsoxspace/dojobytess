
from system.core.model import Model

class Review(Model):
	def __init__(self):
		super(Review, self).__init__()

	def add(self, info):
		review = info['review']
		location = info['location']
		alias = info['alias']
		errors = []
		success = []

		if not review: 
			errors.append('You need to submit a review.')
		if len(review) > 255: 
			errors.append('Your review cannot be longer than 255 characters.')
		id_get = self.db.query_db("SELECT id FROM users WHERE alias = '{}'".format(alias))
		rest_get = self.db.query_db("SELECT id FROM restaurants WHERE restaurant_name = '{}'".format(location))
		compare = self.db.query_db("SELECT * FROM reviews WHERE user_id = '{}' AND restaurant_id = '{}'".format(id_get[0]['id'], rest_get[0]['id']))
		new_id = id_get[0]['id']
		rest = rest_get[0]['id']
		if compare:
			errors.append('You have already reviewed this restaurant.')

		if errors: 
			return{'errors':errors}

		else:
			self.db.query_db("INSERT INTO reviews (review_text, user_id, restaurant_id, created_at, updated_at) VALUES ('{}', '{}', '{}', NOW(), NOW())".format(review, new_id, rest))
			success.append("You done diddly did it!")
			return{'success':success}


	def find(self):
		all_restaurants = self.db.query_db("SELECT restaurant_name FROM restaurants")
		return{'all_restaurants' : all_restaurants}