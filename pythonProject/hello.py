from flask import Flask, request, render_template, make_response
from pythonProject import pandaFunctions

app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('my-form.html')


@app.route('/', methods=['POST'])
def post_update_salary():
    employee = request.form['employee']
    salary = request.form['salary']

    pandaFunctions.changeEmployeeSalary(employee, int(salary))

    response = make_response(render_template('my-form.html'), 200)

    return response


@app.route('/<employee>/<salary>', methods=['POST'])
def post_update_salary_realworld(employee, salary):
    try:
        pandaFunctions.changeEmployeeSalary(employee, int(salary))
        response = make_response(render_template('my-form.html'), 200)
    except TypeError:
        response = make_response(render_template('my-form.html'), 500)

    return response
