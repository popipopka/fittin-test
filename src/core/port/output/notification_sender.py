from abc import ABC, abstractmethod

from src.core.shared.params import OrderCreatedNotificationParams


class NotificationSender(ABC):
    @abstractmethod
    async def send_order_created(self, params: OrderCreatedNotificationParams):
        pass
