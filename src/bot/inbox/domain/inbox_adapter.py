from abc import ABC
from abc import abstractmethod

from src.bot.inbox.domain.entities.publication import Publication


class InboxAdapter(ABC):
    @abstractmethod
    def get_last_msg(self) -> Publication | None:
        raise NotImplementedError()


class TestInbox(InboxAdapter):
    def __init__(self) -> None:
        self.msgs: list[Publication] = []

    def get_last_msg(self) -> Publication | None:
        if len(self.msgs) == 0:
            return None
        last_msg = self.msgs[-1]
        return last_msg
