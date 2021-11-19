from flask import Flask, json, request, render_template
from flask_restful import Api
from dataclasses import dataclass

app = Flask(__name__, template_folder='../templates')
api = Api(app)

@dataclass
class Method:
    title: str
    data: str

@app.route('/generate',methods = ['GET'])
def result():
    file_data = open("../build/contracts/Storage.json", "r").read()
    json_contract = json.loads(file_data)
    methods = []

    for method in json_contract['abi']:
        if method['type'] == 'function':
            name = method['name']
            fullName = name + "("
            for i, inputvar in enumerate(method["inputs"]):
                if i > 0:
                    fullName = fullName + ","
                fullName = fullName + inputvar["type"]
            fullName = fullName + ")"
            methods = methods + [Method(fullName, method)]

    result = {
        'title': json_contract['contractName'],
        'source': json_contract['source'],
        'methods': methods,
        'abi': json.dumps(json_contract['abi'], indent=4),
    }

    return render_template("index.html", contract = result)

if __name__ == '__main__':
    app.run(debug=True)