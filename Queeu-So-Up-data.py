from flask import Flask
from flask import jsonify
import json
from flask import json
import pymysql
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
   return 'Index API-REST Queeu' 

@app.route('/test')
def test():
    # Connect to the database
    connection = pymysql.connect(host='192.168.2.161',
                                user='Qatest',
                                password='Quito.2019',
                                db='queues',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT COUNT(Numero_Mensajes_Actual) AS Total FROM `queues` "
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
            #///////////////////////////////
            
            sql2 = "SELECT `Peticion`, substring(Time,1,19) AS Month, `Numero_Mensajes_Actual` As Sales_Figure, `Numero_Mensajes_Anterior` AS Perc FROM `queues` WHERE `TestNumero`=%s and `Peticion`>%s"
            cursor.execute(sql2, (35, 30))
            resultMensajes_Actual = cursor.fetchall()
            Mensajes_Actual = resultMensajes_Actual
            print("Mensaje: ", Mensajes_Actual)
            #print(resultMale)
            
            #///////////////////////////////
            sql3 = "SELECT  `Time` AS time FROM `queues` WHERE `TestNumero`=%s"
            cursor.execute(sql3, (19))
            resultTime = cursor.fetchall()
            TimeF = resultTime
            print("Time: ", TimeF)  
            #print(TimeF)   
          

        return jsonify(Mensajes_Actual)

    finally:
        connection.close()

if __name__ == '__main__':
   #app.run(debug=True, port=5050)
   app.run(host='192.168.2.161', debug=True, port=5067)
   #app.run(debug=True, port=5050)
   
#coemtario
 
