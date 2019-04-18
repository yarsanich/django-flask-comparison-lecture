# -*- coding: utf-8 -*-
"""Create an application instance."""
from flask.helpers import get_debug_flag

from conduit.app import create_app
from conduit.settings import DevConfig, ProdConfig

CONFIG = DevConfig if get_debug_flag() else ProdConfig

print(f'Running with {CONFIG}')

print(CONFIG.DB_PATH)

app = create_app(CONFIG)
