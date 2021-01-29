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
            self.wfile.write(("<b>Empresa</b>"
                        + "<br><br> La hora actual es:" + str(datetime.datetime.now())).encode('utf-8'))

        elif self.path == '/contacto':
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            # Send the html message
            self.wfile.write(("<b>Contacto</b>"
                        + "<br><br> La hora actual es:" + str(datetime.datetime.now())).encode('utf-8'))

        elif self.path == '/static/img/Putin.jpeg':
            content, mime = get_static('static/img/Putin.jpeg')
            self.send_response(200)
            self.send_header('Content-type',mime)
            self.end_headers()
            # Send the html message
            self.wfile.write(content)
            
            
            

server = HTTPServer(('', PORT), myHandler)
print('Started httpserver on port ', PORT)

#Wait forever for incoming http requests
server.serve_forever()