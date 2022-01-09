import pytest
from django.contrib.auth import get_user_model
from .forms import LinkForm
from .models import Link
from .utils import generate_unique_slug


# Test if home page is displayed correctly
def test_home_is_displayed(client):
    req = client.get('/')
    assert b'Fill up the form to shorten your URL' in req.content
    assert req.status_code == 200

# Test sending invalid URL to the form
def test_invalid_form_data(client):
    form_data= {
        'long_url': 'invalid-url.//a'
    }

    form = LinkForm(data=form_data)

    assert not form.is_valid()


# Test sending valid URL to the form
def test_valid_form_data(client):
    form_data= {
        'long_url': 'https://www.google.fr'
    }

    form = LinkForm(data=form_data)

    assert form.is_valid()

# Test saving a short URL to the db
@pytest.mark.django_db
def test_save_url_to_db():
    url = Link.objects.create(
        long_url='http://www.google.fr', 
        short_slug=generate_unique_slug()
    )

    assert Link.objects.count() == 1
    assert url.long_url == 'http://www.google.fr'
    assert url.nb_hits == 0

# Test redirection from short URL is working
@pytest.mark.django_db
def test_redirection(client):
    url = Link.objects.create(
        long_url='https://www.google.fr', 
        short_slug=generate_unique_slug()
    )
    
    req = client.get(f'/{url.short_slug}')
    url.refresh_from_db()
    assert req.get('location') == 'https://www.google.fr'
    assert req.status_code == 302
    assert url.nb_hits == 1

# Test that a logged in user can access his created links list
@pytest.mark.django_db
def test_links_list(client):
    user = get_user_model().objects.create_user(
                email='virgin@gmail.com', 
                password='Azerty123$'
            )
    url1 = Link.objects.create(
        owner=user,
        long_url='https://www.google.fr', 
        short_slug=generate_unique_slug()
    )
    url2 = Link.objects.create(
        owner=user,
        long_url='https://www.facebook.com', 
        short_slug=generate_unique_slug()
    )

    client.login(email='virgin@gmail.com', password='Azerty123$')
    req = client.get('/my-links')

    assert req.status_code == 200
    assert f'{url1.short_slug}'.encode() in req.content
    assert f'{url2.short_slug}'.encode() in req.content