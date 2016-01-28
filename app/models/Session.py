
from system.core.model import Model
import re

class Session(Model):
  def __init__(self):
    super(Session, self).__init__()

  def login(self, info):
    EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
    errors = []
    password = info['password']
    email = info['email']

    #check before query
    if not email:
      errors.append('Your email is missing')
    if not password:
      errors.append('Your password is missing.')

    if errors: 
      return {'errors':errors}

    #run query and compare to input
    compare = self.db.query_db("SELECT * FROM users WHERE email = '{}'".format(email))
    if not compare:
      errors.append('That user does not exist. Try again.')
      return {'errors':errors}
    if email != compare[0]['email']:
      errors.append('That user does not exist. Try again.')
    if not self.bcrypt.check_password_hash(compare[0]['password'], password):
      errors.append('Check your password.')
    if errors:
      return {"errors":errors}
    else:
      return {"alias": compare[0]['alias'], "location": compare[0]['location']}

