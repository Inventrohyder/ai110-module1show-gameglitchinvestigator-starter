import pytest
from streamlit.testing.v1 import AppTest


@pytest.fixture
def app_test():
    """Fixture to provide a running instance of the Streamlit application for end-to-end testing."""
    at = AppTest.from_file("app.py")
    at.run()
    return at
