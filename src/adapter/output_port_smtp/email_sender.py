from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from aiosmtplib import SMTP

from src.core.port.output import NotificationSender
from src.core.shared.params import OrderCreatedNotificationParams
from .html_render import render_order_html


class EmailSender(NotificationSender):

    def __init__(self, client: SMTP):
        self.client = client

    async def send_order_created(self, params: OrderCreatedNotificationParams):
        message = MIMEMultipart('alternative')
        message['Subject'] = f'Ваш заказ №{params.order_id} оформлен'
        message['From'] = 'your_email@gmail.com'
        message['To'] = params.user_email

        html_body = render_order_html(params)
        message.attach(MIMEText(html_body, 'html'))

        await self.client.send_message(message)