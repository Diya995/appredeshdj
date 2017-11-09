#!/usr/local/bin/python 
# -*- coding: utf-8 -*-
'''------------------------------------------------------------------------------------------'''
#app.py 
'''Este modulo se encarga de brindar informacion de como usar la aplicacion en heroku 
En este archivo tambien se tienen los metodos para guardar los datos en la base de datos'''
'''------------------------------------------------------------------------------------------'''

'''------------------------------------------------------------------------------------------'''
#NOTA: Los metodos aqui especificados estan sujetos a varios cambios 
'''------------------------------------------------------------------------------------------'''

'''------------------------------------------------------------------------------------------'''
import os
from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy     
'''------------------------------------------------------------------------------------------'''

'''------------------------------------------------------------------------------------------'''
app = Flask(__name__)
'''------------------------------------------------------------------------------------------'''
 
'''------------------------------------------------------------------------------------------'''
#conectarBaseDatos
'''Realiza la conexion a la base de datos
Este metodo se encarga de realizar la conexion a la base de datos'''
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
bd = SQLAlchemy(app) 
'''------------------------------------------------------------------------------------------'''
 
'''------------------------------------------------------------------------------------------'''
class Maquina(bd.Model):
	id_so = bd.Column(bd.Integer, primary_key=True)
	kernel = bd.Column(bd.String(100), unique=True)
	release = bd.Column(bd.String(100), unique=True)
	nodename = bd.Column(bd.String(100), unique=True)
	kernelv = bd.Column(bd.String(100), unique=True)
	machine = bd.Column(bd.String(100), unique=True)
	processor = bd.Column(bd.String(100), unique=True)
	so = bd.Column(bd.String(100), unique=True)
	hardware = bd.Column(bd.String(100), unique=True)
	user_logged = bd.Column(bd.String(100), unique=True)
	cpu_us = bd.Column(bd.String(100), unique=True)
	cpu_sy  = bd.Column(bd.String(100), unique=True)
	cpu_id = bd.Column(bd.String(100), unique=True)
	cpu_wa = bd.Column(bd.String(100), unique=True)
	cpu_st = bd.Column(bd.String(100), unique=True)
	mem_swpd = bd.Column(bd.String(100), unique=True)
	mem_free = bd.Column(bd.String(100), unique=True)
	mem_buff  = bd.Column(bd.String(100), unique=True)
	cache = bd.Column(bd.String(100), unique=True)
	swap_si = bd.Column(bd.String(100), unique=True)
	swap_so  = bd.Column(bd.String(100), unique=True)     
    

	def __init__(self, kernel, release, nodename, kernelv, machine, processor, so, hardware, user_logged, cpu_us, cpu_sy, cpu_id, cpu_wa, cpu_st, mem_swpd, mem_free, mem_buff, cache, swap_si, swap_so):
		self.kernel = kernel
		self.release = release
		self.nodename = nodename
		self.kernelv = kernelv
		self.machine = machine
		self.processor = processor
		self.so = so
		self.hardware = hardware
		self.user_logged = user_logged
		self.cpu_us = cpu_us
		self.cpu_sy = cpu_sy 
		self.cpu_id = cpu_id
		self.cpu_wa = cpu_wa
		self.cpu_st = cpu_st
		self.mem_swpd = mem_swpd
		self.mem_free = mem_free
		self.mem_buff = mem_buff
		self.cache = cache
		self.swap_si = swap_si
		self.swap_so = swap_so 

	def __repr__(self): 
		return "<Maquina(id_so='%d', kernel='%s', release='%s', nodename='%s', kernelv='%s', machine='%s', processor='%s', so='%s', hardware='%s', usser_logged='%s', cpu_us='%s', cpu_sy='%s', cpu_id='%s', cpu_wa='%s', cpu_st='%s', mem_swpd='%s', mem_free='%s', mem_buff='%s', cache='%s', swap_si='%s', swap_so='%s')>" % (self.id_so, self.kernel, self.release, self.nodename, self.kernelv, self.machine, self.processor, self.so, self.hardware, self.user_logged, self.cpu_us, self.cpu_sy, self.cpu_id, self.cpu_wa, self.cpu_st, self.mem_swpd, self.mem_free, self.mem_buff, self.cache, self.swap_si, self.swap_so)
'''------------------------------------------------------------------------------------------'''
 
