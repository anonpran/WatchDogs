from flask import Flask, request, jsonify

app= Flask(__name__)

@app.route('/verify',methods=['POST'])
def verify_identity():
    data = request.get_json()

    #in a real SSI system, the server would verify the idenity clain using cryptography and tust frameworks
    #for simplicity, assume the user sends a signed claim and the server trusts it.

    if 'signed_claim' in data:
        signed_claim = data['signed_claim']
        #verify the signature and extract the user's idenity information
        #need to add validation steps

        user_identity = "User: "+signed_claim['username']
        return jsonify({'result': 'success','identity':user_idenity})
    
    else:
        return jsonify({'result': 'error','message':'No signed claim provided'})
    
if __name__ =='__main__':
    app.run(debug=True,port=5001)