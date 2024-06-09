from app import create_app

_app = create_app()
_app.run(debug=True, host='0.0.0.0')