# Домашнее задание: Мини-проект «Мои любимые рецепты»

## 0) Подготовка
```bash
mkdir my-favorite-recipes && cd my-favorite-recipes
git init
```

---

## 1) Структура проекта

**Создайте папки и файлы:**
```bash
mkdir src docs data
touch README.md src/app.txt data/recipes.txt
```

**Заполните содержимым:**
- **README.md** — заголовок и краткое описание проекта.
- **data/recipes.txt** — список 5–7 рецептов, по одному в строку.
- **src/app.txt** — псевдокод, как выводить список рецептов.

Пример `data/recipes.txt`:
```
Борщ
Паста карбонара
Шакшука
Блины
Окрошка
```

Пример `src/app.txt`:
```
1. Открыть файл data/recipes.txt
2. Прочитать каждую строку как название рецепта
3. Вывести названия на экран по одному в строке
```

---

## 2) Навигация и просмотр

```bash
ls
ls -a
pwd
cat src/app.txt
less data/recipes.txt   # q для выхода
clear
cd data
cd ..
```

---

## 3) Копирование и удаление

```bash
cp data/recipes.txt data/recipes_backup.txt
mkdir data/archive
cp data/recipes.txt data/archive/
rm data/recipes_backup.txt
mkdir tmp
touch tmp/test.txt
rm -r tmp
```

---

## 4) Первый коммит и пуш

```bash
git add .
git commit -m "Init project: recipe list"
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
- Добавьте файл `docs/<название-рецепта>.md` с ингредиентами и шагами.
- В `src/app.txt` пропишите «меню» — какой рецепт показать первым.
- В `README.md` добавьте раздел «Примеры рецептов».