'''------------------------------------------------------------------------------------------'''
class Descargas(bd.Model):
    id_dt = bd.Column(bd.Integer, primary_key=True)
    magnet_link = bd.Column(bd.String(1000), unique=True)
    iniciada = bd.Column(bd.String(100), unique=True)
    estado_descarga = bd.Column(bd.String(100), unique=True)

    def __init__(self,magnet_link,iniciada,estado_descarga):
        self.magnet_link = magnet_link
        self.iniciada = iniciada
        self.estado_descarga = estado_descarga 
  
    def __repr__(self): 
        return "<Descargas(id_dt='%d', magnet_link='%s', iniciada='%s', estado_descarga='%s')>" % (self.id_dt, self.magnet_link, self.iniciada, self.estado_descarga)
'''------------------------------------------------------------------------------------------'''

'''------------------------------------------------------------------------------------------'''
#index
'''Vista principal con instrucciones
Este metodo se encarga de brindar una vista en HTML Plano con la informacion
de como llevar a cabo los procesos dentro de la aplicacion, todos estos se 
llevan escribiendo URLs en el navegador'''
@app.route('/', methods=['GET']) 
def index():
	return render_template('index.html') 
'''------------------------------------------------------------------------------------------'''

'''------------------------------------------------------------------------------------------'''
#actualizarEstadoMaquina
'''Actualiza el estado de la maquina
Este metodo se encarga de actualizar el estado de de la maquina'''
@app.route('/actualizarEstadoMaquina/<string:kernel>/<string:release>/<string:nodename>/<string:kernelv>/<string:machine>/<string:processor>/<string:so>/<string:hardware>/<string:user_logged>/<string:cpu_us>/<string:cpu_sy>/<string:cpu_id>/<string:cpu_wa>/<string:cpu_st>/<string:mem_swpd>/<string:mem_free>/<string:mem_buff>/<string:cache>/<string:swap_si>/<string:swap_so>', methods=['GET'])
def actualizarEstadoMaquina(kernel, release, nodename, kernelv, machine, processor, so, hardware, user_logged, cpu_us, cpu_sy, cpu_id, cpu_wa, cpu_st, mem_swpd, mem_free, mem_buff, cache, swap_si, swap_so):
	maquina = Maquina.query.filter(Maquina.id_so == 1).one()
	maquina.kernel = kernel  
	maquina.release = release
	maquina.nodename = nodename
	maquina.kernelv = kernelv
	maquina.machine = machine
	maquina.processor = processor
	maquina.so = so
	maquina.hardware = hardware
	maquina.user_logged = user_logged
	maquina.cpu_us = cpu_us
	maquina.cpu_sy = cpu_sy
	maquina.cpu_id = cpu_id
	maquina.cpu_wa = cpu_wa
	maquina.cpu_st = cpu_st
	maquina.mem_swpd = mem_swpd
	maquina.mem_free = mem_free
	maquina.mem_buff = mem_buff
	maquina.cache = cache
	maquina.swap_si = swap_si
	maquina.swap_so = swap_so 
	bd.session.commit() 
	return "	Se ha actualizado el estado de la maquina correctamente \n" 
'''------------------------------------------------------------------------------------------'''

'''------------------------------------------------------------------------------------------'''
#consultarEstadoMaquina
'''Consultar estado de la maquina
Este  metodo hace la consulta de la ultima actualizacion de estado de la maquina, almacenada
en la base de datos'''
@app.route('/consultarEstadoMaquina', methods=['GET'])
def consultarEstadoMaquina():
	maquina = Maquina.query.filter(Maquina.id_so == 1).one()
	return render_template('maquina.html', maquina = maquina)   
'''------------------------------------------------------------------------------------------'''

'''------------------------------------------------------------------------------------------'''
#consultarEstadoMaquinaParametro
'''Consultar el estado de un parametro especifico de la maquina
Este metodo se encarga de consultar la ultima actualizacion de estado de un parametro especifico 
almacenada en la base de datos
@app.route('/consultarEstadoMaquinaParametro/<string:parametro>', methods=['GET'])
def estadoMaquinaParametro(parametro):
	return """
	<p>En esta ruta puede ver el último estado registrado de su máquina LInux con el parámetro: {{parametro}}</p>'''
'''------------------------------------------------------------------------------------------'''

