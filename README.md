<h1>Задание Тензор</h1>
<br>
<img src = "https://mrselenium.com/wp-content/uploads/2020/02/seleniumlogo.png" height = "100">
<img src = "https://unipython.com/wp-content/uploads/2020/04/pytest-framework-min.png" height = "100">
<br>
<br>
<h2>Содержание</h2>
<ul>
 <li><a href="#description">Описание</a>
 <li><a href="#structure">Структура проекта</a>
 <li><a href="#library">Сторонние библиотеки и версия chromedriver</a>
</ul>
<h2 id = description>Описание проекта</h2>

Автотест состоит из двух частей.<br>
1. Проверка работы поисковой строки по ключевому слову "Тензор" и выполнение
поискового запроса.<br>
2. Проверка работы и навигации в коллекции изображений.<br>
В качестве поисковой системы выбран Yandex, коллекции изображений Yandex Картинки.<br>
Задание выполнено с применением <code>pytest</code> и <code>selenium</code>.

<h2 id = structure>Структура проекта</h2>
Проект состоит из 2-х автотестов - проверки поисковой системы (test_sample.py)
и коллекции изображений (test_ya_pictures.py).

<h2 id = library>Сторонние библиотеки и версия chromedriver</h2>
В качестве сторонних библиотек применен <code>requests</code>, и фреймворки <code>pytest-dependency</code>, <code>pytest-depence</code>. Автотест написан
с использованием selenium 4.3.0 и chromedriver версии 107.0.5304.62. В качестве браузера выбран Chrome.
