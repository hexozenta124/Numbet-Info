def handler(request):
    number = request.query.get("number")

    if not number or not number.isdigit() or len(number) != 10:
        return {
            "statusCode": 400,
            "body": {
                "status": "error",
                "message": "Invalid number"
            }
        }

    data = {
        "status": "success",
        "number": number,
        "country": "India",
        "carrier": "Demo Network",
        "location": "West Bengal",
        "valid": True
    }

    return {
        "statusCode": 200,
        "body": data
    }
