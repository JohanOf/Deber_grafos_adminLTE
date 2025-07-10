from flask import Blueprint, send_file, render_template, request
from grafo_utils import grafo_a_imagen, camino_optimo_con_costera, obtener_ciudades

grafo_img_bp = Blueprint('grafo', __name__)
grafo_camino_bp = Blueprint('camino', __name__)
grafo_camino_buscar_bp = Blueprint('camino_buscar', __name__)

@grafo_img_bp.route('/grafo')
def ver_grafo():
    img = grafo_a_imagen()
    return send_file(img, mimetype='image/png')

@grafo_camino_bp.route('/camino')
def ver_camino():
    resultado = camino_optimo_con_costera()
    return render_template("camino.html", resultado=resultado)


@grafo_camino_buscar_bp.route('/camino_formulario', methods=['GET', 'POST'])
def camino_formulario():
    ciudades = obtener_ciudades()
    resultado = None

    if request.method == 'POST':
        origen = request.form.get('origen')
        destino = request.form.get('destino')
        if origen and destino and origen != destino:
            resultado = camino_optimo_con_costera(origen, destino)

    return render_template("formulario.html", ciudades=ciudades, resultado=resultado)

