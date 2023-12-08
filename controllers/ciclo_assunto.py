from flask import render_template, request, flash, redirect
from models import CicloAssunto, CicloEstudo, Assunto
from database import db, lm
from flask import Blueprint, url_for
from flask_login import current_user
from sqlalchemy.sql import func
import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import select

bp_c_assunto = Blueprint("c_assunto", __name__, template_folder='templates')


@bp_c_assunto.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        assunto = Assunto.query.filter_by(id_usuario=current_user.id).all()
        return render_template('c_assunto_create.html', assunto=assunto)
    if request.method == 'POST':
        id_ciclo = CicloEstudo.query.filter_by().order_by(
            CicloEstudo.id.desc()).first().id
        ids_assuntos = request.form.getlist('checkbox')
        for id_assunto in ids_assuntos:
            ciclo_assunto = CicloAssunto(id_ciclo, id_assunto)
            db.session.add(ciclo_assunto)
            db.session.commit()

        return redirect('/')


@bp_c_assunto.route('/calculo', methods=['GET', 'POST'])
def calculo():
  last_ciclo = CicloEstudo.query.filter_by().order_by(
    CicloEstudo.id.desc()).first().id

  q_tempo = CicloEstudo.query.filter_by(id=last_ciclo).first().duracao_ciclo
  q_min = int(datetime.datetime.strftime(q_tempo, '%H')) * 60 + int(
    datetime.datetime.strftime(q_tempo, '%M'))
  dados = db.session.query(CicloAssunto, Assunto).join(CicloAssunto).filter_by(id_ciclo=last_ciclo).all()
  
  soma = 0
  for cicloassunto, assunto in dados:
    soma = int(assunto.nf) + soma

  for cicloassunto, assunto in dados:
      calculo = q_min*int(assunto.nf)/soma
      print('Tempo de estudo para {} é {}'.format(assunto.nome,calculo))
  
  #id_assunto_ciclo_assunto = db.session.query(
  #  CicloAssunto.id_assunto).filter(
  #      CicloAssunto.id_ciclo == last_ciclo).all()
  total_nf = 0
  #for CicloAssunto.id_assunto in id_assunto_ciclo_assunto:
  #  total_nf = db.session.query(func.sum(
  #     Assunto.nf).label('total')).first().total

  #q_partes = q_min / total_nf
  '''
  Session = sessionmaker(bind=engine)
  session = Session()
  nf_materia = (
      session.query(Assunto.nf)
      .join(CicloAssunto, CicloAssunto.id_assunto == Assunto.id)
      .filter(CicloAssunto.id_ciclo == last_ciclo)
      .all()
  )
  '''
  
  #Antigo
  #nf_materia = db.session.query(
  #  Assunto.nf).filter(CicloAssunto.id_ciclo == last_ciclo).all()

  #q_cada_materia = [
  #    float(nf_materia) * q_partes for q_cada_materia in nf_materia]

  #return str(nf_materia)
    # for a in nf_materia:
    #  for c in nf_materia:
    #    while c < len(nf_materia):
    #      q_cada_materia = q_partes * a[c].nf
  #return str(nf_materia)
  return 'Teste'
  
@bp_c_assunto.route('/teste/', methods=['GET', 'POST'])
def teste():
    last_ciclo = CicloEstudo.query.filter_by().order_by(
        CicloEstudo.id.desc()).first().id

    id_assunto_ciclo_assunto = db.session.query(
        CicloAssunto.id_assunto).filter(
            CicloAssunto.id_ciclo == last_ciclo).all()

    for CicloAssunto.id_assunto in id_assunto_ciclo_assunto:
        total_nf = db.session.query(func.sum(
            Assunto.nf).label('total')).first().total
    return str(total_nf)


@bp_c_assunto.route('/teste1/', methods=['GET', 'POST'])
def teste1():
    last_ciclo = CicloEstudo.query.filter_by().order_by(
        CicloEstudo.id.desc()).first().id

    q_tempo = CicloEstudo.query.filter_by(id=last_ciclo).first().duracao_ciclo
    q_min = int(datetime.datetime.strftime(q_tempo, '%H')) * 60 + int(
        datetime.datetime.strftime(q_tempo, '%M'))

    id_assunto_ciclo_assunto = db.session.query(
        CicloAssunto.id_assunto).filter(
            CicloAssunto.id_ciclo == last_ciclo).all()

    for CicloAssunto.id_assunto in id_assunto_ciclo_assunto:
        total_nf = db.session.query(func.sum(
            Assunto.nf).label('total')).first().total

    lista = db.session.query(Assunto, CicloAssunto).join(CicloAssunto).filter(
        CicloAssunto.id_ciclo == last_ciclo).all()

    for cicloassunto, assunto in lista:
        print(assunto.nf)


#q_partes = q_min / total_nf
    return str(lista)
