import pytest

from helpers import users


@pytest.fixture
def user():
    user = users.register_new_user()
    yield user
    users.delete_user(user[3])
