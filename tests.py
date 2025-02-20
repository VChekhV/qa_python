import pytest
from main import BooksCollector

class TestBooksCollector:

    @pytest.fixture
    def collector_with_books(self):
        collector = BooksCollector()
        # Добавляем книги в коллекцию
        collector.books_genre = {
            'Аватар': 'Фантастика',
            'Остров проклятых': 'Детективы',
            'Шрек': 'Мультфильмы',
            'Клаустрофобы': 'Ужасы',
            'Штрафной бросок': 'Детективы',
            'Алхимик': 'Фантастика',
            'Ну, погоди!': 'Комедии'
        }
        return collector

    @pytest.mark.parametrize("book_names", [('Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить')])
    def test_add_new_book_add_two_books(self, book_names):
        collector = BooksCollector()
        collector.add_new_book(book_names[0])
        collector.add_new_book(book_names[1])
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize("book_name, genre", [
        ('Аватар', 'Фантастика'),
        ('Остров проклятых', 'Детективы'),
        ('Шрек', 'Мультфильмы'),
        ('Клаустрофобы', 'Ужасы'),
        ('Ну, погоди!', 'Комедии'),
        ('Алхимик', 'Фантастика')
    ])
    def test_set_book_genre_correctly(self, collector_with_books, book_name, genre): #проверяем установку жанра книге
        collector_with_books.set_book_genre(book_name, genre)
        # Проверяем, что жанр книги правильно установлен
        assert collector_with_books.books_genre[book_name] == genre

    @pytest.mark.parametrize("book_name, invalid_genre", [
        ('Аватар', 'Боевик'),
        ('Остров проклятых', 'Драма'),
        ('Шрек', 'Триллер'),
        ('Клаустрофобы', 'Роман'),
        ('Ну, погоди!', 'Мюзикл'),
        ('Алхимик', 'История')
    ])
    def test_set_book_genre_invalid_genre(self, collector_with_books, book_name, invalid_genre): #проверяем, что несуществующий жанр не устанавливается
        # Пытаемся установить несуществующий жанр
        original_genre = collector_with_books.books_genre[book_name]
        collector_with_books.set_book_genre(book_name, invalid_genre)
        # Проверяем, что жанр книги не изменился
        assert collector_with_books.books_genre[book_name] == original_genre

    @pytest.mark.parametrize("book_name, expected_genre", [
        ('Аватар', 'Фантастика'),
        ('Остров проклятых', 'Детективы'),
        ('Шрек', 'Мультфильмы'),
        ('Клаустрофобы', 'Ужасы'),
        ('Штрафной бросок', 'Детективы'),
        ('Алхимик', 'Фантастика'),
        ('Ну, погоди!', 'Комедии')
    ])
    def test_get_book_genre_existing_book_with_genre(self, collector_with_books, book_name, expected_genre):
        # Проверяем, что для книги с установленным жанром возвращается правильный жанр
        result = collector_with_books.get_book_genre(book_name)
        assert result == expected_genre

    @pytest.mark.parametrize("book_name", [
        'Гордость и предубеждение и зомби',
        '1984',
        'Война и мир',
        'Скотный двор',
        'Убить пересмешника'
    ])
    def test_get_book_genre_existing_book_without_genre(self, collector_with_books, book_name):
        # Проверяем, что для книги без установленного жанра возвращается None
        expected_genre = None
        result = collector_with_books.get_book_genre(book_name)
        assert result == expected_genre

    @pytest.mark.parametrize("book_name", [
        'Игры разума',
        'Гарри Поттер и философский камень',
        'Властелин колец',
        'Пиковая дама',
        'Зеленая миля'
    ])
    def test_get_book_genre_non_existing_book(self, collector_with_books, book_name):
        # Проверяем, что для несуществующей книги возвращается None
        expected_genre = None
        result = collector_with_books.get_book_genre(book_name)
        assert result == expected_genre

    @pytest.mark.parametrize("genre, expected_books", [
        ('Детективы', ['Остров проклятых', 'Штрафной бросок']),
        ('Фантастика', ['Аватар', 'Алхимик']),
        ('Мультфильмы', ['Шрек']),
        ('Ужасы', ['Клаустрофобы']),
        ('Комедии', ['Ну, погоди!'])
    ])
    def test_get_books_with_specific_genre_existing_genre(self, collector_with_books, genre, expected_books):
        # Проверяет, что для жанра, книги которого присутствуют в коллекции, возвращается правильный список книг
        result = collector_with_books.get_books_with_specific_genre(genre)
        assert result == expected_books

    @pytest.mark.parametrize("genre, expected_books", [
        ('Романтика', []),  # Жанр с отсутствием книг
        ('История', [])  # Несуществующий жанр
    ])
    def test_get_books_with_specific_genre_no_books_for_genre(self, collector_with_books, genre, expected_books):
        # Проверяет, что для жанра, книги которого отсутствуют, возвращается пустой список.
        result = collector_with_books.get_books_with_specific_genre(genre)
        assert result == expected_books

    @pytest.mark.parametrize("genre, expected_books", [
        ('Романтика', []),  # Жанр с отсутствием книг
        ('История', [])  # Несуществующий жанр
    ])
    def test_get_books_with_specific_genre_non_existing_genre(self, collector_with_books, genre, expected_books):
        # Проверяет, что для несуществующего в genre жанра, возвращается пустой список.
        result = collector_with_books.get_books_with_specific_genre(genre)
        assert result == expected_books

    @pytest.mark.parametrize("expected_books_genre", [
        {
            'Аватар': 'Фантастика',
            'Остров проклятых': 'Детективы',
            'Шрек': 'Мультфильмы',
            'Клаустрофобы': 'Ужасы',
            'Штрафной бросок': 'Детективы',
            'Алхимик': 'Фантастика',
            'Ну, погоди!': 'Комедии'
        }
    ])
    def test_get_books_genre_return_books_genre(self, collector_with_books, expected_books_genre):
        # Проверяет, что метод get_books_genre возвращает точный словарь books_genre, который ожидается.
        result = collector_with_books.get_books_genre()
        assert result == expected_books_genre

    @pytest.mark.parametrize("expected_books_for_children", [
        (['Аватар', 'Шрек', 'Алхимик', 'Ну, погоди!'])
    ])
    def test_get_books_for_children_two_books(self, collector_with_books, expected_books_for_children):
        # Ожидаем, что только книги без ограничений по возрасту будут в списке
        result = collector_with_books.get_books_for_children()
        assert result == expected_books_for_children

    @pytest.mark.parametrize("book_to_add", [
        # Разные книги для добавления в избранное
        'Аватар',
        'Остров проклятых',
        'Шрек',
        'Клаустрофобы'
    ])
    def test_add_book_in_favorites_book_to_add(self, collector_with_books, book_to_add):
        # Добавляем книгу в избранное
        collector_with_books.add_book_in_favorites(book_to_add)
        # Проверяем, что книга добавилась в список избранных
        assert book_to_add in collector_with_books.favorites

    @pytest.mark.parametrize("book_to_add", [
        # Разные книги для добавления в избранное
        'Аватар',
        'Остров проклятых',
        'Шрек',
        'Клаустрофобы'
    ])
    def test_add_book_in_favorites_book_twice_to_add(self, collector_with_books, book_to_add):
        # Пробуем добавить книгу дважды
        collector_with_books.add_book_in_favorites(book_to_add)
        collector_with_books.add_book_in_favorites(book_to_add)
        # Убедимся, что в избранных нет дублирующих записей
        assert collector_with_books.favorites.count(book_to_add) == 1

    @pytest.mark.parametrize("book_to_modify", [
        # Разные книги для добавления и удаления из избранного
        'Аватар',
        'Остров проклятых',
        'Шрек',
        'Клаустрофобы'
    ])
    def test_delete_book_from_favorites(self, collector_with_books, book_to_modify):
        # Добавляем книгу в избранное
        collector_with_books.add_book_in_favorites(book_to_modify)
        # Удаляем книгу из избранного
        collector_with_books.delete_book_from_favorites(book_to_modify)
        # Проверяем, что книга удалена из списка избранных
        assert book_to_modify not in collector_with_books.favorites

    @pytest.mark.parametrize("book_to_remove", [
        # Книги, которых нет в избранном
        'Остров проклятых',
        'Шрек',
        'Клаустрофобы',
        'Несуществующая книга'
    ])
    def test_delete_book_from_favorites_no_book(self, collector_with_books, book_to_remove):
        # Добавляем книгу в избранное
        book_to_add = 'Аватар'
        collector_with_books.add_book_in_favorites(book_to_add)
        # Пытаемся удалить книгу, которой нет в избранном
        collector_with_books.delete_book_from_favorites(book_to_remove)
        # Убеждаемся, что список избранных остался без изменений
        assert collector_with_books.favorites == ['Аватар']

    @pytest.mark.parametrize("favorites_list", [
        ['Аватар', 'Остров проклятых'],
        ['Шрек'],
        ['Клаустрофобы', 'Аватар'],
        [],
    ])
    def test_get_list_of_favorites_books(self, collector_with_books, favorites_list):
        # Устанавливаем список избранных книг
        collector_with_books.favorites = favorites_list
        # Получаем список избранных книг
        favorites = collector_with_books.get_list_of_favorites_books()
        # Проверяем, что список избранных соответствует ожиданиям
        assert favorites == favorites_list