import asyncpg
from fastapi import HTTPException
from .config import DATABASE_URL

async def get_db_pool():
    try:
        # Create a connection pool
        pool = await asyncpg.create_pool(DATABASE_URL)
        return pool
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Could not connect to database: {str(e)}"
        )

async def execute_query(query: str, params: tuple = None, fetch: bool = True):
    pool = await get_db_pool()
    async with pool.acquire() as connection:
        try:
            if fetch:
                result = await connection.fetch(query, *params) if params else await connection.fetch(query)
                return result
            else:
                await connection.execute(query, *params) if params else await connection.execute(query)
                return None
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Database query failed: {str(e)}"
            )
        finally:
            await pool.close()