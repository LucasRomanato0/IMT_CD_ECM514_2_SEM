import os
from flask import Flask, request
from src.modules.get_similar_notices.app.get_similar_notices_presenter import get_similar_notices_presenter
from src.shared.helpers.external_interfaces.http_flask import FlaskHttpRequest, FlaskHttpResponse
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def health_check():
    return "Similarity Search Finep API is running"


def flask_route(request, presenter):
    flask_request = FlaskHttpRequest(request)
    res = presenter(flask_request)
    return FlaskHttpResponse(body=res.body, status_code=res.status_code).to_flask_response()


@app.route('/get-similar-notices', methods=['POST'])
def get_similar_notices():
    return flask_route(request, get_similar_notices_presenter)


def rag_api(request):
    with app.request_context(request.environ):
        try:
            rv = app.preprocess_request()
            if rv is None:
                rv = app.dispatch_request()
        except Exception as e:
            rv = app.handle_user_exception(e)
        response = app.make_response(rv)
        return app.process_response(response)


if os.getenv('ENV') == 'DEV':
    if __name__ == '__main__':
        print('Running in DEV mode')
        app.run(debug=True)
