import pytest

from src.driver.browser_type import BrowserType
from src.driver.web_driver_factory import init_web_driver


@pytest.fixture
class BaseTest:

    @pytest.fixture
    def setup_test(request):
        url = "https://www.aquariux.com/solutions/trader/"
        driver = init_web_driver(BrowserType.EDGE)

        yield
        # def clean_test():
        #     driver.quit()

        driver.quit()
