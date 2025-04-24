import pytest
from seleniumbase import BaseCase

# Create a fixture for SeleniumBase
@pytest.fixture(scope="class")
def selenium_base():
    """SeleniumBase fixture."""
    class TestClass(BaseCase):
        def setUp(self):
            super().setUp()
            #  No need to start a server, we'll load the HTML directly

        def tearDown(self):
            super().tearDown()
    test_case = TestClass()
    yield test_case
    test_case.tearDown()