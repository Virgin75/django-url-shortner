import pytest


#@pytest.mark.django_db
@pytest.mark.urls('config.urls')
def test_home_is_displayed(client):
    page_content = client.get('/shorten').content
    assert b'Fill up the form to shorten your URL' in page_content
