>>>Документ отражает условные этапы разработки
1.  На первом этапе сделал
    > Добавил файл data.excl и excode.py 
    > Прочитал исходный файл при помощи функции reader, создал и вернул из функции словарь с координатам corr.
2.  На втором этапе сделал
    >  Создал функцию list2geojson. Она позволяет перейти от списка координат к готовый geojson b json
    >  Выборка и заполение свойств geojson - автоматическая
    >  Создал функцию loadtoMongo. Она записывает в в базу данных MongoDB готовый json. Вызывается единажды
3.  На третьем этапе сделал
    > Создал функцию Sample. Она отвечает за выборку случайных данных
    > Протестировал функцию на одной из выборок
    > Создал множество выборок (не менее 10)
    > Сохранил выборки в geojson
