import logging
from logging.handlers import RotatingFileHandler
import app.settings as settings
from app.get_data.ipea import get_ipea_data, get_territorios
from app.send_data.load_ipea import load, load_territorios

logging.basicConfig(level=settings.LOG_LEVEL)
log = logging.getLogger(__name__)


def main():
    log.info("Running... ")
    load_territorios()
    # load(settings.DATA_DIR)
    log.info("... END!")


if __name__ == "__main__":
    main()
