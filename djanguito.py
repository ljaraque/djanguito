from http.server import BaseHTTPRequestHandler,HTTPServer
import datetime
import mimetypes

PORT = 8080

def render(archivo, context):
    with open('templates/'+archivo,'r') as templatefile:
        template = templatefile.read()
        template_renderizado = template.format_map(context)
        return template_renderizado.encode('utf-8')
    
def get_static(file_name):
    mime = mimetypes.MimeTypes().guess_type(file_name)[0]
    with open(file_name, "rb") as file:
        static_file = file.read()
        return static_file, mime
    
class myHandler(BaseHTTPRequestHandler):
    
    #Handler for the GET requests
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            # Send the html message
            context = {
                'titulo':'esta es la pagina renderizada',
                'hora':str(datetime.datetime.now()),
                'saludo':'Zdrastvuytie'
            }
            self.wfile.write(render('inicio.html',context))
        
        elif self.path == '/empresa':
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            # Send the html message
            context = {
                'titulo':'Esta es la pagina de la empresa',
                'hora':str(datetime.datetime.now()),
                'saludo':'Empresa de python.'
            }
            self.wfile.write(render('empresa.html', context))

        elif self.path == '/contacto':
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            # Send the html message
            context = {
                'titulo':'Esta es la pagina de contaco',
                'hora':str(datetime.datetime.now()),
                'saludo':'CONTACTANOS!'
            }
            self.wfile.write(render('contacto.html', context))

        elif self.path[0:7] == '/static':
            content, mime = get_static(self.path[1:])
            self.send_response(200)
            self.send_header('Content-type',mime)
            self.end_headers()
            # Send the html message
            self.wfile.write(content)

    def do_POST(self):
        if self.path == '/contacto':
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()

            # obtenemos los datos desde el request POST
            largo_contenido = int(self.headers['Content-Length'])
            data = self.rfile.read(largo_contenido).decode('utf-8')
            

            context = {
                'titulo':'Esta es la pagina de contaco',
                'mensaje':'EL CONTACTO HA SIDO EXITOSO',
                'data': data
            }
            self.wfile.write(render('contacto_exito.html', context))
            
            
            

server = HTTPServer(('', PORT), myHandler)
print('Started httpserver on port ', PORT)

#Wait forever for incoming http requests
server.serve_forever()