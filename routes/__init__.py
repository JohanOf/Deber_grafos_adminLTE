from .home_routes import home_bp
from .grafo_routes import grafo_img_bp, grafo_camino_bp, grafo_camino_buscar_bp

def register_blueprints(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(grafo_img_bp)
    app.register_blueprint(grafo_camino_bp)
    app.register_blueprint(grafo_camino_buscar_bp)