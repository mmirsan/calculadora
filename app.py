from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def form():
    peso = 0
    altura = 0
    imc = 0
    if (request.method == "POST"):
        peso = float(request.form.get("peso"))
        altura = float(request.form.get("altura"))
        imc = (peso/(altura*altura))
        print(peso, altura, imc)
    if imc < 18.5:
        mensaje = "Peso bajo"
    elif imc > 18.5 and imc < 24.9:
        mensaje = "Peso normal"
    elif imc > 24.9 and imc < 29.9:
        mensaje = "Sobrepeso"
    elif imc > 30.0:
        mensaje = "Obesidad"
    return render_template("formulario.html", peso=peso, altura=altura, imc=imc, mensaje=mensaje)
app.run()