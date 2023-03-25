from datetime import datetime

from src.bot.social_network.domain.entities.publication import Publication
from src.bot.social_network.domain.repository import SocialNetworkRepositoryMock
from src.bot.social_network.domain.social_network import SocialNetworkMock


def post_new_messages(
    social_networks: list[SocialNetworkMock],
    social_network_repository: SocialNetworkRepositoryMock,
) -> None:
    new_publications = []
    for social_network in social_networks:
        last_message_date = social_network_repository.last_message_date(social_network.name)
        publications: list[Publication] = social_network.get_new_publications(last_message_date)
        social_network_repository.update_last_message_date(social_network.name, datetime.utcnow())
        new_publications.extend(publications)
    for publication in new_publications:
        for social_network in social_networks:  # noqa: WPS440
            social_network.post(publication)
