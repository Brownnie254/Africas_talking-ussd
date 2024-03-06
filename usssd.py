from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def ussd_callback():
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "").strip()

    if text == '':
        response = "CON Welcome to Mobile Phone Insurance\n"
        response += "Please select an option:\n"
        response += "1. Insure my phone against theft\n"
        response += "2. Insure my phone against accidental damage\n"
        response += "3. Insure my phone against technical malfunction\n"
        response += "4. File a claim"
    
    elif text == '0':
        response = "CON You have returned to the main menu. Please select an option:\n"
        response += "1. Insure my phone against theft\n"
        response += "2. Insure my phone against accidental damage\n"
        response += "3. Insure my phone against technical malfunction\n"
        response += "4. File a claim"

    elif text in ['1', '2', '3', '4']:
        option = int(text)
        if option == 2:
            response = "CON You've selected insurance against accidental damage.\n"
            response += "Please briefly describe the damage issue"
        elif option == 3:
            response = "CON You've selected insurance against technical malfunction.\n"
            response += "Please briefly describe the technical issue"
        elif option == 4:
            response = "CON To file a claim, please briefly describe the issue"
        else:
            response = "CON Please enter your phone's IMEI number"
    
    elif text.startswith('1*') or text.startswith('2*') or text.startswith('3*') or text.startswith('4*'):
        parts = text.split('*')
        if len(parts) == 2:
            imei_number = parts[1]
            response = "CON Please enter your phone's type or model"
        elif len(parts) == 3:
            phone_type = parts[2]
            response = "CON Select a payment plan:\n"
            response += "1. Monthly\n"
            response += "2. Quarterly\n"
            response += "3. Annually"
        elif len(parts) == 4:
            payment_plan = parts[3]
            response = "END Thank you for selecting the payment plan.\n"
            response += "Payment Plan: " + payment_plan
            response += "\n\nYour premium payment request has been initiated. Please check your phone for payment instructions."
        else:
            response = "END Invalid input. Please try again."
    
    else:
        response = "END Invalid selection. Please try again."
    
    return response

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
