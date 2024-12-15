from fastapi import APIRouter

from ml_ops_labs.ml_api.web.api.echo.schema import Message

router = APIRouter()


@router.post("/echo", response_model=Message)
async def send_echo_message(
    incoming_message: Message,
) -> Message:
    """
    Sends echo back to user.

    :param incoming_message: incoming message.
    :returns: message same as the incoming.
    """
    return incoming_message
