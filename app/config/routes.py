
from system.core.router import routes

routes['default_controller'] = 'Pages'
routes['POST']['/register'] = "Users#register"
routes['POST']['/login'] = "Sessions#login"
routes['GET']['/logout'] = "Sessions#logoff"
routes['GET']['/dashboard'] = "Pages#dashboard"
routes['POST']['/add_store'] = "Restaurants#add"
routes['POST']['/add_review'] = "Reviews#add"
routes['GET']['/search'] = 'Restaurants#search'
routes['POST']['/find'] = 'Restaurants#find'
