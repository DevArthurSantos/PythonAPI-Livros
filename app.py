from flask import Flask, jsonify, request
import json



app = Flask(__name__)

with open("livros.json", "r") as f:
    livros = json.load(f)

# salvar edição
def salvar():
    with open("livros.json", "w") as f:
        f.write(json.dumps(livros, indent=4, sort_keys=True))
    return

# Consultar
@app.route("/livros", methods=["GET"])
def getLivros():
    return jsonify(livros)


# Consultar(ID)
@app.route("/livros/<int:id>", methods=["GET"])
def getLivrosPorID(id):
    for livro in livros:
        if livro.get("id") == id:
            return jsonify(livro)


# Editar(ID)
@app.route("/livros/<int:id>", methods=["PUT"])
def editarLivrosPorID(id):
    livroAlt = request.get_json()
    for indece, livro in enumerate(livros):
        if livro.get("id") == id:
            livros[indece].update(livroAlt)
            salvar()
            return jsonify(livros[indece])


# Criar
@app.route("/livros", methods=["POST"])
def criarLivro():
    novoLivro = request.get_json()
    livros.append(novoLivro)
    salvar()
    return jsonify(livros)


# Deletar(ID)
@app.route("/livros/<int:id>", methods=["DELETE"])
def apagarLivro(id):
    for indece, livro in enumerate(livros):
        if livro.get("id") == id:
            del livros[indece]
            salvar()
            return jsonify(livros)


app.run(port=5000, host="localhost", debug=True)
