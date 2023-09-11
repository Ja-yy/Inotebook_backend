"""AUTH -JWT
Class for JWT validation.
"""

import time
from typing import Annotated, Any, Dict

from bson.objectid import ObjectId
from fastapi import Depends, HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import ExpiredSignatureError, JWTError, jwt

from app.core.config import settings


class JWTUtils(HTTPBearer):
    """
    Utils for JWT authentication
    """

    @classmethod
    def signJWT(cls, _id) -> str:
        """
        Generates the token using email id.

        :param email: The email id of the visitor.
        :returns: token with email as payload.
        """
        payload = {
            "_id": _id,
            # expiry time of 48 hours (sec * min * hour)
            "expires": time.time()
            + 60 * 60 * int(settings.JWT_ACCESS_TOKEN_EXPIRE_HOURS),
        }
        api_token = jwt.encode(
            payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM
        )

        return api_token

    def decodeJWT(self, api_token: str) -> Dict[str, Any]:
        """
        Decode generated token.

        :param token: encrypted token string.
        :returns: decoded tokens data.
        """
        try:
            decoded_token = jwt.decode(
                api_token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
            )
            return decoded_token if decoded_token["expires"] >= time.time() else {}
        except JWTError:
            return {}

    def verifyJWT(self, jwtoken: str) -> bool:
        isTokenValid: bool = False

        try:
            payload = self.decodeJWT(jwtoken)
        except:
            payload = None
        if payload:
            isTokenValid = True
        return isTokenValid


class JWTBearer(JWTUtils):
    """
    Class for JWt authentication.

    """

    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(
            JWTBearer, self
        ).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403, detail="Invalid authentication scheme."
                )
            if not self.verifyJWT(credentials.credentials):
                raise ExpiredSignatureError(
                    status_code=403, detail="Invalid token or expired token."
                )
            payload = self.decodeJWT(credentials.credentials)
            return {"token": credentials.credentials, "payload": payload}
        else:
            raise JWTError(status_code=403, detail="Invalid authorization code.")


def get_user_id(user_detail: Annotated[Dict, Depends(JWTBearer())]) -> ObjectId:
    return ObjectId(user_detail.get("payload").get("_id"))
