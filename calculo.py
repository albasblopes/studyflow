from flask import render_template, request, redirect
from models import Assunto, CicloEstudo, CicloAssunto
from database import db, lm
from flask import Blueprint, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import current_user
from main import app
from sqlalchemy.sql import func
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import select

last_ciclo = CicloEstudo.query.filter_by().order_by(CicloEstudo.id.desc()).first().id
id_usuario = current_user.id
@app.route('/teste2')
def teste1():
  q_horas = CicloEstudo.query.filter_by(id = last_ciclo).first().duracao_ciclo
  return str(q_horas)

@app.route('/teste3')
def teste2():
  q_horas2 = CicloEstudo.query.filter_by(id_usuario = current_user.id).first().duracao_ciclo
  return str(q_horas2) 

  q_materias = CicloAssunto.query.filter_by(last_ciclo= CicloAssunto.id_ciclo).count(CicloAssunto)
  
  id_assunto_ciclo_assunto = CicloAssunto.query.filter_by(id_ciclo = last_ciclo).all().id_assunto
  total_nf = Assunto.query.filter_by(id = id_assunto_ciclo_assunto).func.sum(Assunto.nf).first().nf
  
  q_partes = q_horas/total_nf
  
  nf_materia = select(Assunto.nf).join(CicloAssunto, CicloAssunto.id == Assunto.id).where(CicloAssunto.id_ciclo == last_ciclo)

for nf_materia in q_cada_materia:
  q_cada_materia = q_horas/q_partes*nf_materia

q_materias = CicloAssunto.query.filter_by(last_ciclo=CicloAssunto.id_ciclo).count(CicloAssunto)

@app.route('/teste4')
def teste4():
  nf_materia = select(Assunto.nf).join(CicloAssunto, CicloAssunto.id == Assunto.id).where(CicloAssunto.id_ciclo == last_ciclo)
  return str(nf_materia)

