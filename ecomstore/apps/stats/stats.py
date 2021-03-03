import os
import base64


def tracking_id(request):
    if 'tracking_id' in request.session:
        return request.session['tracking_id']
    else:
        request.session['tracking_id'] = base64.b64encode(os.urandom(36))
        return request.session['tracking_id']


# TODO - add recently viewed and recommendation functions
