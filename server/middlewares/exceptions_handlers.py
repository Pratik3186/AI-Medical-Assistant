from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from server.logger import logger

async def catch_exceptions_middleware(request:Request,call_next):
    try:
        return await call_next(request)
    except Exception as exc:
        logger.exception("UNHANDLED EXCEPTIONS")
        return JSONResponse(status_code=500,content={"error":str(exc)})
    
    
