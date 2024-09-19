import pytest

from main import BooksCollector


@pytest.fixture
def collector():
    collector = BooksCollector()

    return collector


@pytest.fixture
def add_book():
    add_book = BooksCollector().add_new_book('Улитка на склоне')

    return add_book
