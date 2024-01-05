from .auth import auth_blueprint

def init_app(app):
    app.register_blueprint(auth_blueprint, url_prefix='/api', name='auth')
