from abc import ABC
from abc import abstractmethod
from datetime import datetime


class SocialNetworkRepository(ABC):
    @abstractmethod
    def last_message_date(self, social_network_name: str) -> datetime:
        raise NotImplementedError()

    @abstractmethod
    def update_last_message_date(self, social_network_name: str, date: datetime) -> None:
        raise NotImplementedError()


class SocialNetworkRepositoryMock(SocialNetworkRepository):

    def __init__(self, database: dict[str, datetime]) -> None:
        self.database: dict[str, datetime] = database

    def last_message_date(self, social_network_name: str) -> datetime:
        return self.database[social_network_name]

    def update_last_message_date(self, social_network_name: str, date: datetime) -> None:
        self.database[social_network_name] = date
