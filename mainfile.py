import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import  request

# ==================================CRUD operations for employee table==========================
@app.route('/emp',methods=['GET'])
def emp():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM rest_emp")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/add_employee', methods=['POST'])
def addEmployee():
    try:
        _json = request.json
        _id = _json['id']
        _name = _json['name']
        _age = _json['age']
        if _id and  _name and _age and request.method == 'POST':
            sqlQuery = "INSERT INTO rest_emp(id, name, age) VALUES(%s, %s, %s)"
            bindData = (_id, _name, _age)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Employee added successfully!')
            respone.status_code = 200
            return respone
        else:
            return not_found()
    except Exception as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


@app.route('/update', methods=['PUT'])
def update():
    try:
        _json = request.json
        _id = _json['id']
        _name = _json['name']
        _age = _json['age']
        if _id and  _name and _age and request.method == 'PUT':
            sqlQuery = "UPDATE rest_emp SET id=%s, name=%s, age=%s"
            bindData = ( _id,_name,_age)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Employee updated successfully!')
            respone.status_code = 200
            return respone
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/delete/<int:id>',methods=['DELETE'])
def delete(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM rest_emp WHERE id=%s", (id,))
        conn.commit()
        resp = jsonify('User deleted successfully!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

# ======================================== CRUD operations for employee project details table=====================
@app.route('/emp_project',methods=['GET'])
def empProject():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM emp_project")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_project', methods=['POST'])
def addProject():
    try:
        _json = request.json
        _project_id = _json['project_id']
        _emp_id = _json['emp_id']
        _project_name = _json['project_name']
        _domain_name = _json['domain_name']
        if _project_id and  _emp_id and _project_name and _domain_name and request.method == 'POST':
            sqlQuery = "INSERT INTO emp_project(project_id,emp_id,project_name,domain_name) VALUES(%s, %s, %s,%s)"
            bindData = (_project_id, _emp_id, _project_name,_domain_name)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Employee project details added successfully!')
            respone.status_code = 200
            return respone
        else:
            return not_found()
    except Exception as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

@app.route('/update_project', methods=['PUT'])
def updateProject():
    try:
        _json = request.json
        _project_id = _json['project_id']
        _emp_id = _json['emp_id']
        _project_name = _json['project_name']
        _domain_name = _json['domain_name']
        if _project_id and  _emp_id and _project_name and _domain_name and request.method == 'PUT':
            sqlQuery = "UPDATE emp_project SET project_id=%s, emp_id=%s, project_name=%s,domain_name=%s"
            bindData = (_project_id,_emp_id,_project_name,_domain_name)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('project details  updated successfully!')
            respone.status_code = 200
            return respone
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/delete_project/<int:id>',methods=['DELETE'])
def deleteProject(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM emp_project WHERE project_id=%s", (id,))
        conn.commit()
        resp = jsonify('project deleted successfully!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


# =============== CRUD operations for employee family details table ======================

#
# insert into emp_family(ID,emp_id,Relation,Gender)values(2,2,"Sister","F")
@app.route('/emp_family',methods=['GET'])
def empFamily():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM emp_family")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/add_family_details', methods=['POST'])
def familyDetails():
    try:
        _json = request.json
        _ID = _json['ID']
        _emp_id = _json['emp_id']
        _Relation = _json['Relation']
        _Gender = _json['Gender']
        if _ID and  _emp_id and _emp_id and _Relation and _Gender and  request.method == 'POST':
            sqlQuery = "INSERT INTO emp_family(ID,emp_id,Relation,Gender) VALUES(%s, %s, %s,%s)"
            bindData = (_ID, _emp_id,_Relation,_Gender)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Employee project details added successfully!')
            respone.status_code = 200
            return respone
        else:
            return not_found()
    except Exception as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


@app.route('/delete_family_details/<int:id>',methods=['DELETE'])
def deleteFamilyMember(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM emp_family WHERE ID=%s", (id,))
        conn.commit()
        resp = jsonify('family member deleted successfully!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/update_family_details', methods=['PUT'])
def updateFamilyMember():
    try:
        _json = request.json
        _ID = _json['ID']
        _emp_id = _json['emp_id']
        _Relation = _json['Relation']
        _Gender = _json['Gender']
        if _ID and _emp_id and _emp_id and _Relation and _Gender and request.method == 'PUT':
            sqlQuery = "UPDATE emp_family SET project_id=%s, emp_id=%s, project_name=%s,domain_name=%s"
            bindData = (_ID,_emp_id,_Relation,_Gender)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('family details  updated successfully!')
            respone.status_code = 200
            return respone
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()



@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone

if __name__ == "__main__":
    app.run(debug=True)
