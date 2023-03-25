from abc import ABC
from abc import abstractmethod
from datetime import datetime

from src.bot.social_network.domain.entities.publication import Publication


class SocialNetwork(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def get_new_publications(self, last_message_date: datetime) -> list[Publication]:
        raise NotImplementedError()

    @abstractmethod
    def post(self, publication: Publication) -> None:
        raise NotImplementedError()


class SocialNetworkMock(SocialNetwork):
    def __init__(self, name: str) -> None:
        self.name = name
        self.private_messages: list[Publication] = []
        self.profile_publications: list[Publication] = []

    def get_new_publications(self, last_message_date: datetime) -> list[Publication]:
        new_publications = []
        for message in self.private_messages:
            if message.date < last_message_date:
                break
            new_publications.append(message)
        return new_publications

    def post(self, publication: Publication) -> None:
        self.profile_publications.append(publication)
