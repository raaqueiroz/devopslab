from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Aula marota de Pipeline"

if __name__ == '__main__':
    app.run(debug=True)

# print("1 + 1 = "(1+1))
# Last line