'''------------------------------------------------------------------------------------------'''
#ordenarDescargaTorrent
'''Ordenar la descarga de un torrent 
Este metodo se encarga de ordenar la descarga de un torrent que se hace a traves de un magnet link
 y almacena la orden en la base de datos'''
@app.route('/ordenarDescarga', methods=['POST'])
def ordenarDescarga(): 
	magnet_link = str( request.form['magnet_link'] ) 
	nuevaDescarga = Descargas(magnet_link, 'No', '0%')
	bd.session.add(nuevaDescarga)
	bd.session.commit()
	descargas = Descargas.query.order_by(Descargas.id_dt).all() 
	mensaje = "Se ha ordenado la descarga correctamente" 
	return render_template('descarga.html', mensaje = mensaje, descargas = descargas)
'''------------------------------------------------------------------------------------------'''
 
'''------------------------------------------------------------------------------------------'''
#actualizarEstadoDescarga
'''Actualiza el estado de una descarga de torrent
Este metodo se encarga de actualizar el estado de una descarga de torrent anteriormente ordenada'''
@app.route('/actualizarEstadoDescarga/<string:id_dt>/<string:estado_descarga>', methods=['GET'])
def actualizarEstadoDescarga(id_dt,estado_descarga):
	descarga = Descargas.query.filter(Descargas.id_dt == id_dt).one()
	descarga.estado_descarga = estado_descarga
	bd.session.commit() 
	return "	Se ha actualizado el estado de la descarga correctamente \n"
'''------------------------------------------------------------------------------------------'''

'''------------------------------------------------------------------------------------------'''
#consultarEstadoDescarga
'''Consultar el estado de una descarga de torrent
Este metodo se encarga de consultar el estado de una descarga de torrent anteriormente ordenada'''
@app.route('/consultarEstadoDescargas', methods=['GET'])
def consultarEstadoDescargas():
	descargas = Descargas.query.order_by(Descargas.id_dt).all()
	return render_template('descarga.html', descargas = descargas)    
'''------------------------------------------------------------------------------------------'''

'''------------------------------------------------------------------------------------------'''
#consultarNumeroDescargas
'''Consultar el estado de una descarga de torrent
Este metodo se encarga de consultar el estado de una descarga de torrent anteriormente ordenada'''
@app.route('/consultarIdFinalDescargas', methods=['GET'])
def consultarIdFinalDescargas():
	descarga_inicial = Descargas.query.order_by("id_dt desc").first()
	return str( descarga_inicial.id_dt ) 
'''------------------------------------------------------------------------------------------'''

'''------------------------------------------------------------------------------------------'''
#consultarNumeroDescargas
'''Consultar el numero de descargas de torrent
Este metodo se encarga de consultar el estado de una descarga de torrent anteriormente ordenada'''
@app.route('/consultarNumeroDescargas', methods=['GET'])
def consultarNumeroDescargas():
	return str( len(Descargas.query.order_by(Descargas.id_dt).all()) ) 
'''------------------------------------------------------------------------------------------'''

'''------------------------------------------------------------------------------------------'''
#consultarNuevasDescargas
'''Consultar las nuevas descargas de torrent
Este metodo se encarga de consultar si hay nuevas descargas de torrent ordenadas y las retorna'''
@app.route('/consultarNuevasDescargas', methods=['GET'])
def consultarNuevasDescargas(): 
	consultaNuevasDescargas = Descargas.query.filter(Descargas.iniciada == "No").all()
	numeroDescargas = str( len(consultaNuevasDescargas) )
	nuevasDescargas = ""
	for nuevaDescarga in consultaNuevasDescargas:
		nuevaDescarga.iniciada = "Si" 
		nuevasDescargas = nuevasDescargas + nuevaDescarga.magnet_link + " "
	nuevasDescargas = numeroDescargas + " " + nuevasDescargas
	bd.session.commit() 
	return nuevasDescargas
'''------------------------------------------------------------------------------------------'''
 
'''------------------------------------------------------------------------------------------'''
@app.errorhandler(404)
def notFound(error):
	return "Not found"

@app.route('/robots.txt')
def robots():
	res = app.make_response('User-agent: *\nAllow: /')
	res.mimetype = 'text/plain'
	return res
'''------------------------------------------------------------------------------------------'''

'''------------------------------------------------------------------------------------------'''
if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port, debug=True)    
'''------------------------------------------------------------------------------------------'''