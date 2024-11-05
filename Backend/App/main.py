from fastapi import FastAPI
from .routes import pdf_routes
import asyncpg
from .config import DATABASE_URL

app = FastAPI()

async def lifespan(app: FastAPI):
    # Create a connection pool on startup
    app.state.pool = await asyncpg.create_pool(DATABASE_URL)
    yield  # This indicates that the app is ready
    # Close the connection pool on shutdown
    await app.state.pool.close()

# Set the lifespan handler
app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Welcome to the PDF Q&A API"}

@app.get("/health-check")
async def health_check():
    try:
        # Attempt to create a connection pool to check DB connectivity
        pool = await asyncpg.create_pool(DATABASE_URL)
        await pool.fetch("SELECT 1")  # Simple query to check connectivity
        await pool.close()  # Close the pool
        return {"status": "Database connection successful"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed: {str(e)}")

# Include routes with a prefix
app.include_router(pdf_routes.router, prefix="/api")
