from src.bot.inbox.domain.entities.publication import Publication
from src.bot.inbox.domain.inbox_adapter import InboxAdapter


def read_last(inbox: InboxAdapter) -> Publication | None:
    publication = inbox.get_last_msg()
    return publication
