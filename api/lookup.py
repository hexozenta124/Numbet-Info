from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/api/lookup", methods=["GET"])
def lookup():
    number = request.args.get("number")

    if not number or not number.isdigit() or len(number) != 10:
        return jsonify({
            "status": "error",
            "message": "Invalid number"
        })

    data = {
        "status": "success",
        "number": number,
        "country": "India",
        "carrier": "Demo Network",
        "location": "West Bengal",
        "valid": True
    }

    return jsonify(data)

# IMPORTANT for Vercel
def handler(request, context):
    return app(request.environ, start_response)
