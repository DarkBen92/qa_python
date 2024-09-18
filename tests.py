from main import BooksCollector
import pytest
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test


class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    @pytest.mark.parametrize(
        'books',
        [['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить']]
    )
    def test_add_new_book_add_two_books(self, books):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        for name in books:
            collector.add_new_book(name)

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_name_more_than_forty_one_characters_not_add_book(self):
        collector = BooksCollector()

        collector.add_new_book('Повседневная практика показывает, что вот')
        assert len(collector.books_genre) == 0

    def test_add_new_book_repeat_book_not_add_book(self):
        collector = BooksCollector()

        collector.add_new_book('Пикник на обочине')
        collector.add_new_book('Пикник на обочине')
        assert len(collector.books_genre) == 1

    def test_set_book_genre_add_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Улитка на склоне')
        collector.set_book_genre('Улитка на склоне', 'Фантастика')
        assert collector.books_genre.get('Улитка на склоне') == 'Фантастика'

    def test_get_book_genre_is_displayed_book_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Улитка на склоне')
        collector.set_book_genre('Улитка на склоне', 'Фантастика')
        assert collector.get_book_genre('Улитка на склоне') == 'Фантастика'

    @pytest.mark.parametrize('books', [
        [
            ('Улитка на склоне', 'Фантастика'),
            ('Пила', 'Ужасы'),
            ('Пикник на обочине', 'Фантастика'),
            ('Король Лев', 'Мультфильмы'),
            ('Библиография Шерлока Холмса', 'Детективы'),
            ('Сборник анекдотов', 'Комедии')
        ]
    ])
    def test_get_books_with_specific_genre_is_displayed_by_genre(self, books):
        collector = BooksCollector()

        for name, genre in books:
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)

        assert collector.get_books_with_specific_genre('Фантастика') == ['Улитка на склоне', 'Пикник на обочине']

    @pytest.mark.parametrize('books', [
        [
            ('Улитка на склоне', 'Фантастика'),
            ('Пила', 'Ужасы'),
            ('Пикник на обочине', 'Фантастика'),
            ('Король Лев', 'Мультфильмы'),
            ('Библиография Шерлока Холмса', 'Детективы'),
            ('Сборник анекдотов', 'Комедии')
        ]
    ])
    def test_get_books_genre_is_displayed_books_genre(self, books):
        collector = BooksCollector()

        for name, genre in books:
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)

        library = collector.books_genre
        assert collector.get_books_genre() == library

    @pytest.mark.parametrize('books', [
        [
            ('Улитка на склоне', 'Фантастика'),
            ('Пила', 'Ужасы'),
            ('Пикник на обочине', 'Фантастика'),
            ('Король Лев', 'Мультфильмы'),
            ('Библиография Шерлока Холмса', 'Детективы'),
            ('Сборник анекдотов', 'Комедии')
        ]
    ])
    def test_get_books_for_children_not_in_children_books_list(self, books):
        collector = BooksCollector()

        for name, genre in books:
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)

        assert len(collector.get_books_for_children()) == 4

    @pytest.mark.parametrize('books', [
        [
            'Улитка на склоне',
            'Пила',
            'Пикник на обочине',
            'Король Лев',
            'Библиография Шерлока Холмса',
            'Сборник анекдотов'
        ]
    ])
    def test_add_book_in_favorites_add_two_books_in_favorites(self, books):
        collector = BooksCollector()

        for name in books:
            collector.add_new_book(name)

        collector.add_book_in_favorites('Пикник на обочине')
        collector.add_book_in_favorites('Библиография Шерлока Холмса')
        assert len(collector.favorites) < 3

    @pytest.mark.parametrize('books', [
        [
            'Улитка на склоне',
            'Пила'
        ]
    ])
    def test_delete_book_from_favorites_delete_one_book(self, books):
        collector = BooksCollector()

        for name in books:
            collector.add_new_book(name)
            collector.add_book_in_favorites(name)

        collector.delete_book_from_favorites('Пила')
        assert len(collector.favorites) == 1

    @pytest.mark.parametrize('books', [
        [
            'Пикник на обочине',
            'Король Лев',
            'Библиография Шерлока Холмса',
        ]
    ])
    def test_get_list_of_favorites_books_is_displayed_favorites_books(self, books):
        collector = BooksCollector()

        for name in books:
            collector.add_new_book(name)
            collector.add_book_in_favorites(name)

        assert len(collector.get_list_of_favorites_books()) == 3
