from src.core.shared.params import OrderCreatedNotificationParams


def render_order_html(data: OrderCreatedNotificationParams):
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
