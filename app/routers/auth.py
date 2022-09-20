import httpx
import json
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.dto import UserDTO


validate_url = "http://localhost:8001/auth/users/me"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def validate_auth(token: str = Depends(oauth2_scheme)):
    async with httpx.AsyncClient() as client:
        headers = {'Authorization': 'Bearer ' + token}
        print(token)
        response = await client.get(validate_url, headers=headers)
        print(response.text)
        print(response.status_code)
        if response.status_code != 200:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Unauthorized",
                headers={"WWW-Authenticate": "Bearer"},
            )
        # j = json.load(response.text)
        # print(j)
        return True




