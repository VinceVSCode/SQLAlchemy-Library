# main_api.py will be the entry point for the FastAPI application.
# It will set up the FastAPI app and include the router from the api.routes module.

from fastapi import FastAPI
from api.routes import router

# Create the FastAPI application instance
app = FastAPI()

# Include the router from the api.routes module
# This will register all the routes defined in the router with the FastAPI app.
app.include_router(router)

