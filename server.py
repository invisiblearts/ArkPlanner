from sanic import Sanic, response
from MaterialPlanning import MaterialPlanning

app = Sanic()

app.static('/', './static/index.html')

@app.route("/plan", methods=['POST'])
async def plan(request):
    try:
        input_data = request.json
        owned_dct = input_data["owned"]
        required_dct = input_data["required"]
    except:
        return response.json({"error": True, "reason": "Uninterpretable input"})
    mp = MaterialPlanning()
    dct = mp.get_plan_dct(required_dct, owned_dct)
    return response.json(dct)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)
