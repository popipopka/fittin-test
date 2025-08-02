from typing import Any, AsyncGenerator

from aiosmtplib import SMTP

from src.config import app_config


async def get_smtp_client() -> AsyncGenerator[SMTP, Any]:
    client = SMTP(
        hostname=app_config.smtp.server,
        port=app_config.smtp.port
    )
    await client.connect()
    await client.login(app_config.smtp.username, app_config.smtp.password)

    try:
        yield client
    finally:
        await client.quit()
