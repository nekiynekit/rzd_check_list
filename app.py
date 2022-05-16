from tabnanny import check
from flask import Flask, redirect, render_template, request, current_app
from config import Config
from forms import SearchForm, CheckListForm
from flask_sqlalchemy import SQLAlchemy
from tools import serialize_list, serialize_str, serialized


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

class CheckList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, index=True, unique=True)
    pickled_list = db.Column(db.Text, nullable=False)


@app.route('/', methods=['GET', 'POST'])
def start_page():
    return render_template('start_page.html')

@app.route('/find', methods=['GET', 'POST'])
def find_check_list():
    form = SearchForm()
    if form.validate_on_submit():
        check_list_name = form.search_request.data
        check_list = CheckList.query.filter_by(name=str(check_list_name)).all()
        if len(check_list) == 0:
            return render_template('find_check_list.html', form=form, request_message=f'Чек-листа {check_list_name} не существует!')
        else:
            print(check_list)
            return redirect(f'/check_list/{check_list_name}')

    return render_template('find_check_list.html', form=form, request_message='')

@app.route('/check_list/<name>')
def watch_check_list(name):
    check_list = CheckList.query.filter_by(name=str(name)).one()
    helper_list = serialize_str(check_list.pickled_list)
    print(helper_list)
    print(check_list.pickled_list)
    helper_list = [(idx + 1, item) for idx, item in enumerate(helper_list)]
    return render_template('night_watch.html', name=check_list.name, items=helper_list)

@app.route('/create', methods=['GET', 'POST'])
def create_check_list():
    try:
        name = request.form['list_name']
    except:
        return render_template('create_check_list.html')
    flag = '1'
    indx = 1
    check_list = []
    print(request.form)
    while flag != 'No data':
        check_list.append(request.form.get(f'item{indx}', 'No data'))
        indx += 1
        flag = check_list[-1]
    check_list.pop()
    print(f'Ты создал {check_list}')
    if serialized(check_list):
        db.session.add(CheckList(name=name, pickled_list=serialize_list(check_list)))
        db.session.commit()
    else:
        return f"""'{serialize_str(serialize_list(check_list))}' != '{check_list}'"""
    return redirect('/')