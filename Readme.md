<h1>Парсер данных через селениум на сайте: https://www.nseindia.com/</h1>

<h2>Использование:</h2>
- <code>pip install -r requirements.txt</code> 
- <code>python nseindia.py</code> 

<h2>Настройки:</h2>
- options.headless = <code>True</code> - безоконный режим

<p>P.s По умолчанию стоит <code>False</code> т.к в безоконном режиме не грузит страницу. Используются рандомные юзер-агенты</p>



<h1>Парсинг последних твитов Elon Musk</h1>

<h2>Использование:</h2>
- <code>pip install -r requirements.txt</code> 
- <code>python elonmusk.py</code> 

<h2>Настройки:</h2>
- run = ScraperElon(10) <code>10</code> - сколько постов нужно получить

Теперь получаем токен, на случай, если парсер не работает:<br>
<code>F12 >> сеть' >> Fetch/XHR >> UserTweeets >> Файлы cookie >> gt</code>
- <code>config_twitter/cfg.yaml >> 'x-guest-token': 'Сюда вставляем значение gt'</code>

![Screen](https://github.com/makwerik/Webrevers/blob/master/img/screen.PNG)
