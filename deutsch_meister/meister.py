from starlette.applications import Starlette
from starlette.responses import JSONResponse
import uvicorn


def create_app():

    app = Starlette(debug=False)

    @app.route('/')
    async def homepage(response):
        return JSONResponse({'Hello, ': 'World!'})

    return app

app = create_app()
