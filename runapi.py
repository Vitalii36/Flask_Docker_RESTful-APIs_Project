from core import create_app

appapi = create_app()

if __name__ == "__main__":
    appapi.run(debug=True, host='0.0.0.0', port=8000)