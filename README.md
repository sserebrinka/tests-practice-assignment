# Автоматизированное тестирование граничных значений с Google Sheets
Проект для запуска автотестов, значения для которых берутся из таблицы, а результаты записываются автоматически

## Как использовать
1. **Клонируйте репозиторий:**
```
git clone https://github.com/your-username/tests-practice-assignment.git
cd tests-practice-assignment
```
2. **Скачайте ключ доступа JSON из Google Cloud и положите в папку ```utils```:**
 - Перейдите по ссылке https://console.developers.google.com/
 - Создайте новый проект (если его ещё нет)
 - Перейдите в раздел "**APIs & Services**" -> "**Library**"
 - Найдите и включите API: **Google Sheets API** и **Google Drive API**
 - Перейдите в **"Credentials"** -> нажмите **"Create credentials"** -> **"Service account"**
 - Введите любое имя и нажмите **"Create and Continue"**
 - Роли можно пропустить -> нажимаем **"Done"**
 - Теперь у вас есть созданная сервисная учетная запись. Нажмите на нее -> вкладка **"Keys"**
  ![image](https://github.com/user-attachments/assets/f4404594-82c5-4b32-8f87-80129a65665f)
  ![image](https://github.com/user-attachments/assets/11f4b12c-70c5-4b90-9fa4-1cd0105e300d)
 - Создайте ключ. Нажмите **"Add Key"** -> **"Create new key"** -> выберите **JSON**
 - Переместите скачанный **JSON-файл** в папку ```utils```
 - Создайте Google таблицу
 - **ШАБЛОН ДЛЯ ТАБЛИЦЫ**. Вставьте шаблон в вашу созданную таблицу:
  https://docs.google.com/spreadsheets/d/1wHL78EzO61pKK0r1s-sZ56wLs0H-puVs1RyxvSOJNfA/edit?usp=sharing
 - Нажмите **"Поделиться"**
 - Скопируйте поле ```client_email``` из скачанного **JSON-файла**
 - Вставьте email клиента в окно **"Поделиться"** и выдайте ему роль **"Редактор"**  
3. **Создайте ```.env``` файл в корне проекта:***
```
CREDENTIALS_FILE = 'id_вашей_таблицы'
SPREADSHEET_ID = 'скачанный_json_файл.json'
```
ID вашей таблицы находится между ```https://docs.google.com/spreadsheets/d/``` и ```/edit?gid=0#gid=0```  
4. **Установите зависимости:**
```
pip install -r requirements.txt
```
5. **Запустите тесты:**
```
pytest -s -v
```
## Таблица заполненная вручную:
![image](https://github.com/user-attachments/assets/3779e565-0090-47e5-ae72-cdac4759eb69)
## Замечания
При запуске автотестов некоторые ячейки в таблице могут остаться незаполненными по причине того, что на странице отображается системное уведомление от сайта, которое не имеет HTML-структуры (уведомление от сайта). Такое уведомление невозмоэно обработать автоматически и получить его текст через Selenium. Возможно есть альтерантивные варианты, но я пока не реализовала.

