**Задание**

Реализовать консольное приложение заметки, с сохранением, чтением,
добавлением, редактированием и удалением заметок. Заметка должна
содержать идентификатор, заголовок, тело заметки и дату/время создания
или последнего изменения заметки. Сохранение заметок необходимо сделать
в формате json или csv формат (разделение полей рекомендуется делать через
точку с запятой). Реализацию пользовательского интерфейса студент может
делать как ему удобнее, можно делать как параметры запуска программы
(команда, данные), можно делать как запрос команды с консоли и
последующим вводом данных, как-то ещё, на усмотрение студента.

**Инструкции по установке**

Перед использованием приложения установить библиотеку natsort (pip install natsort)\
Запуск приложения из файла **main.py**


**Информация о приложении**

Приложение состоит из 5 пунктов:
1. Создать заметку - создает заметку с последовательным вводом заголовка
и текста. При вводе 0 можно выйти в главное меню.
2. Поиск по заметкам - по умолчанию выполняет поиск по всем элементам заметки без исключения, выводится список всех заметок,
удовлетворяющих критериям поиска. Можно искать по дате в указанном формате, также можно искать заметки по id.
Можно вывести список всех заметок или вернуться в главное меню, если ввести 0.
3. Редактировать заметку - редактирует заметку. Сначала нужно ввести id заметки,
если заметка с введенным id есть, программа предложит изменить название и текст заметки.
Если название или текст редактировать не нужно, можно нажать Enter, не вводя ничего, 
в этом случае сохранится текущий текст или название.
Измененная заметка сохраняется под исходным id.
4. Удалить заметку - удаляет заметку по введенному id.
5. Выход - выход из программы

**Структура заметки**\
id |  название  |   текст  | дата создания/редактирования\
10 | приготовить |  еду  |     14-02-2023 17:35:46

**Структура в файле CSV**\
id ; название  ;   текст ;   дата создания/редактирования\
11;позвонить;+79118883746;14-02-2023 17:35:46

Заметки сохраняются в файле notes.csv, разделитель - ";"


**Не изменять вручную файл notes.csv!**