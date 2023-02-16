# Подсчет живых клеток
Цель проекта: <br>
<br>
Один из этапов подразумевает дифференцировку стволовых клеток, а также оптимизацию методик их выращивания (изменения состава среды, реагентов, концентраций и т.д.). Для анализа роста клеток и их количества необходимо считать их вручную или с помощью дорогостоящих приборов.<br>
<br>
Чтобы упростить и автоматизировать данный процесс, мы написали скрипт для подсчета процентного соотношения площади живых клеток на основе изображений окрашенных клеток в двух цветовых каналах: синем со всеми клетками и красном с мертвыми клетками.<br>
Также мы собрали датасет из 342 изображений для обучения нейросети, если в дальнейшем нам понадобится более высокая точность подсчета.<br>
Пример изображений:<br>
![Image](/images/8_2_all.png)
![Image](/images/8_2_dead.png)
<br>
Какие источники данных?<br>
В качестве источников данных выступает наша лаборатория, а также статьи.<br>
<br>
Какое качество и полнота данных?<br>
Фотографии разделены по цветовым каналам: синим — все клетки, красным — мертвые клетки.<br>
<br>
Как увеличить объем и качество ваших данных?<br>
Объем данных напрямую зависит от работы нашей лаборатории, поэтому их количество увеличится, когда мы начнем активно работать с этими клетками.<br>
<br>
Как данные влияют на результат вашего проекта?<br>
<br>
<br>
Какие бенчмарки по работе с данными определяете?<br>
<br>
<br>
Какие инструменты для хранения, очистки, разметки, версионирования данных применяете сейчас и планируете применить в будущем?<br>
<br>
<br>
Как обеспечите воспроизводимость экспериментов?<br>
<br>
<br>
