from src.bot.inbox.domain.entities.publication import Publication
from src.bot.inbox.domain.inbox_adapter import TestInbox
from src.bot.inbox.services import read_last


def test_get_last_publication_of_non_empty_inbox():
    inbox = TestInbox()
    last_publication = Publication()
    for _ in range(5):
        inbox.msgs.append(Publication())
    inbox.msgs.append(last_publication)
    assert read_last(inbox) is last_publication


def test_get_last_publication_of_empty_inbox():
    inbox = TestInbox()
    assert read_last(inbox) is None
