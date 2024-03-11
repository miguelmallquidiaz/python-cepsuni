from flask import Flask, render_template, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
# pip install -U flask-cors

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'system'
mysql  = MySQL(app)

#El cross_origin permite que se pueda llamar desde páginas web y puertos diferentes

@app.route('/api/customers/<int:id>')
@cross_origin()
def getCustomer(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT id, firstname, lastname, email, phone FROM customers WHERE id = ' + str(id))
    data = cur.fetchall()
    content = {}
    for row in data:
        content = {
        'id':row[0],
        'firstname':row[1],
        'lastname':row[2],
        'email':row[3],
        'phone':row[4],
        }
    return jsonify(content)

@app.route('/api/customers')
@cross_origin()
def getAllCustomers():
    cur = mysql.connection.cursor()
    cur.execute('SELECT id, firstname, lastname, email, phone FROM customers')
    data = cur.fetchall()
    result = []
    for row in data:
        content = {
        'id':row[0],
        'firstname':row[1],
        'lastname':row[2],
        'email':row[3],
        'phone':row[4],
        }
        result.append(content)
    return jsonify(result)

@app.route('/api/customers', methods=['POST'])
@cross_origin()
def createCustomer():
    if 'id' in request.json:
        updateCustomer()
    else:
        saveCustomer()
    return "ok"

def saveCustomer():
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO `customers` (`firstname`, `lastname`, `email`, `phone`) VALUES (%s, %s, %s, %s)",(request.json['firstname'], request.json['lastname'], request.json['email'], request.json['phone']))
    #Empaqueta todo para que mysql realice la operación
    mysql.connection.commit()
    return "Cliente Guardado"

def updateCustomer():
    cur = mysql.connection.cursor()
    cur.execute("UPDATE `customers` SET `firstname` = %s, `lastname` = %s, `email` = %s, `phone`= %s WHERE id = %s",(request.json['firstname'], request.json['lastname'], request.json['email'], request.json['phone'], request.json['id']))
    #Empaqueta todo para que mysql realice la operación
    mysql.connection.commit()
    return "Cliente Actualizado"

@app.route('/api/customers/<int:id>', methods=['DELETE'])
@cross_origin()
def removeCustomer(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM customers WHERE `customers`.`id` = " + str(id))
    #Empaqueta todo para que mysql realice la operación
    mysql.connection.commit()
    return "Cliente Eliminado"

@app.route('/')
@cross_origin()
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(None, 3000)