def hello(event, context):
    query_params = event.get("queryStringParameters") or {}
    name = query_params.get("name", "World")
    return {"statusCode": 200, "body": f"Hello, {name}!"}
