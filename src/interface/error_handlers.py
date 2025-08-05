from fastapi import Request, status
from fastapi.responses import JSONResponse

from src.application.error import RecordNotFoundError, RecordAlreadyExistsError, AuthenticationError
from src.config import app_config
from src.interface.app import app


@app.exception_handler(RecordNotFoundError)
def handle_record_not_found_error(req: Request, exc: RecordNotFoundError):
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,
                        content={'detail': str(exc)})


@app.exception_handler(RecordAlreadyExistsError)
def handle_record_already_exists_error(req: Request, exc: RecordAlreadyExistsError):
    return JSONResponse(status_code=status.HTTP_409_CONFLICT,
                        content={'detail': str(exc)})


@app.exception_handler(AuthenticationError)
def handle_authentication_error(req: Request, exc: AuthenticationError):
    return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED,
                        content={'detail': str(exc)})


@app.exception_handler(Exception)
async def handle_exception_handler(req: Request, exc: Exception):
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        content={"detail": str(exc) if app_config.debug else 'Внутренняя ошибка сервера'})