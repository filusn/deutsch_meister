from starlette.applications import Starlette
from starlette.responses import JSONResponse
import uvicorn


def create_app():

    app = Starlette(debug=False)

    @app.route('/')
    async def homepage(response):
        return JSONResponse({'Hello, ': 'World!'})

    @app.on_event("startup")
    async def create_db_client():
        # start client here and reuse in future requests <mongodb>


    @app.on_event("shutdown")
    async def shutdown_db_client():
        # stop client here

    return app

app = create_app()
