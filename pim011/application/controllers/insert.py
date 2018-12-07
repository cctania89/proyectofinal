import web


render = web.template.render('application/views/', base='master')

class Insert:
    def __init__(self):
        pass

    def GET(self):  
        return render.insert()
    
    def POST(self):
        formulario = web.input()
        email = formulario['email']
        password = formulario['password']
        
        raise web.seeother('/')