from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from datetime import datetime
from model import *

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# --- Usuarios ---
@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    data = request.get_json()
    usuario = Usuario(**data)
    db.session.add(usuario)
    db.session.commit()
    return jsonify({'mensaje': 'Usuario creado'}), 201

@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([{
        'id': u.id, 'correo': u.correo, 'rol': u.rol
    } for u in usuarios])

# --- Partidos ---
@app.route('/partidos', methods=['POST'])
def crear_partido():
    data = request.get_json()
    data['fecha'] = datetime.strptime(data['fecha'], '%Y-%m-%d').date()
    partido = Partido(**data)
    db.session.add(partido)
    db.session.commit()
    return jsonify({'mensaje': 'Partido creado'}), 201

@app.route('/partidos', methods=['GET'])
def obtener_partidos():
    partidos = Partido.query.all()
    return jsonify([{
        'id': p.id, 'fecha': p.fecha.strftime('%Y-%m-%d'),
        'lugar': p.lugar, 'equipo1': p.equipo1, 'equipo2': p.equipo2,
        'goles_equipo1': p.goles_equipo1, 'goles_equipo2': p.goles_equipo2
    } for p in partidos])

# --- Jugadores ---
@app.route('/jugadores', methods=['POST'])
def crear_jugador():
    data = request.get_json()
    jugador = Jugador(**data)
    db.session.add(jugador)
    db.session.commit()
    return jsonify({'mensaje': 'Jugador creado'}), 201

@app.route('/jugadores', methods=['GET'])
def obtener_jugadores():
    jugadores = Jugador.query.all()
    return jsonify([{
        'id': j.id, 'nombre': j.nombre, 'equipo': j.equipo,
        'posicion': j.posicion, 'edad': j.edad
    } for j in jugadores])

# --- Estadísticas Jugador-Partido ---
@app.route('/estadisticas', methods=['POST'])
def agregar_estadistica():
    data = request.get_json()
    estadistica = JugadorPartido(**data)
    db.session.add(estadistica)
    db.session.commit()
    return jsonify({'mensaje': 'Estadística registrada'}), 201

@app.route('/estadisticas', methods=['GET'])
def obtener_estadisticas():
    estadisticas = JugadorPartido.query.all()
    return jsonify([{
        'id': e.id,
        'jugador_id': e.jugador_id,
        'partido_id': e.partido_id,
        'goles': e.goles,
        'asistencias': e.asistencias,
        'tarjetas_amarillas': e.tarjetas_amarillas,
        'tarjetas_rojas': e.tarjetas_rojas
    } for e in estadisticas])

if __name__ == '__main__':
    app.run(debug=True)
