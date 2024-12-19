from core.utils import wait_for_page_to_load
from pytest import mark

from core.utils import log


@mark.smoke
@mark.ui
def test_title_validation(driver):
    log.info("1. Open website.")
    wait_for_page_to_load(driver)
    assert driver.title == "Example Domain", "Title is not 'Example Domain'"