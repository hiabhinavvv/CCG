from .models import Base
from .database import engine  # ✅ Import from database.py

def init_db():
    """Initialize database tables"""
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    init_db()
    print("Database initialized!")
