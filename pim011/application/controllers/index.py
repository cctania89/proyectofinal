import web

render = web.template.render('application/views/', base='master')

class Index:
    def __init__(self):
        pass

    def GET(self):       
        datos =['Tania','00258847@re.unid.mx']     
        return render.index(datos)
