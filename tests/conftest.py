import copy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module

original_activities = copy.deepcopy(app_module.activities)


@pytest.fixture(scope="session")
def client():
    return TestClient(app_module.app)


@pytest.fixture(autouse=True)
def reset_activities():
    app_module.activities.clear()
    app_module.activities.update(copy.deepcopy(original_activities))
