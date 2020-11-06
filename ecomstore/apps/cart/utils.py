import random


CART_ID_SESSION_KEY = 'cart_id'


def _cart_id(request):
    if request.session.get(CART_ID_SESSION_KEY, '') == '':
        request.session[CART_ID_SESSION_KEY] = _generate_cart_id()
    return request.session[CART_ID_SESSION_KEY]


def _generate_cart_id():
    cart_id = ''
    characters = (
        'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        '1234567890'
    )
    cart_id_length = 50
    for _ in range(cart_id_length):
        cart_id += characters[random.randint(0, len(characters) - 1)]

    return cart_id

