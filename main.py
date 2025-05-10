from src.config import app as app_config
import uvicorn
import debugpy

if __name__ == "__main__":
    if app_config.DEBUG:
        debugpy.listen((app_config.HOST, app_config.DEBUG_PORT))
        print(f"Debugging is running in port: {app_config.DEBUG_PORT}")

    uvicorn.run(
        "src.app:app",
        reload=app_config.DEBUG,
        host=app_config.HOST,
        port=app_config.PORT
    )
