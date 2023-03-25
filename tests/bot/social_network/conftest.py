import datetime

import pytest

from src.bot.social_network.domain.entities.publication import Publication
from src.bot.social_network.domain.repository import SocialNetworkRepositoryMock
from src.bot.social_network.domain.social_network import SocialNetworkMock
EPOCH_YEAR = 1970


@pytest.fixture()
def social_networks():
    twitter = SocialNetworkMock('Twitter')
    twitter.private_messages.append(Publication(datetime.datetime.utcnow()))
    twitter.private_messages.append(Publication(datetime.datetime.utcnow()))
    instagram = SocialNetworkMock('Instagram')
    youtube = SocialNetworkMock('Youtube')
    youtube.private_messages.append(Publication(datetime.datetime.utcnow()))
    return [twitter, instagram, youtube]


@pytest.fixture()
def social_network_repository(social_networks):  # noqa: WPS442
    db = {
        social_networks[0].name: datetime.datetime(EPOCH_YEAR, 1, 1),
        social_networks[1].name: datetime.datetime(EPOCH_YEAR, 1, 1),
        social_networks[2].name: datetime.datetime(EPOCH_YEAR, 1, 1),
    }
    return SocialNetworkRepositoryMock(db)
