####
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

"""
@app.route("/")
def home():
    return "Home"
"""
@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John Doe test",
        "email": "john.doe@example.co.in"
    }
    
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
    
    return jsonify(user_data), 200

@app.route("/create-user", methods=["POST", "GET"])
def create_user():
    if request.method == "POST":
        data = request.get_json()
        return jsonify(data), 201  
    else:
        data = {
                "wrongMethod": "Invalid method GET, API support POST only"
            }
        return jsonify(data), 405

@app.route("/random-user", methods=["POST"])
def random_user():
    data = {}
    response = requests.get('http://127.0.0.1:5000/get-user/0987')
    if response.status_code == 200:
        #response.json()['name'] = "Jane Doe"
        data["name"]= response.json()['name']
        if data["name"] == "John Doe":
            data.pop("name")
            data["name"] = "Jane Doe"
        return jsonify(data), 200
    else:
        data = {
                "issueAPI": "Facing issues in accessing the service"
            }
        return jsonify(data), 503


# UMANG API test
@app.route("/eligibility_test", methods=["POST"])
def eligibilityTest():
    url = "https://apigw.umangapp.in/NikshayApi/ws1/stateDistrictData"
    data = {
                "tkn": "fp04a2ab2b-ee18-4a96-8f37-6f1ef8a952d2/3",
                "trkr": "213132",
                "lang": "en",
                "language": "en",
                "usrid": "3006983102",
                "mode": "web",
                "pltfrm": "windows",
                "did": None,
                "deptid": "307",
                "formtrkr": "0",
                "srvid": "1323",
                "subsid": "0",
                "subsid2": "0",
                "bearerToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ1bWFuZyIsImV4cCI6MTY0OTM0NzYwOH0.4vnkuQyQnFazwM-Q8MgXJ_bcykS3nK5HQgYdcevLpdzUjek0QpfAx825Gz5CdyKuQ8vMlQvg-gK2_K052IRZXQ"
            }
    
    Headers = {
                "x-api-key": "VKE9PnbY5k1ZYapR5PyYQ33I26sXTX569Ed7eqyg",
                "deptid": "307",
                "formtrkr": "0",
                "srvid": "1323",
                "subsid": "0",
                "subsid2": "0"
            }
    response = requests.post(url, headers=Headers, json=data)
    return response.json()

"""
    requests.get(
  'https://api.github.com/user', 
  auth=HTTPBasicAuth('username', 'password')
)
    ########
query = {'lat':'45', 'lon':'180'}
response = requests.get('http://api.open-notify.org/iss-pass.json', params=query)
print(response.json())
#######
# Create a new resource
response = requests.post('https://httpbin.org/post', data = {'key':'value'})

#####
# Update an existing resource
requests.put('https://httpbin.org/put', data = {'key':'value'})
"""
if __name__ == "__main__":
    app.run(debug=True)

