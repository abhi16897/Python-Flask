from flask import Flask,jsonify,request

app = Flask(__name__)

stores=[
    {
        'name':'my First Store',
        'items':[
            {
                'name':'choclate',
                'price':'15'
            }
        ]
    },
       {
        'name':'My Second Store',
        'items':[
            {
                'name':'iceCream',
                'price':'50'
            }
        ]
    }
]

@app.route('/store',methods=["POST"])
def createStore():
    request_data=request.get_json()
    new_store={
        'name':request_data['name'],
        'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store)

@app.route('/store/<string:name>',methods=["GET"])
def getstore(name):
    for store in stores:
        print(store['name'])
        if store['name']== name:
            return jsonify(store)
    return jsonify({'message':"Store Not Found!"})

@app.route('/store')
def getstores():
    return jsonify({'stores':stores})

@app.route('/store/<string:name>/item')
def create_item_in_store(name):
    for store in stores:
        if store['name']== name:
            return jsonify({'Items':store['items']})
    return jsonify({'message':"Store Not Found!"})


app.run()