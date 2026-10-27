# Домашнее задание: Мини-проект «Список любимых фильмов»

## 0) Подготовка
```bash
mkdir my-favorite-movies && cd my-favorite-movies
git init
```

---

## 1) Структура проекта

**Создайте папки и файлы:**
```bash
mkdir src docs data
touch README.md src/app.txt data/movies.txt
```

**Заполните содержимым:**
- **README.md** — заголовок `# My Favorite Movies` и краткое описание проекта.
- **data/movies.txt** — список 5–7 любимых фильмов, по одному в строку.
- **src/app.txt** — псевдокод, как выводить список фильмов.

Пример `data/movies.txt`:
```
Inception
The Matrix
Interstellar
The Godfather
Pulp Fiction
```

Пример `src/app.txt`:
```
1. Открыть файл data/movies.txt
2. Прочитать каждую строку как название фильма
3. Вывести названия на экран по одному в строке
```

---

## 2) Навигация и просмотр

```bash
ls
ls -a
pwd
cat src/app.txt
less data/movies.txt   # q для выхода
clear
cd data
cd ..
```

---

## 3) Копирование и удаление

```bash
cp data/movies.txt data/movies_backup.txt
mkdir data/archive
cp data/movies.txt data/archive/
rm data/movies_backup.txt
mkdir tmp
touch tmp/test.txt
rm -r tmp
```

---

## 4) Первый коммит и пуш

```bash
git add .
git commit -m "Init project: movie list"
git branch -M main
git remote add origin <URL_вашего_репозитория>
git push -u origin main
```

---

## Что сдать
1. Ссылку на репозиторий GitHub.  
2. Историю команд:
```bash
history > commands.txt
git add commands.txt
git commit -m "Add terminal history"
git push
```

---

## Идеи для плюсика (по желанию)
- Добавьте файл `docs/<название-фильма>.md` с описанием и интересными фактами.
- В `src/app.txt` пропишите «меню» — какой фильм показать первым.
- В `README.md` добавьте раздел «Примеры фильмов».
