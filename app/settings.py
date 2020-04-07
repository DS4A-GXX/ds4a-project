

# LOG SETTINGS
LOG_FORMAT = "%(asctime)s-%(levelname)s-%(name)s-:%(message)s"
SECRET_KEY = "thatslif3"

# SETTINGS BY ENV
try:
    from app.settings_production import *
except ImportError:
    pass

try:
    from app.settings_homolog import *
except ImportError:
    pass

try:
    from app.settings_local import *
except ImportError:
    pass