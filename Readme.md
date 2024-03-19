
<h1>Предисловие:</h1>

<h3>Реализовал получение токенов "guest_id", "Bearer", без селениума, так же изменился способ получения из json информацию о твитах,
поэтому <code>elonmusk.py</code> - НЕ РАБОТАЕТ, используем <code>twitter.py</code>, создал отельный cfg.json, куда токены каждый раз перезаписываются,изначально в cfg нет этих токенов, они парсятся непосредственно в коде и уже потом записываются в файл
если что могу на раз-два вернуть конфиг назад в код, просто решил разгрузить его таким образом. Старался соблюдать принцип DRY,но из-за спешки и неудобства плохо получилось)) И в целом я считаю, что можно сделать лучше, если есть время </h3>

<h1>Парсер данных через селениум на сайте: https://www.nseindia.com/</h1>

<h2>Использование:</h2>
- <code>pip install -r requirements.txt</code> 
- <code>python nseindia.py</code> 

<h2>Настройки:</h2>
- options.headless = <code>True</code> - безоконный режим

<p>P.s По умолчанию стоит <code>False</code> т.к в безоконном режиме не грузит страницу. Используются рандомные юзер-агенты</p>

<h1>Парсинг последних N твитов без использования selenium</h1>

<h2>Использование:</h2>
- <code>pip install -r requirements.txt</code> 
- <code>python twitter.py</code> 

<h2>Настройки:</h2>
- t = ScrapperTwitter(username='', quantity=10, proxy=None) <code>username</code> - чьи посты нужно получить | <code>quantity</code> - сколько постов нужно получить |  <code>proxy</code> - прокси

Используются так же рандомные юзер-агенты, токены теперь получаем через requests


<h1>Парсинг последних N твитов с использованием selenium</h1>

<h2>Использование:</h2>
- <code>pip install -r requirements.txt</code> 
- <code>python elonmusk.py</code> 

<h2>Настройки:</h2>
- run = ScraperElon(username='', quantity=10, proxy=None) <code>username</code> - чьи посты нужно получить | <code>quantity</code> - сколько постов нужно получить |  <code>proxy</code> - прокси

Используются так же рандомные юзер-агенты, токен теперь получаем через selenium. Так же в selenium нужно добавить прокси

