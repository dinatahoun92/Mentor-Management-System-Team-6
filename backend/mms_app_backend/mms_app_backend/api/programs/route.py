from fastapi import APIRouter, Response, status, Depends
from sqlalchemy.orm import Session

from .constants import PROGRAM_EXISTS_MESSAGE, PROGRAM_CREATE_SUCCESS_MESSAGE
from .crud import create_program_crud
from .responses import CreateProgramResponse
from .schemas import CreateProgram
from ..account_management.models import Program
from ..authentication.constants import INVALID_AUTHENTICATION_MESSAGE
from ..authentication.helpers import verify_access_token
from ..utils import get_db, get_token

router = APIRouter()
get = router.get
post = router.post


@post('/users/programs', status_code=status.HTTP_201_CREATED, response_model=CreateProgramResponse)
def create_program(program: CreateProgram, response: Response, db: Session = Depends(get_db),
                   jwt_token: str = Depends(get_token())):
    user = verify_access_token(db, jwt_token)
    program_response = CreateProgramResponse()
    db_program = db.query(Program).filter(Program.name == program.name).first()
    if not user:
        program_response.message = INVALID_AUTHENTICATION_MESSAGE
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return program_response
    if db_program:
        program_response.message = PROGRAM_EXISTS_MESSAGE
        response.status_code = status.HTTP_409_CONFLICT
        return program_response
    if not db_program:
        db_program = create_program_crud(db, program)
        program_response.message = PROGRAM_CREATE_SUCCESS_MESSAGE
        program_response.data.program = db_program
        program_response.success = True

    return program_response