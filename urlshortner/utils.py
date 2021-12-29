import random
import string
from .models import Link

def generate_unique_slug():
    
    letters = string.ascii_lowercase
    digits = string.digits

    rand_letters = ''.join(
        random.choice(letters) for i in range(4)
        )
    
    rand_digits = ''.join(
            random.choice(digits) for i in range(4)
        )

    slug = rand_letters + rand_digits
    shuffled_slug = list(slug)
    random.shuffle(shuffled_slug)
    result = ''.join(shuffled_slug)

    # Check if generated slug already exists in db
    try:
        Link.objects.get(short_slug=result)
    except Link.DoesNotExist:
        # Slug does not exists in db, we can continue
        return result
    else:
        # Regenerate a new slug
        generate_unique_slug()