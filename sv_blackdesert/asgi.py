"""
ASGI config for sv_blackdesert project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
import quizes.routing
import users.routing
import admins.routing

from channels.auth    import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            users.routing.websocket_urlpatterns +
                # Second chat connection
            quizes.routing.websocket_urlpatterns +

            admins.routing.websocket_urlpatterns
        )
    ),
})