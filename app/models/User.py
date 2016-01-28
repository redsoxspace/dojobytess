
from system.core.model import Model
import re

class User(Model):
    def __init__(self):
        super(User, self).__init__()

    #checks info from register function in the controller, if it checks out, they are added to the database
    def verify_user(self, info):
		EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
		errors = []
		if "'" in info['alias']:
			info['alias'] = info['alias'].replace("'", "''")
		mailcheck = self.db.query_db("SELECT 'email' FROM users WHERE 'email' = '{}'".format(info['email']))
		aliascheck = self.db.query_db("SELECT alias FROM users where alias = '{}'".format(info['alias']))
		if len(info['alias']) <2: 
			errors.append('Your alias needs to have more than two characters')
		if len(mailcheck) > 0:
			errors.append('That email is already in use. Either choose another email or log in with it.')
		if len(aliascheck) > 0:
			errors.append('That alias is already in use. Choose another.')
		elif not EMAIL_REGEX.match(info['email']):
			errors.append('That is not a valid email. Please try again.')
		elif not info['email']:
			errors.append('Please do not leave the email field blank.')
		if len(info['password']) < 8:
			errors.append('Your password must be no less than 8 characters.')
		elif info['password'] != info['confirm']:
			errors.append('Make sure your password matches the input in confirm password.')
			        # if "'" in info['restaurant_name']:
           #  info['restaurant_name'] = info['restaurant_name'].replace("'", "''")


		if errors:
			return{"status": False, "errors" :errors}

		else:
			alias = info['alias']
			email = info['email']
			password = info['password']
			location = info['location']
			hash_pw = self.bcrypt.generate_password_hash(password)

			query = "INSERT INTO users (alias, email, password, location, created_at, updated_at) VALUES ('{}', '{}', '{}', '{}', NOW(), NOW())".format(alias, email, hash_pw, location)
			self.db.query_db(query)
			return{'status': True, 'success': 'Registration successful! Please log in.', 'alias':alias}