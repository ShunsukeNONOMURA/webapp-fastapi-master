

# from sqlmodel import Session
# from app.ddd.application.usecase.user import CreateUserUseCase
# from app.ddd.infrastructure.database.db import get_session
# from app.ddd.infrastructure.uow import UserUnitOfWorkImpl
# def __usecase(session: Session = Depends(get_session)) -> CreateUserUseCase:
#     return CreateUserUseCase(uow=UserUnitOfWorkImpl(session))

from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.ddd.presentation.endpoint.token.router import router
from app.ddd.presentation.schema.token import CreateTokenResponse

# from fastapi.param_functions import Form
# class CustomOAuth2PasswordRequestForm:
#     def __init__(
#         self,
#         username: str = Form(),
#         password: str = Form(),
#     ):
#         self.username = username
#         self.password = password

@router.post(
    path="/token",
    response_model=CreateTokenResponse,
    # responses={
    #     status.HTTP_409_CONFLICT: UserDuplicationError(user_id="dammy").response(),
    # },
)
def create_token(
    # request: CreateUserRequest,
    # usecase: CreateUserUseCase = Depends(__usecase),
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> CreateTokenResponse:
    """トークンを作成する."""
    # input_dto: CreateUserInputDTO = CreateUserInputDTO.model_validate(request)
    # dto: CreateUserOutputDTO = usecase.execute(input_dto)
    # return CreateUserResponse.model_validate(dto)

    print("token")
    print(form_data.username)
    print(form_data.password)

    user_id = form_data.username

    from datetime import timedelta

    from app.ddd.infrastructure.auth import create_access_token
    # ACCESS_TOKEN_EXPIRE_MINUTES = 5
    access_token_expires = timedelta(minutes=5)
    access_token = create_access_token(
        data={"sub": user_id},
        expires_delta=access_token_expires
    )
    return CreateTokenResponse(
        access_token=access_token,
        # token_type=TOKEN_TYPE
    )
