from flask_sqlalchemy import SQLAlchemy



from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    contra = db.Column(db.String(100), nullable=False)
    rol = db.Column(db.String(20), nullable=False)

class Partido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    lugar = db.Column(db.String(100), nullable=False)
    equipo1 = db.Column(db.String(50), nullable=False)
    equipo2 = db.Column(db.String(50), nullable=False)
    goles_equipo1 = db.Column(db.Integer, default=0)
    goles_equipo2 = db.Column(db.Integer, default=0)

class Jugador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    equipo = db.Column(db.String(50), nullable=False)
    posicion = db.Column(db.String(50))
    edad = db.Column(db.Integer)

class JugadorPartido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jugador_id = db.Column(db.Integer, db.ForeignKey('jugador.id'), nullable=False)
    partido_id = db.Column(db.Integer, db.ForeignKey('partido.id'), nullable=False)
    goles = db.Column(db.Integer, default=0)
    asistencias = db.Column(db.Integer, default=0)
    tarjetas_amarillas = db.Column(db.Integer, default=0)
    tarjetas_rojas = db.Column(db.Integer, default=0)
``
