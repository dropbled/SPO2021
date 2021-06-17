# ***Drawing robot (plotter)***

### Цель проекта
Разработать работающую модель робота-плоттера для преобразования печатаемого текста в рукописный шрифт на лист А4

### Значимость проекта
В современном мире человек всё меньше пишет текст от руки, ведь набор его на компьютере выглядит проще, хотя и в напечатанном виде он выглядит несколько однообразно. В связи с этим может возникнуть необходимость "ручного" написания, однако в таком случае невозможно что-либо исправить аккуратно. И в таком случае подобный проект - лучшее решение, позволяющее создать идеальный текст в электронном виде и затем перевести его в красивый рукописный, не затрачивая при этом собственных сил, так как для этого нужно всего лишь загрузить данные на робота.  

### Задачи
1. Придумать и собрать корпус и движущуюся часть робота на трёх осях
2. Создать программу для перевода печатаемого текста в рукописный

### Описание работы
Наш робот должен принимать с компьютера входной параметр - текст - в виде набора параметро передвижения по двум горизонтальным осям *(X и Y)* и на их основе производить движение.

### Этапы работы
1. Начальный этап - создание внешнего вида робота и проверка его работоспособности
2. Подключение ROS

### Структура робота
Весь проект выполнен с использованием комплектующих *Lego*

1. Корпус
* рама для крепления на ней движимой части
2. Ось X
* два мотора
* две рейки для крепления моторов оси Y
3. Ось Y
* два мотора
* рейки для крепления оси Z
4. Ось Z
* мотор
* крепление для опускания/подъёма карандаша
5. Блок *Lego EV3*

### Что было сделано и чего удалось достичь на начальном этапе
В результате работы удалось сделать робота с наиболее плавным и устойчивым движением двигателей по осям. Для более качественной работы блока EV3 образ системы был установлен с [сайта ev3dev](https://www.ev3dev.org/docs/getting-started/) на полностью "чистую" SD-карту. По итогам нескольких тестов удалось найти максимально правильные необходимые напряжения для подачи на двигатели.

[Пример работы робота](https://drive.google.com/file/d/1FAD7zE_WIPlvrzDgCZBnQWeJByxbpj38/view?usp=sharing)
