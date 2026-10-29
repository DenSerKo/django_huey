from .base import *

HUEY = {
    'huey_class': 'huey.RedisHuey',
    'name': 'my-app',
    'url': env.str('REDIS_URL', default=''),
    'immediate': False,
}