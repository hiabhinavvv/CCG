from src.app import app
from src.database.init_db import init_db

# Initialize database tables on startup
init_db()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
