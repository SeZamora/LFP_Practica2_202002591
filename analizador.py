from email import message
import imp
from filelock import AcquireReturnProxy
from os import system, startfile

from taken import Token 
from errores import Error
from Etiquetas import Atributos
ListaAtributos = []
Entrada1 = ''

class AnalizadorLexico:
    letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s", "t", "u","v","w","x","y","z","ñ","Ñ"] 
    digitos=  ["1","2","3","4","5","6","7","8","9","0", "!","-","<",">"]
    numeros=  ["1","2","3","4","5","6","7","8","9","0", "(", ".",")",'"',"!","-","<",">"]
    numeros2=  ["1","2","3","4","5","6","7","8","9","0"]
    listaTokens  = []
    listaErrores = []
    ListaObjetos = []
    ListaAuxiliar2 = []
    ListaAuxiliar3 = []
    

   
    
    def AnalizadorLexico(self, Entrada):
        self.listaTokens = []
        self.listaErrores = []
        self.ListaObjetos = []
        self.ListaAuxiliar2 = []
        self.ListaAuxiliar3 = []
        linea = 1
        columna = 1
        
        buffer = ''
        estado = 0
        i = 0
        acepto=0
        while i< len(Entrada):
            c = Entrada[i]
            j=0
            if acepto == 1:
                break
            while j< len(Entrada):
                a = Entrada[j]

                if estado == 0:
                   
                    if (c.lower() in self.letras) or (c in self.digitos) :
                        buffer += c
                        columna += 1
                        i=i+1
                    elif buffer.lower() == "<!--controles":
                       
                        estado = 1 
                        buffer = ""
                        i=i+1
                    elif c == '\n':
                        columna = 1
                        linea += 1
                        i=i+1
                    elif c in ['\t',' ']:
                        columna += 1
                        i=i+1
                        pass
                    elif c == '\r':
                        i=i+1
                        pass
                    else:
                        buffer += c
                       
                        buffer = ''
                        columna += 1
                        i=i+1
                    break
                elif estado == 1:
                    
                    
                    if (c.lower() in self.letras) :
                        buffer += c
                        columna += 1
                        i=i+1
                    elif buffer.lower() == "contenedor":
                        etiqueta = ""
                        etiqueta = buffer
                        
                        
                        buffer = ''
                        estado = 2
                        i=i+1
                    elif buffer.lower() == "boton":
                        etiqueta = ""
                        etiqueta = buffer
                        
                        buffer = ''
                        estado = 2
                        i=i+1
                        
                    elif buffer.lower() == "clave":
                        etiqueta = ""
                        etiqueta = buffer
                        
                        buffer = ''
                        estado = 2
                        i=i+1
                        
                    elif buffer.lower() == "etiqueta":
                        etiqueta = ""
                        etiqueta = buffer
                         
                        buffer = ''
                        estado = 2
                        i=i+1
                        
                    elif buffer.lower() == "texto":
                        etiqueta = ""
                        etiqueta = buffer
                         
                        buffer = ''
                        estado = 2
                        i=i+1
                        
                    elif buffer.lower() == "check":
                        etiqueta = ""
                        etiqueta = buffer
                         
                        buffer = ''
                        estado = 2
                        i=i+1
                        
                    elif buffer.lower() == "radioboton":
                        etiqueta = ""
                        etiqueta = buffer
                         
                        buffer = ''
                        estado = 2
                        i=i+1
                        
                    elif buffer.lower() == "areatexto":
                        etiqueta = ""
                        etiqueta = buffer
                         
                        buffer = ''
                        estado = 2
                        i=i+1
                        
                    elif c == '\n':
                        columna = 1
                        linea += 1
                        i=i+1
                    elif c in ['\t',' ']:
                        columna += 1
                        i=i+1
                        
                    elif buffer.lower() == "controles":
                        acepto = 1
                        break
                    else:
                        buffer += c
                         
                        buffer = ''
                        columna += 1
                        i=i+1
                    break
                elif estado == 2:
                    
                    if c.isalpha() or c.isdigit():
                        buffer += c
                        columna += 1
                        i=i+1
                        break
                    elif c == '\n':
                        columna = 1
                        linea += 1
                        i=i+1    
                        break
                    elif c in ['\t',' ']:
                        columna += 1
                        i=i+1
                        break
                    elif c == ";":
                        columna += 1
                        id= ""
                        self.listaTokens.append(Token(buffer, "ID"))
                        id = buffer
                       
                        estado = 3
                        buffer = ""
                        i=i+1
                        ancho=None
                        alto = None
                        color1=None
                        color2=None
                        color3=None
                        texto=None
                        alineacion=None
                        marcada=None
                        grupo=None
                        posx=None
                        posy=None
                        add=None
                    else:
                        buffer += c
                         
                        buffer = ''
                        columna += 1
                        i=i+1
                        break
                        
                    
                elif estado == 3:
                    
                    if (a.lower() in self.letras) or (a in self.digitos) :
                        buffer += a
                        columna += 1
                        j=j+1
                    elif buffer.lower() == "<!--propiedades":
                        self.listaTokens.append(Token(buffer, "controles a usar "))
                        estado = 4
                        buffer = ""
                        j=j+1
                    elif buffer.lower() == "<!--colocacion":
                        self.listaTokens.append(Token(buffer, "controles a usar "))
                        estado = 6
                        buffer = ""
                        j=j+1
                    elif a == '\n':
                        columna = 1
                        linea += 1
                        buffer=""
                        j=j+1
                    elif a in ['\t',' ']:
                        columna += 1
                        j=j+1


                        
                    elif a == '\r':
                        j=j+1
                        
                    else:
                        buffer += a
                         
                        buffer = ''
                        columna += 1
                        j=j+1
                elif estado == 4:
                    
                    if (a.lower() in self.letras) or (a in self.numeros) :
                        buffer += a
                        columna += 1
                        j=j+1
                    elif a == '\n':
                        columna = 1
                        linea += 1
                        j=j+1
                    elif a in ['\t',' ']:
                        columna += 1
                        j=j+1
                        pass
                    elif a == '\r':
                        j=j+1
                        pass
                    elif buffer == ";":
                        buffer=""
                    else:
                        buffer += a
                         
                        buffer = ''
                        columna += 1
                        j=j+1

                    if buffer == (id+".setAncho("):
                        
                        estado = 5
                        tipo = "Ancho"
                        buffer=""
                    elif buffer == (id+".setAlto("):
                        
                        estado = 5
                        tipo = "Alto"
                        buffer=""
                    elif buffer == (id+'.setTexto("'):
                        
                        estado = 5
                        tipo = "Texto"
                        buffer=""
                    elif buffer == (id+".setAlineacion("):
                        
                        estado = 5 
                        tipo = "Alineacion"
                        buffer=""
                    elif buffer == (id+".setColorFondo("):
                        
                        estado = 5
                        tipo = "Fondo"
                        buffer=""
                    elif buffer == (id+".setColorLetra("):
                        
                        estado = 5
                        tipo = "Letra"
                        buffer=""
                    elif buffer == (id+".setMarcada("):
                        
                        estado = 5
                        tipo = "Marca"
                        buffer=""
                    elif buffer == (id+".setGrupo("):
                        
                        estado = 5
                        tipo = "Grupo"
                        buffer=""
                    elif buffer.lower() == "propiedades":
                        
                        estado = 3
                        buffer = ""
                        
                        
                        

                    
                elif estado == 5:
                    if (a.lower() in self.letras) or (a in self.digitos) :
                        buffer += a
                        columna += 1
                        j=j+1
                    elif ((a==")") or (a==",")):
                        pass
                    elif (a==" "):
                        buffer +=a
                        j=j+1
                    elif(a=='"') :
                        j=j+1   
                    else:
                        buffer += a
                         
                        buffer = ''
                        columna += 1
                        j=j+1

                    if tipo == "Letra" or tipo ==  "Fondo":
                        if a == ",":
                            if color1 == None:
                                color1 = buffer
                                buffer=""
                            elif color2 == None:
                                color2=buffer
                                buffer=""
                            j=j+1
                        elif a==")":
                            color3=buffer
                            buffer=""
                            j=j+1
                            estado=4
                    elif tipo == "Ancho" or tipo == "Alto" or tipo == "Alineacion"or tipo == "Marca"or tipo == "Grupo" or tipo == "Texto":
                        if a ==")":
                            if tipo	 == "Ancho":
                                ancho = buffer
                            elif tipo == "Alto":
                                alto = buffer
                            elif tipo == "Alineacion":
                                if buffer.lower()=="centro":
                                    alineacion = "center"
                                elif buffer.lower()=="derecho":
                                    alineacion="right"
                                else:
                                    alineacion="left"
                                
                            elif tipo == "Marca":
                                marcada = buffer
                            elif tipo == "Grupo":
                                grupo = buffer
                            elif tipo == "Texto":
                                texto = buffer
                                
                            j=j+1
                            estado=4
                            buffer=""                                
                elif estado == 6:    
                    if (a.lower() in self.letras) or (a in self.numeros2) :
                        buffer += a
                        columna += 1
                        j=j+1
                    elif a == '\n':
                        columna = 1
                        linea += 1
                        j=j+1
                    elif a in ['\t',' ']:
                        columna += 1
                        j=j+1
                        pass
                    elif a == '\r':
                        j=j+1
                        pass
                    elif a == ";":
                        buffer=""
                        j=j+1
                    elif a== ".":
                        if buffer == id:
                            comp = 0
                            tipo = "Posicion"
                            buffer=""
                            estado=7
                        else: 
                            temporal = buffer
                            buffer =""
                        j=j+1
                    elif a=="(":
                        buffer=""
                        j=j+1
                    elif a==",":
                        j=j+1
                    elif a==")":
                        if buffer == id:
                            tipo ="Add"
                            add = temporal
                        else:
                            buffer=""
                            temporal=""
                        j=j+1

                    else:
                        buffer += a
                         
                        buffer = ''
                        columna += 1
                        j=j+1
                    
                    if buffer.lower() == "colocacion":
                       
                        estado = 1
                        buffer = ""
                        j=0
                        if alineacion==None:
                            alineacion="left"
                        if texto==None:
                            texto=" "
                        objeto = Atributos(etiqueta, id, alto , ancho, color1, color2 , color3, texto, alineacion, marcada, grupo, posx ,posy, add)
                        print(etiqueta, id, alto , ancho, color1, color2 , color3, texto, alineacion, marcada, grupo, posx ,posy, add)
                        self.ListaObjetos.append(objeto)
                        break
                elif estado==7:
                    if (a.lower() in self.letras) or (a in self.digitos) :
                        buffer += a
                        columna += 1
                        j=j+1
                    elif ((a==")") or (a==",")):
                        pass
                    elif a=="(":
                        if buffer.lower()=="setposicion":
                            comp = 1
                        buffer=""
                        j=j+1
                    elif(a=='"') :
                        j=j+1   
                    else:
                        buffer += a
                         
                        buffer = ''
                        columna += 1
                        j=j+1
                    
                    if tipo == "Posicion":
                        if a == ",":
                            if posx == None:
                                posx = buffer
                                buffer=""
                            j=j+1
                        elif a==")":
                            if comp == 1 :
                                posy=buffer
                                buffer=""
                                j=j+1
                                estado=6
                            else:
                                j=j+1
                                estado=6
   
    def Html(self):
        mensaje=""
        mensaje = "<!doctype html> \n" \
            "<html>\n" \
            "<head>\n" 
        mensaje+="<link href="+'"pagina.css"'+" rel="+'"stylesheet"'+" type="+'"text/css">'
        mensaje+="</head>\n" \
            "<body>\n"
        for this in self.ListaObjetos:
            
            if this.add.lower() == "this":
                mensaje += "<div id="+'"'+this.id+'">\n'
                
                for dentro in self.ListaObjetos:
                    
                    if dentro.add.lower() == this.id.lower():
                        div=1
                        div2=0
                        if dentro.etiqueta.lower() == "contenedor":
                            mensaje += "<div id="+'"'+dentro.id+'">\n'
                            
                            for dentro2 in self.ListaObjetos:
                                
                                if (dentro2.add.lower() == dentro.id.lower()):
                                    div2=1
                                    if dentro2.etiqueta.lower() == "contenedor":
                                        mensaje += "<div id="+'"'+dentro2.id+'">\n'
                                        for dentro3 in self.ListaObjetos:
                                            
                                            if dentro3.add.lower() == dentro2.id.lower():
                                                
                                                if dentro3.etiqueta.lower() == "contenedor":
                                                    mensaje += "<div id="+'"'+dentro3.id+'">\n'
                                                    mensaje += '</div>\n'
                                                elif dentro3.etiqueta.lower() == "clave":
                                                    mensaje += '<input type = "password" id="' + dentro3.id+'" value="'+dentro3.texto+'" style="text-align:'+ dentro3.alineacion+'"/>\n'
                                                elif dentro3.etiqueta.lower() == "areatexto":
                                                    mensaje += '<TEXTAREA id="'+dentro3.id+'">'+dentro3.texto+ ' </TEXTAREA>\n'
                                                elif dentro3.etiqueta.lower() == "texto":
                                                    mensaje += '<input type = "text" id="'+ dentro3.id+'" value="'+dentro3.texto+'" style="text-align:'+dentro3.alineacion+'" />\n'
                                                elif dentro3.etiqueta.lower() == "radioboton":
                                                    mensaje += '<input type="radio" name="'+dentro3.grupo+'" id="'+ dentro3.id +'"'
                                                    if dentro3.marcada.lower() == "true":
                                                        mensaje += 'checked />'+dentro3.texto+"\n"
                                                    else:
                                                        mensaje += '/>'+dentro3.texto+"\n"
                                                elif dentro3.etiqueta.lower() == "check":
                                                    mensaje += '<input type="checkbox" id="'+dentro3.id +'"'
                                                    if dentro3.marcada.lower() == "true":
                                                        mensaje += 'checked />'+dentro3.texto+"\n"
                                                    else:
                                                        mensaje += '/>'+dentro3.texto+"\n"
                                                elif dentro3.etiqueta.lower() == "boton":
                                                    mensaje += '<input type="submit" id="'+ dentro3. id + '" value="' + dentro3.texto + '" style="text-align:'+ dentro3.alineacion + '"/>\n'
                                                elif dentro3.etiqueta.lower() == "etiqueta":
                                                    mensaje += '<label id="'+dentro3.id +'">'+ dentro3.texto + '</label>\n'
                                        mensaje += "</div>\n"
                                    elif dentro2.etiqueta.lower() == "clave":
                                        mensaje += '<input type = "password" id="' + dentro2.id+'" value="'+dentro2.texto+'" style="text-align:'+ dentro2.alineacion+'"/>\n'
                                    elif dentro2.etiqueta.lower() == "areatexto":
                                        mensaje += '<TEXTAREA id="'+dentro2.id+'">'+dentro2.texto+ ' </TEXTAREA>\n'
                                    elif dentro2.etiqueta.lower() == "texto":
                                        mensaje += '<input type = "text" id="'+ dentro2.id+'" value="'+dentro2.texto+'" style="text-align:'+dentro2.alineacion+'" />\n'
                                    elif dentro2.etiqueta.lower() == "radioboton":
                                        mensaje += '<input type="radio" name="'+dentro2.grupo+'" id="'+ dentro2.id +'"'
                                        if dentro2.marcada.lower() == "true":
                                            mensaje += 'checked />'+dentro2.texto+"\n"
                                        else:
                                            mensaje += '/>'+dentro2.texto+"\n"
                                    elif dentro2.etiqueta.lower() == "check":
                                        mensaje += '<input type="checkbox" id="'+dentro2.id +'"'
                                        if dentro2.marcada.lower() == "true":
                                            mensaje += 'checked />'+dentro2.texto+"\n"
                                        else:
                                            mensaje += '/>'+dentro2.texto+"\n"
                                    elif dentro2.etiqueta.lower() == "boton":
                                        mensaje += '<input type="submit" id="'+ dentro2. id + '" value="' + dentro2.texto + '" style="text-align:'+ dentro2.alineacion + '"/>\n'
                                    elif dentro2.etiqueta.lower() == "etiqueta":
                                        mensaje += '<label id="'+dentro2.id +'">'+ dentro2.texto + '</label>\n'
                               
                            mensaje += '</div>\n'
                        elif dentro.etiqueta.lower() == "clave":
                            mensaje += '<input type = "password" id="' + dentro.id+'" value="'+dentro.texto+'" style="text-align:'+ dentro.alineacion+'"/>\n'
                        elif dentro.etiqueta.lower() == "areatexto":
                            mensaje += '<TEXTAREA id="'+dentro.id+'">'+dentro.texto+ ' </TEXTAREA>\n'
                        elif dentro.etiqueta.lower() == "texto":
                            mensaje += '<input type = "text" id="'+ dentro.id+'" value="'+dentro.texto+'" style="text-align:'+dentro.alineacion+'" />\n'
                        elif dentro.etiqueta.lower() == "radioboton":
                            mensaje += '<input type="radio" name="'+dentro.grupo+'" id="'+ dentro.id +'"'
                            if dentro.marcada.lower() == "true":
                                mensaje += 'checked />'+dentro.texto+"\n"
                            else:
                                mensaje += '/>'+dentro.texto+"\n"
                        elif dentro.etiqueta.lower() == "check":
                            mensaje += '<input type="checkbox" id="'+dentro.id +'"'
                            if dentro.marcada.lower() == "true":
                                mensaje += 'checked />'+dentro.texto+"\n"
                            else:
                                mensaje += '/>'+dentro.texto+"\n"
                        elif dentro.etiqueta.lower() == "boton":
                            mensaje += '<input type="submit" id="'+ dentro. id + '" value="' + dentro.texto + '" style="text-align:'+ dentro.alineacion + '"/>\n'
                        elif dentro.etiqueta.lower() == "etiqueta":
                            mensaje += '<label id="'+dentro.id +'">'+ dentro.texto + '</label>\n'
                
                mensaje += '</div>\n'
        mensaje+="</body>\n"
        mensaje+="</html>"
        ruta = 'ReporteTokens.html'
        archivo = open(ruta,'w')
        archivo.write(mensaje)
        startfile('ReporteTokens.html')
        print("Se ha generado el html con los reportes.") 
    
    def css(self):
        archivo=""
        for css in self.ListaObjetos:
            archivo+="#"+css.id+"{\n"
            archivo += "position:absolute;\n"
            if css.posx != None:
                archivo += "left:"+ css.posx+ "px;\n"+ "top:"+ css.posy+ "px;\n"
            if css.ancho != None:
                archivo += "width:"+ css.ancho +"px;\n"
            if css.alto != None:
                archivo += "height:"+ css.alto +"px;\n"
            if css.color1 != None:
                if css.etiqueta.lower()=="contenedor":
                    archivo += "background-color: rgb("+css.color1+","+css.color2+","+css.color3+");\n"
                else:
                    archivo += "color: rgb("+css.color1+","+css.color2+","+css.color3+");\n"
            archivo+="}\n"
        ruta = 'pagina.css'
        crear = open(ruta,'w')
        crear.write(archivo)
        print("Se ha generado el css con los reportes.") 
