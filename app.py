

from flask import Flask, jsonify, request

app = Flask(__name__)
app.debug = True

Students = [
    
     {
        "student_id": "101",
        "first_name": "Anish",
        "last_name": "Sharma",
        "dob": "01/01/1980",
        "amount_due": "0",
         
    },
    
     {
        "student_id": "102",
        "first_name": "Dilsher",
        "last_name": "Singh",
        "dob": "01/02/1990",
        "amount_due": "1000",
         
    },
    
 ]
 
@app.route('/Students')
def hello():
    return jsonify(Students)

#ADD

@app.route('/Students', methods=['POST'])

def add_student():

    student = request.get_json()

    Students.append(student)

    return {'id': len(Students)}, 200



#UPDATE



@app.route('/Students/<int:index>', methods=['PUT'])
def update_student(index):
    student = request.get_json()
    Students[index] = student
    return jsonify(Students[index]), 200



#DELETE

@app.route('/Students/<int:index>', methods=['DELETE'])

def delete_student(index):

    Students.pop(index)

    return 'None', 200



app.debug = True
app.run()

