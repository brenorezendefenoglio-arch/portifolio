# Importar
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

# Conteúdo da página
@app.route('/')
def index():
    return render_template('index.html')


# Habilidades Dinâmicas
@app.route('/', methods=['POST'])
def process_form():
    if request.method == 'POST':
        # Captura qual botão foi clicado
        button_anime = request.form.get('button_anime')
        button_cs2 = request.form.get('button_cs2')
        button_minecraft = request.form.get('button_minecraft')
        button_volei = request.form.get('button_volei')

        return render_template(
            'index.html',
            button_anime=button_anime,
            button_cs2=button_cs2,
            button_minecraft=button_minecraft,
            button_volei=button_volei
        )
    
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)
