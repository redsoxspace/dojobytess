
from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('User')
	# Has the model check registration info, returns errors or sucess messages 

    def register(self):
        info = {
        'alias': request.form['alias'],
        'email': request.form['email'],
        'location': request.form['location'],
        'password': request.form['password'],
        'confirm': request.form['confirm'],
        }
        if info:
        	inspector = self.models['User'].verify_user(info)
        try: 
        	inspector['errors']
        	for message in inspector['errors']:
        		flash(message)

        except:
        	session['success'] = inspector['success']
        	session['alias'] = inspector['alias']

        return redirect("/")
