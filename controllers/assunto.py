from flask import render_template, request, flash, redirect
from models import Assunto, CicloEstudo
from database import db, lm
from flask import Blueprint, url_for
from flask_login import current_user

bp_assunto = Blueprint("assunto", __name__, template_folder='templates')

@bp_assunto.route('/recovery')
def recovery():
  if not current_user.admin:
    flash("Acesso não permitido")
    return redirect('/login')
    
  if request.method=='GET':
    assunto = Assunto.query.all()
    return render_template('materia_recovery.html', assunto = assunto)

@bp_assunto.route('/create', methods= ['GET', 'POST'])
def create():
  if request.method == 'GET':
    return render_template('materia_create2.html')
  if request.method == 'POST':
    id_usuario = current_user.id
    nome = request.form.get('nome')
    descricao = request.form.get('descricao')
    nf = request.form.get('nf')
    assunto = Assunto(id_usuario, nome, descricao, nf)
    db.session.add(assunto)
    db.session.commit()
    flash('Assuntos cadastrados com sucesso')
    return redirect('/assunto')

@bp_assunto.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
  assunto = Assunto.query.get(id)
  
  if request.method== 'GET':
    return render_template('materia_update2.html',  assunto = assunto)
  if request.method=='POST':
    assunto.nome = request.form.get('nome')
    assunto.descricao = request.form.get('descricao')
    assunto.peso = request.form.get('peso')
    assunto.nf = request.form.get('nf')

    db.session.add(assunto) 
    db.session.commit()
    flash('Dados atualizados com sucesso!')
    return redirect('/assunto')

@bp_assunto.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
  if request.method == 'GET':
    assunto = Assunto.query.get(id)
    return render_template('materia_delete2.html', assunto = assunto)

  if request.method == 'POST':
    assunto = Assunto.query.get(id)
    db.session.delete(assunto)
    db.session.commit()
    flash('Usuário excluído com sucesso')
    return redirect('/assunto')



@bp_assunto.route('/teste1')
def teste1():
  last_ciclo = CicloEstudo.query.filter_by().order_by(CicloEstudo.id.desc()).first().id
  
  q_tempo = CicloEstudo.query.filter_by(id = last_ciclo).first().duracao_ciclo
  q_min = int(datetime.datetime.strftime(q_tempo, '%H'))*60 + int(datetime.datetime.strftime(q_tempo, '%M'))

  id_assunto_ciclo_assunto = db.session.query(CicloAssunto.id_assunto).filter(CicloAssunto.id_ciclo == last_ciclo).all()

  for CicloAssunto.id_assunto in id_assunto_ciclo_assunto:
    total_nf = db.session.query(func.sum(Assunto.nf).label('total')).first().total

  q_partes = q_min/total_nf
  return str(q_partes)