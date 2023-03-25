import datetime

from src.bot.social_network import services


def test_post_new_messages(social_networks, social_network_repository):
    date = datetime.datetime.utcnow()
    services.post_new_messages(social_networks, social_network_repository)
    for social_network in social_networks:
        assert len(social_network.profile_publications) == 3
    for social_network_date in social_network_repository.database.values():
        assert social_network_date > date


def test_older_publications_are_not_posted(social_networks, social_network_repository):
    social_network_repository.database['Twitter'] = datetime.datetime.utcnow()
    services.post_new_messages(social_networks, social_network_repository)
    for social_network in social_networks:
        assert len(social_network.profile_publications) == 1
