"""This creates app that speaks with Twilio and where you can put your custom data"""
# https://www.twilio.com/docs/quickstart/python/twiml/say-response


from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)
 
# Try adding your own number to this list!
callers = {
    "+14252143104": "Curious George",
    "+14255288154": "Python",
}
 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    # Get the caller's phone number from the incoming Twilio request
    from_number = request.values.get('From', None)
    resp = twilio.twiml.Response()
 
    # if the caller is someone we know:
    if from_number in callers:
        # Greet the caller by name
        resp.say("Hello " + callers[from_number])
    else:
        resp.say("Hello Monkey")
 
    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)