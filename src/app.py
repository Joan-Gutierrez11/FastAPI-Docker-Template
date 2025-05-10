from fastapi import FastAPI
import sqlalchemy as sa

from .db.config import SessionDependency
from .config import db, app as app_config
from .utils import get_current_datetime

app = FastAPI()

@app.get('/')
async def main():
    return { 'msg': 'Hello FastAPI' }

@app.get('/config/app')
async def config_app():
    return app_config

@app.get('/config/database')
async def config_db():
    return db

@app.get('/timezone')
async def timezone():
    return {
        'code': app_config.TZ,
        'time': get_current_datetime(as_string=True)
    }

@app.get('/check-db')
async def check_db(db: SessionDependency):
    return {
        'session_open': True if db.connection() else False
    }
