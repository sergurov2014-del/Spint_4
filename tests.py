import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.books_genre) == 2

    def test_add_new_book_already_in_collection_negative(self): #1)негативный тест на проверку метода add_new_book, с экземпляром который уже есть в колекции
        collector = BooksCollector()
        collector.add_new_book('Война и пир')
        collector.add_new_book('Война и пир')
        assert len(collector.books_genre)==1

    @pytest.mark.parametrize('book_input, expected_count', 
                            [
                                  ("1",1),
                                  ("A"*40, 1),
                                  ("b"*41,0),
                                  ("c"*100,0),
                                  ('', 0)
                            ]
                             )  
    def test_add_new_book_values_in_and_out_of_range(self, book_input, expected_count): #2)тест с параметризацией, проверяются добавление книги с длинной внутри, вне и на границе разрешённого диапазона 
        collector = BooksCollector()
        collector.add_new_book(book_input)
        assert len(collector.books_genre)==expected_count

    @pytest.mark.parametrize('genre_input, should_change', 
                            [
                                ('Детективы',True),
                                ('Фантастика', True),
                                ("", False),
                                ("Веб-новелла", False),
                                ("Детектив", False),
                                ("Комедии",False) 
                            ]
                            )
    def test_set_book_genre_validation_correct_and_incorrect_genre(self, genre_input, should_change): #3) проверка работы метода set_book_genre - жанр книги заменяется, если на замену подаётся валидный жанр
        collector = BooksCollector()
        collector.add_new_book("За кого же Пупа получил зарплату?")
        collector.set_book_genre("За кого же Пупа получил зарплату?","Комедии")
        initial_genre=collector.books_genre["За кого же Пупа получил зарплату?"]
        collector.set_book_genre("За кого же Пупа получил зарплату?", genre_input)
        final_genre=collector.books_genre["За кого же Пупа получил зарплату?"]
        if should_change:
        # Если жанр валидный, он должен измениться на тот, который мы передали
            assert final_genre == genre_input
        else:
        # Если жанр невалидный, он должен остаться таким, каким был до попытки изменения
            assert final_genre == initial_genre 
    
    def test_get_book_genre_from_books_genre_collection_positive(self): #4) проверка работы метода возвращаюшего жанр книги по ей имени
        collector = BooksCollector()
        collector.add_new_book("Приключения Шерлока Холмса")
        collector.set_book_genre("Приключения Шерлока Холмса", "Детективы")
        assert collector.get_book_genre("Приключения Шерлока Холмса")=="Детективы"


    def test_get_books_with_specific_genre_returns_correct_list (self):#5)позитивная проверка на получения списка из 2-х добавленных детективов
        collector = BooksCollector()
        collector.add_new_book("Приключения Шерлока Холмса")
        collector.set_book_genre("Приключения Шерлока Холмса", "Детективы")
        collector.add_new_book("12 Стульев")
        collector.set_book_genre("12 Стульев", "Комедия")
        collector.add_new_book("Десять негритят")
        collector.set_book_genre("Десять негритят", "Детективы")
        assert set(collector.get_books_with_specific_genre("Детективы")) == {'Приключения Шерлока Холмса', 'Десять негритят'}            


    def test_get_books_genre_for_one_book (self):#6)тест на получение словаря books_genre
        collector = BooksCollector()
        collector.add_new_book("Приключения Шерлока Холмса")
        collector.set_book_genre("Приключения Шерлока Холмса", "Детективы")
        assert collector.get_books_genre()=={"Приключения Шерлока Холмса": "Детективы"}         

    def test_get_books_for_children_one_comedy_returns(self):#7)тест на возвращение книги подходящей детям
        collector = BooksCollector()
        collector.add_new_book("ОНО")
        collector.set_book_genre("ОНО", "Ужасы")
        collector.add_new_book("Уголовный кодекс РФ")
        collector.set_book_genre("Уголовный кодекс РФ", "Комедии")
        assert collector.get_books_for_children()==["Уголовный кодекс РФ"]

    def test_add_book_in_favorites_ensures_uniqueness(self):#8)тест на добавление 1 книги в избранное
        collector = BooksCollector()
        collector.add_new_book("ОНО")
        collector.add_book_in_favorites("ОНО")
        collector.add_book_in_favorites("ОНО")
        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites(self):#9)тест на проверку удаления книг из избранного
        collector = BooksCollector()
        collector.add_new_book("ОНО")
        collector.add_book_in_favorites("ОНО")
        collector.delete_book_from_favorites("ОНО")
        assert len(collector.favorites) == 0

    def test_get_list_of_favorites_books_add_then_get_two_books_from_favorite(self):#10) проверка получения 2 книг из списка избранных
        collector = BooksCollector()
        collector.add_new_book("Моя Борьба с Курсом по автоматизации")
        collector.add_new_book("Приключения Чебы и Гены в Лас-Вегасе")
        collector.add_book_in_favorites("Моя Борьба с Курсом по автоматизации")
        collector.add_book_in_favorites("Приключения Чебы и Гены в Лас-Вегасе")
        assert collector.get_list_of_favorites_books()==["Моя Борьба с Курсом по автоматизации", "Приключения Чебы и Гены в Лас-Вегасе"] 