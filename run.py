from app import app
from app.routes.auth import auth_blueprint

app.register_blueprint(auth_blueprint, url_prefix='/api', name='auth')

if __name__ == '__main__':
    app.run(debug=True)
