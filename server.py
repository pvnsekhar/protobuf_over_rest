from flask import Flask, request, Response, jsonify
import mydata_pb2
import calc_pb2
from urllib.parse import parse_qs, urlparse

from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

app.register_blueprint(get_swaggerui_blueprint('/swagger', '/static/calc.yaml'), url_prefix='/swagger')

@app.route('/send-data', methods=['POST'])
def send_data():
    try:
        # Deserialize Protobuf data from the request body
        received_data = mydata_pb2.MyData()
        received_data.ParseFromString(request.data)

        # Process the data
        print(f"Received: {received_data}")

        # Create a response
        response_data = mydata_pb2.MyData(id="123", name="Server", age=99)
        return Response(response_data.SerializeToString(), content_type='application/protobuf')
    except Exception as e:
        return str(e), 400

@app.route('/calc-data')
def calc_data():

    query_params=parse_qs(urlparse(request.url).query)
    print(query_params)
    
    request_data= calc_pb2.calc_request(
        var1=int(query_params.get('var1',['0'])[0]),
        var2=int(query_params.get('var2',['0'])[0])
    ).SerializeToString()

    inputs=calc_pb2.calc_request()
    inputs.ParseFromString(request_data)

    print(f"inputs received are :{inputs}")

    calc_response=calc_pb2.calc_response(result=int(inputs.var1*inputs.var2),success=True)
    return Response(calc_response.SerializeToString(), content_type='application/protobuf')

@app.route('/')
def hello():
    return "cool! it is working"

if __name__ == '__main__':
    app.run(debug=True)
