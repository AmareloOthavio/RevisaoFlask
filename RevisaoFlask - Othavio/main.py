from flask import Flask, render_template, request, redirect

app = Flask(__name__)

filmes = []

@app.route('/')
def index():
    return render_template('index.html', filmes=filmes)

@app.route('/adicionar_filme', methods=['GET', 'POST'])
def adicionar_filme():
    if request.method == 'POST':
        nomefilme = request.form['nomefilme']
        lancamento = request.form['lancamento']
        idfilme = len(filmes)
        filmes.append([idfilme, nomefilme, lancamento])
        return redirect('/')
    else:
        return render_template('adicionar_filme.html')


@app.route('/editar_filme/<int:idfilme>', methods=['GET', 'POST'])
def editar_filme(idfilme):
    if request.method == 'POST':
        nomefilme = request.form['nomefilme']
        lancamento = request.form['lancamento']


        filmes[idfilme] = [idfilme, nomefilme, lancamento]

        return redirect('/')
    else:
        filme = filmes[idfilme]
        return render_template('editar_filme.html', filme=filme)


@app.route('/excluir_filme/<int:idfilme>')
def excluir_filme(idfilme):
    del filmes[idfilme]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)