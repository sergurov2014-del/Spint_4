# qa_python

# В данном файле описаны тесты покрывающие функционал класса BooksCollector для финального задания спринта по Юнит тестированию

# 0)test_add_new_book_add_two_books - тест на проверку добавления двух книг данный авторами курса для примера

# 1) test_add_new_book_already_in_collection_negative - негативный тест на проверку метода add_new_book, с экземпляром который уже есть в колекции

# 2) test_add_new_book_values_in_and_out_of_range - тест с параметризацией (book_input, expected_count), проверяется добавление книги с длинной названия внутри, вне и на границе разрешённого диапазона

# 3)test_set_book_genre_validation_correct_and_incorrect_genre - тест с параметризацией (genre_input, should_change). Проверка работы метода set_book_genre - жанр книги заменяется, если на замену подаётся валидный жанр

# 4)test_get_book_genre_from_books_genre_collection_posite - тест на проверку работы метода возвращаюшего жанр книги по ей имени

# 5)test_get_books_with_specific_genre_returns_correct_list - тест с позитивной проверкой получения списка из 2-х добавленных детективов


# 6)test_get_books_genre_for_one_book - тест на получение словаря books_genre с одной книгой

# 7)test_get_books_for_children_one_comedy_returns - тест на возвращение одной книги подходящей детям

# 8)test_add_book_in_favorites_ensures_uniqueness - тест на единичное добавление книги в избранное, при попытке добавить её дважды

# 9)test_delete_book_from_favorites -тест на проверку удаления книг из избранного

# 10)test_get_list_of_favorites_books_add_then_get_two_books_from_favorite - тест на проверку получения 2 книг из списка избранных