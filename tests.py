from main import BooksCollector
import pytest
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test


class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.mark.parametrize(
        'normal_name_book',
        [
            'Я',
            'Agile life',
            'Тут Название Книги Ровно Сорок Символов!'
        ]
    )
    def test_add_new_book_name_lass_than_forty_one_symbols_add_book(self, collector, normal_name_book):
        collector.add_new_book(normal_name_book)
        assert len(collector.books_genre) == 1

    @pytest.mark.parametrize(
        'big_name_book',
        [
            'Повседневная практика показывает, что вот',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
            '101010101000110101101011001010010010101010101010110010110'
        ]
    )
    def test_add_new_book_name_more_than_forty_one_symbols_not_add_book(self, collector, big_name_book):
        collector.add_new_book(big_name_book)
        assert len(collector.books_genre) == 0

    def test_add_new_book_repeat_book_not_add_book(self, collector):
        collector.add_new_book('Пикник на обочине')
        collector.add_new_book('Пикник на обочине')
        assert len(collector.books_genre) == 1

    def test_set_book_genre_add_genre(self, collector):
        collector.add_new_book('Улитка на склоне')
        collector.set_book_genre('Улитка на склоне', 'Фантастика')
        assert collector.books_genre.get('Улитка на склоне') == 'Фантастика'

    def test_get_book_genre_is_displayed_book_genre(self, collector):
        collector.add_new_book('Улитка на склоне')
        collector.set_book_genre('Улитка на склоне', 'Фантастика')
        assert collector.get_book_genre('Улитка на склоне') == 'Фантастика'

    def test_get_books_with_specific_genre_is_displayed_by_genre(self, collector):
        collector.add_new_book('Улитка на склоне')
        collector.set_book_genre('Улитка на склоне', 'Фантастика')
        collector.add_new_book('Пикник на обочине')
        collector.set_book_genre('Пикник на обочине', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Улитка на склоне', 'Пикник на обочине']

    def test_get_books_genre_is_displayed_books_genre(self, collector):
        collector.add_new_book('Улитка на склоне')
        collector.set_book_genre('Улитка на склоне', 'Фантастика')
        collector.add_new_book('Сборник анекдотов')
        collector.set_book_genre('Сборник анекдотов', 'Комедии')
        assert len(collector.get_books_genre()) == 2

    def test_get_books_for_children_not_in_children_books_list(self, collector):
        collector.add_new_book('Король Лев')
        collector.set_book_genre('Король Лев', 'Мультфильмы')
        collector.add_new_book('Пила')
        collector.set_book_genre('Пила', 'Ужасы')

        assert len(collector.get_books_for_children()) == 1

    def test_add_book_in_favorites_add_two_books_in_favorites(self, collector):
        collector.add_new_book('Пикник на обочине')
        collector.add_book_in_favorites('Пикник на обочине')
        collector.add_new_book('Библиография Шерлока Холмса')
        collector.add_book_in_favorites('Библиография Шерлока Холмса')
        assert len(collector.favorites) == 2

    def test_delete_book_from_favorites_delete_one_book(self, collector):
        collector.add_new_book('Улитка на склоне')
        collector.add_book_in_favorites('Улитка на склоне')
        collector.add_new_book('Пила')
        collector.add_book_in_favorites('Пила')
        collector.delete_book_from_favorites('Пила')
        assert len(collector.favorites) == 1

    def test_get_list_of_favorites_books_is_displayed_favorites_books(self, collector):
        collector.add_new_book('Пикник на обочине')
        collector.add_book_in_favorites('Пикник на обочине')
        collector.add_new_book('Король Лев')
        collector.add_book_in_favorites('Король Лев')
        assert len(collector.get_list_of_favorites_books()) == 2
