from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from aiosmtplib import SMTP

from src.application.repository import NotificationSender
from src.application.shared.params import OrderCreatedNotificationParams
from src.config import app_config

EMAIL_FROM_ADDRESS = app_config.smtp.email

class EmailSender(NotificationSender):

    def __init__(self, client: SMTP):
        self.client = client

    async def send_order_created(self, params: OrderCreatedNotificationParams):
        message = MIMEMultipart('alternative')
        message['Subject'] = f'Ваш заказ №{params.order_id} оформлен'
        message['From'] = EMAIL_FROM_ADDRESS
        message['To'] = params.user_email

        html_body = render_order_html_body(params)
        message.attach(MIMEText(html_body, 'html'))

        await self.client.send_message(message)


def render_order_html_body(data: OrderCreatedNotificationParams):
    items_html = "".join([
        f"<tr><td>{item.name}</td><td>{item.quantity}</td><td>{item.price:.2f}</td></tr>"
        for item in data.products
    ])

    return f"""
        <html>
          <body>
            <h2>Здравствуйте, {data.user_email}!</h2>
            <p>Спасибо за ваш заказ №{data.order_id}, оформленный {data.created_at.strftime('%Y-%m-%d %H:%M:%S')} (UTC).</p>
            <table border="1" cellpadding="5" cellspacing="0">
              <tr>
                <th>Товар</th>
                <th>Количество</th>
                <th>Цена</th>
              </tr>
              {items_html}
            </table>
            <p><strong>Итого:</strong> {data.total_price:.2f}</p>
          </body>
        </html>
        """
