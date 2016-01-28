
from system.core.model import Model

class Review(Model):
	def __init__(self):
		super(Review, self).__init__()

	def add(self, info):
		review = info['review']
		location = info['location']
		if "'" in location:
			location = location.replace("'", "''")
		alias = info['alias']
		if "'" in alias: 
			alias = alias.replace("'", "''")
		errors = []
		success = []
		if not review: 
			errors.append('You need to submit a review.')
		if len(review) > 255: 
			errors.append('Your review cannot be longer than 255 characters.')
		id_get = self.db.query_db("SELECT id FROM users WHERE alias = '{}'".format(alias))
		rest_get = self.db.query_db("SELECT id FROM restaurants WHERE restaurant_name like '%{}%' LIMIT 1".format(location))
		new_id = id_get[0]['id']
		rest = rest_get[0]['id']
		compare = self.db.query_db("SELECT * FROM reviews WHERE user_id = '{}' AND restaurant_id = '{}'".format(new_id, rest))
		if compare:
			errors.append('You have already reviewed this restaurant.')

		if errors: 
			return{'errors':errors}

		else:
			self.db.query_db("INSERT INTO reviews (review_text, user_id, restaurant_id, created_at, updated_at) VALUES ('{}', '{}', '{}', NOW(), NOW())".format(review, new_id, rest))
			success.append("Restaurant Successfully Added")
			return{'success':success}


	def find(self):
		all_restaurants = self.db.query_db("SELECT restaurant_name FROM restaurants")
		return{'all_restaurants' : all_restaurants}











