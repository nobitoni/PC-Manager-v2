# PC Manager (telebot)


PC Manager - удобная программа для удаленного управления компьютером (только для windows 10 / 11)


## Установка

### .exe файл
[СКАЧАТЬ](https://github.com/nobitoni/PC-Manager-v2/releases/download/untagged-7918e16fa1970536f135/pcm-v2.rar)

### .py файл (Для windows)
```bash
git clone https://github.com/nobitoni/PC-Manager-v2.git
cd "PC-Manager-v2"
pip install -r requirements.txt
```
Чтобы запустить бота, выполните настройку, далее ботом можно пользоваться введя следующее в консоль:
```bash
pythonw bot.py
```
Отключение будет автоматическое, после выключения система, либо вручную через диспетчер задач

## Настрокйка

1. Откройте мессенджер Telegram и войдите в свой аккаунт или создайте новый, если вы еще этого не сделали.
2. Введите @BotFather во вкладке поиска и выберите соответствующего бота.
Примечание: У официальных ботов Telegram рядом с именем стоит галочка.
3. Нажмите кнопку Start, чтобы активировать бота BotFather. Вы получите список команд для управления ботами.
4. Выберите или введите команду /newbot и нажмите Отправить.
5. Выберите имя для своего бота. Ваши подписчики будут видеть его в своих беседах.
6. После того как вы выберете подходящее имя для бота, он будет создан. Вы получите сообщение со ссылкой на вашего бота t.me/<имя_бота>. Скопируйте значение токена и вставьте его в json-файл в поле token (вместо слова TOKEN), обязательно используя двойные кавычки.
7. В поле users вместо значения "id" вставьте свой id (чтобы узнать его, воспользуйтесь [@userinfobot](https://t.me/userinfobot)). Это мера безопасности, чтобы ваш компьютер мог управляться вами с одной или нескольких учетных записей. Вы можете указать более одного id.
Пример:
```json
"users": [123, 234, 456]
```
8. Если вы используете ноутбук, вы можете распознать его заряд, для этого в поле "is_laptop" поставьте значение True.

## Связь с разработчиком через соц.сети -> [@Артем](https://bit.ly/3wAJaPa)
