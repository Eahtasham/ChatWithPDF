import asyncpg
from fastapi import FastAPI, HTTPException
from typing import Optional, Tuple, List, Any
import logging
from .config import DATABASE_URL

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
pool: Optional[asyncpg.Pool] = None

async def get_db_pool():
    global pool
    if pool is None:
        try:
            # Create a connection pool with a maximum of 10 connections
            pool = await asyncpg.create_pool(DATABASE_URL, max_size=10)
            logger.info("Database connection pool created.")
        except Exception as e:
            logger.error(f"Could not connect to database: {str(e)}")
            raise HTTPException(
                status_code=500,
                detail=f"Could not connect to database: {str(e)}"
            )

async def execute_query(query: str, params: Optional[Tuple[Any]] = None, fetch: bool = True) -> Optional[List[dict]]:
    await get_db_pool()  # Ensure the pool is created
    async with pool.acquire() as connection:
        try:
            if fetch:
                result = await connection.fetch(query, *params) if params else await connection.fetch(query)
                return result
            else:
                await connection.execute(query, *params) if params else await connection.execute(query)
                return None
        except Exception as e:
            logger.error(f"Database query failed: {str(e)}")
            raise HTTPException(
                status_code=500,
                detail=f"Database query failed: {str(e)}"
            )

@app.on_event("startup")
async def startup():
    await get_db_pool()  # Create the database connection pool

@app.on_event("shutdown")
async def shutdown():
    if pool is not None:
        await pool.close()  # Close the connection pool on shutdown
        logger.info("Database connection pool closed.")