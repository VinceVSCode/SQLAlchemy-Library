# main_api.py will be the entry point for the FastAPI application.
# It will set up the FastAPI app and include the router from the api.routes module.

from fastapi import FastAPI
from api.routes import router
from fastapi.responses import HTMLResponse

# Create the FastAPI application instance
app = FastAPI()

# Include the router from the api.routes module
# This will register all the routes defined in the router with the FastAPI app.
app.include_router(router)

@app.get("/", response_class=HTMLResponse  )
def root_menu():
    """
    Root endpoint that returns a simple HTML response.
    This can be used to provide a welcome message or a simple UI.
    """
    return """
    <html>
        <head>
            <title>Library API Menu</title>
        </head>
        <body>
            <h1>Welcome to the Library API!</h1>
            <p>Use the endpoints to interact with the library system.</p>
            <ul>
                <li><a href="/docs">Swagger UI </a></li>
                <li><a href="/books">View all books</a></li>
                <li><a href="/users">View all users</a></li>
                <li><a href="/loans">View active loans</a></li>
            </ul>
            
        </body>
    </html>
    """