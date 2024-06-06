from flask import Flask, make_response, request
import json


app = Flask(__name__)

with open('customers.json') as file:
    customers = json.load(file)

@app.get('/customers')
def handle_get_customers():
    page_size = 10
    page_offset = 0

    if 'page' in request.args:
        page_offset = (int(request.args['page']) - 1) * page_size

    response = make_response(json.dumps(customers[page_offset: page_offset+page_size+1]))
    response.headers['Content-Type'] = 'application/json'
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6789, debug=True)
