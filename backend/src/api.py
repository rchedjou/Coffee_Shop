from crypt import methods
import os
from webbrowser import get
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

'''
@TODO uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
!! Running this funciton will add one
'''
# db_drop_and_create_all()

# ROUTES
'''
@TODO implement endpoint
    GET /drinks
        it should be a public endpoint
        it should contain only the drink.short() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks')
def retrive_drink():
    selection_drinks = Drink.query.all()
    drinks = [drink.short() for drink in  selection_drinks]
    if (len(drinks)==0):
        abort(404)
    else :
        print(drinks)
        return jsonify({
            "succes" : "True",
            "drinks" : drinks
        })
    

'''
@TODO implement endpoint
    GET /drinks-detail
        it should require the 'get:drinks-detail' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks-detail')
@requires_auth('get:drinks-detail')
def retrive_drinks_detail(jwt):
    # print(jwt)
    selection_drinks_details = Drink.query.all()
    drinks = [drink.long() for drink in  selection_drinks_details]
    if (len(drinks)==0):
        abort(404)
    else :
        return jsonify({
            "succes" : "True",
            "drinks" : drinks
        })
    

'''
@TODO implement endpoint
    POST /drinks
        it should create a new row in the drinks table
        it should require the 'post:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the newly created drink
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def create_drink(jwt):
    # print(jwt)
    body = request.get_json()
    
    title = body.get("title", None)
    recipe = body.get("recipe", None)
    print(body)
    try:
        drink = Drink(title=title, recipe=json.dumps(recipe))
        drink.insert()
        
        return jsonify({
            "success" : True,
            "drinks" : [drink.long()]
        })
    except:
        abort(422)
    # print(drink.id)
    

'''
@TODO implement endpoint
    PATCH /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should update the corresponding row for <id>
        it should require the 'patch:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the updated drink
        or appropriate status code indicating reason for failure
'''


@app.route('/drinks/<int:id_drink>', methods=['PATCH'])
@requires_auth('patch:drinks')
def update_drink(jwt, id_drink):
    # print(jwt)
    drink = Drink.query.get(id_drink)
    if drink:
        try:
            body = request.get_json()
            title = body.get('title')
            recipe = body.get('recipe')  
            
            if title:
                drink.title = title
            if recipe:
                drink.recipe = json.dumps(recipe)
                
            drink.update()
            
            return jsonify({
                "success" : True,
                "drinks" : [drink.long()]
            })
            
        except Exception:
            abort(422)
    else:
        abort(404)

'''
@TODO implement endpoint
    DELETE /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should delete the corresponding row for <id>
        it should require the 'delete:drinks' permission
    returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
        or appropriate status code indicating reason for failure
'''

@app.route("/drinks/<int:id_drink>", methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drinks(jwt, id_drink):
    # print(jwt)
    try:
        drink=Drink.query.filter(Drink.id==id_drink).one_or_none()
        if drink is None:
            abort(404)
        drink.delete()
    except:
        abort(422)
        
    return jsonify({
        "succes":True,
        "delete": id_drink
    })
    



# Error Handling
'''
Example error handling for unprocessable entity
'''

@app.errorhandler(422)
def unprocessable(error):
    return (jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422)


'''
@TODO implement error handlers using the @app.errorhandler(error) decorator
    each error handler should return (with approprate messages):
             jsonify({
                    "success": False,
                    "error": 404,
                    "message": "resource not found"
                    }), 404

'''

'''
@TODO implement error handler for 404
    error handler should conform to general task above
'''
@app.errorhandler(404)
def not_found(error):
    return (
        jsonify({"success": False, "error": 404, "message": "resource not found"}),
        404
    )


'''
@TODO implement error handler for AuthError
    error handler should conform to general task above
'''
@app.errorhandler(AuthError)
def handle_auth_error(error):
    print(error.error)
    return(
        jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error.get('code')
        }), error.status_code
    )
