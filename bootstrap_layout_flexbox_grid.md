# Bootstrap 5: Layout, Flexbox и Grid

> **Учебный конспект по Bootstrap 5.3**  
> В этом материале рассматриваются построение адаптивных страниц, стандартная 12-колоночная сетка Bootstrap, Flexbox utilities и возможности CSS Grid. Все основные примеры работают с Bootstrap 5.3.5 через CDN; исключение — примеры с экспериментальными классами `.grid` / `.g-col-*`, для которых требуется специальная сборка Bootstrap.

## Содержание

1. [Что такое Layout, Flexbox и Grid](#1-что-такое-layout-flexbox-и-grid)
2. [Подключение Bootstrap](#2-подключение-bootstrap)
3. [Контейнеры](#3-контейнеры)
4. [Стандартная сетка: row и col](#4-стандартная-сетка-row-и-col)
5. [Адаптивность и breakpoints](#5-адаптивность-и-breakpoints)
6. [Гибкие и автоматические колонки](#6-гибкие-и-автоматические-колонки)
7. [Row-cols и вложенные сетки](#7-row-cols-и-вложенные-сетки)
8. [Gutters: g, gx, gy и отличие от gap](#8-gutters-g-gx-gy-и-отличие-от-gap)
9. [Flexbox: d-flex и направление](#9-flexbox-d-flex-и-направление)
10. [Выравнивание по осям](#10-выравнивание-по-осям)
11. [Перенос, растяжение и порядок](#11-перенос-растяжение-и-порядок)
12. [hstack, vstack и автоматические отступы](#12-hstack-vstack-и-автоматические-отступы)
13. [Grid: что поддерживает Bootstrap](#13-grid-что-поддерживает-bootstrap)
14. [Размеры, отступы и отображение](#14-размеры-отступы-и-отображение)
15. [Полноценная страница интернет-магазина](#15-полноценная-страница-интернет-магазина)
16. [Типичные ошибки](#16-типичные-ошибки)
17. [Практические задания](#17-практические-задания)
18. [Контрольный тест](#18-контрольный-тест)
19. [Шпаргалка и ссылки](#19-шпаргалка-и-ссылки)

---

## 1. Что такое Layout, Flexbox и Grid

**Layout** — способ организации содержимого веб-страницы: шапки, бокового меню, основных блоков, карточек и подвала.

В Bootstrap полезно различать три уровня:

| Механизм | Для чего нужен | Типичные классы |
|---|---|---|
| **Bootstrap Layout / Grid System** | Структура страницы, колонки, адаптивные карточки | `container`, `row`, `col`, `col-md-6`, `row-cols-lg-3` |
| **Flexbox utilities** | Направление, выравнивание и распределение элементов | `d-flex`, `justify-content-between`, `align-items-center` |
| **CSS Grid utilities** | Использование `display: grid`; для сложной CSS-сетки нужны дополнительные правила | `d-grid`, `gap-3` |

> **Важно:** стандартная *12-колоночная сетка Bootstrap* (`row`, `col`) построена на **Flexbox**, а не на нативном CSS Grid. Это два разных понятия, хотя в обоих встречается слово *grid*.

### Структура страницы

```text
.container
├── header
├── .row
│   ├── .col-lg-3   → боковая панель
│   └── .col-lg-9   → основной контент
│       └── .row   → вложенная сетка карточек
│           ├── .col
│           ├── .col
│           └── .col
└── footer
```

---

## 2. Подключение Bootstrap

Создадим HTML-файл:

```html
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bootstrap Layout</title>

    <link
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/css/bootstrap.min.css"
        rel="stylesheet"
    >
</head>
<body>

    <div class="container py-4">
        <h1>Моя первая страница</h1>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

Атрибут `viewport` нужен для правильного поведения адаптивной страницы на мобильных устройствах. Для Layout и Flexbox достаточно CSS Bootstrap; JavaScript требуется только некоторым интерактивным компонентам (например, выпадающим меню и модальным окнам).

---

## 3. Контейнеры

Контейнер задаёт горизонтальную область размещения контента.

### `.container`

```html
<div class="container">
    <h1>Ограниченная ширина</h1>
</div>
```

У `.container` максимальная ширина изменяется в зависимости от ширины экрана:

| Экран | Максимальная ширина `.container` |
|---|---:|
| Менее 576 px | 100% доступной ширины |
| От 576 px | 540 px |
| От 768 px | 720 px |
| От 992 px | 960 px |
| От 1200 px | 1140 px |
| От 1400 px | 1320 px |

Контейнер также имеет горизонтальные внутренние отступы.

### `.container-fluid`

```html
<div class="container-fluid">
    <h1>Контент во всю ширину</h1>
</div>
```

Занимает **100% ширины родительского элемента** при любой ширине экрана.

### Адаптивные контейнеры

```html
<div class="container-md">...</div>
<div class="container-lg">...</div>
<div class="container-xl">...</div>
```

Например, `container-lg` остаётся широким на маленьких экранах, а начиная с breakpoint `lg` получает ограниченную максимальную ширину.

**Когда выбирать:**

- `container` — обычный сайт, статья, каталог, форма.
- `container-fluid` — широкая панель управления или секция на всю ширину.
- `container-lg` — если до большого экрана блок должен занимать всю доступную ширину.

---

## 4. Стандартная сетка: `row` и `col`

Главная схема:

```html
<div class="container">
    <div class="row">
        <div class="col">A</div>
        <div class="col">B</div>
        <div class="col">C</div>
    </div>
</div>
```

- `container` ограничивает ширину.
- `row` создаёт строку с Flexbox и позволяет колонкам переноситься.
- `col` создаёт гибкую колонку.

Три одинаковых `col` распределят доступную ширину поровну: примерно по **33,33%**.

### Почему сетка состоит из 12 частей?

Число 12 удобно делится на 2, 3, 4 и 6. Например:

| Разметка | Доли | Результат |
|---|---|---|
| `col-6` + `col-6` | 6 + 6 | Две половины |
| `col-4` + `col-4` + `col-4` | 4 + 4 + 4 | Три трети |
| `col-3` × 4 | 3 + 3 + 3 + 3 | Четыре четверти |
| `col-8` + `col-4` | 8 + 4 | 2/3 и 1/3 |

Пример:

```html
<div class="row">
    <div class="col-3 bg-info">A — 25%</div>
    <div class="col-6 bg-warning">B — 50%</div>
    <div class="col-3 bg-success">C — 25%</div>
</div>
```

**Если сумма фиксированных ширин больше 12**, колонки переносятся на следующую Flexbox-строку:

```html
<div class="row">
    <div class="col-8">Первый блок</div>
    <div class="col-6">Второй блок переносится</div>
</div>
```

`row` реализован на Flexbox. Упрощённо:

```css
.row {
    display: flex;
    flex-wrap: wrap;
}
```

В реальном Bootstrap у строки также есть настройки gutters (отступов между колонками).

---

## 5. Адаптивность и breakpoints

**Breakpoint** — минимальная ширина окна, начиная с которой активируется соответствующее правило.

| Префикс | Начальная ширина |
|---|---:|
| Без префикса: `col-12` | 0 px |
| `sm` | 576 px |
| `md` | 768 px |
| `lg` | 992 px |
| `xl` | 1200 px |
| `xxl` | 1400 px |

Bootstrap использует подход **Mobile First**: сначала правила для маленького экрана, затем — для больших.

```html
<div class="row g-3">
    <div class="col-12 col-md-6 col-lg-4">
        Карточка
    </div>
</div>
```

Что происходит:

| Ширина окна | Активная ширина карточки |
|---|---|
| Менее 768 px | `col-12` → 100% |
| От 768 до 991 px | `col-md-6` → 50% |
| От 992 px | `col-lg-4` → 33,33% |

`col-md-6` означает **«от 768 px и выше, пока не переопределено»**, а не «только на планшетах».

### Пример: шесть адаптивных карточек

```html
<div class="container py-4">
    <div class="row g-3">
        <div class="col-12 col-md-6 col-lg-4"><div class="bg-primary text-white p-3">1</div></div>
        <div class="col-12 col-md-6 col-lg-4"><div class="bg-primary text-white p-3">2</div></div>
        <div class="col-12 col-md-6 col-lg-4"><div class="bg-primary text-white p-3">3</div></div>
        <div class="col-12 col-md-6 col-lg-4"><div class="bg-primary text-white p-3">4</div></div>
        <div class="col-12 col-md-6 col-lg-4"><div class="bg-primary text-white p-3">5</div></div>
        <div class="col-12 col-md-6 col-lg-4"><div class="bg-primary text-white p-3">6</div></div>
    </div>
</div>
```

На телефоне — по одной; на планшете — по две; на компьютере — по три карточки в строке.

---

## 6. Гибкие и автоматические колонки

Три часто встречающихся варианта:

| Класс | Смысл |
|---|---|
| `col` | Гибкая колонка, делящая свободное пространство с другими `col` |
| `col-4` | Фиксированная доля: 4 из 12, то есть 33,33% |
| `col-auto` | Ширина определяется содержимым |

### Пример с `col-auto`

```html
<div class="row">
    <div class="col">Левая часть</div>
    <div class="col-auto">Кнопка</div>
    <div class="col">Правая часть</div>
</div>
```

Центральный блок занимает ширину по содержимому, а крайние колонки делят оставшееся пространство.

### Пример из практики: `col-sm-2`, `col-sm`, `col-sm-4`

```html
<div class="row g-2">
    <div class="col-12 col-sm-2"><div class="bg-warning p-2">A</div></div>
    <div class="col-12 col-sm"><div class="bg-warning p-2">B</div></div>
    <div class="col-12 col-sm-4"><div class="bg-warning p-2">C</div></div>
    <div class="col-12 col-sm-4"><div class="bg-warning p-2">D</div></div>
</div>
```

На экранах от 576 px фиксированные колонки занимают `2 + 4 + 4 = 10` частей. Гибкая `col-sm` может занять оставшиеся `2` части. На маленьких экранах каждая `col-12` занимает отдельную строку.

### `col` и `col-sm-auto` в одной строке

```html
<div class="row g-2">
    <div class="col"><div class="bg-danger text-white p-2">Левая</div></div>
    <div class="col col-sm-auto"><div class="bg-danger text-white p-2">Центр</div></div>
    <div class="col"><div class="bg-danger text-white p-2">Правая</div></div>
</div>
```

Ниже 576 px все три блока гибкие. От 576 px центральный получает ширину по содержимому, а остальные занимают оставшееся пространство. Его поведение на маленьких экранах отличается от варианта только с `col-sm-auto` (без `col`).

---

## 7. `row-cols-*` и вложенные сетки

Если у всех карточек одинаковая ширина, можно назначить количество колонок непосредственно строке:

```html
<div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-3">
    <div class="col">Карточка 1</div>
    <div class="col">Карточка 2</div>
    <div class="col">Карточка 3</div>
    <div class="col">Карточка 4</div>
    <div class="col">Карточка 5</div>
    <div class="col">Карточка 6</div>
</div>
```

- `row-cols-1` — одна карточка на строку.
- `row-cols-md-2` — две от 768 px.
- `row-cols-lg-3` — три от 992 px.

**Отличие:** `col-md-6` назначают конкретной колонке, а `row-cols-md-2` — общему родителю.

### Вложенные сетки

Внутри колонки можно создать ещё одну строку:

```html
<div class="container">
    <div class="row g-3">
        <aside class="col-12 col-lg-3">Меню</aside>

        <main class="col-12 col-lg-9">
            <div class="row row-cols-1 row-cols-md-2 g-3">
                <div class="col">Товар 1</div>
                <div class="col">Товар 2</div>
            </div>
        </main>
    </div>
</div>
```

Внутренняя `row` ориентируется на ширину своего контейнера, а не всей страницы. Поэтому содержимое `<main>` можно делить независимо от боковой панели.

---

## 8. Gutters: `g`, `gx`, `gy` и отличие от `gap`

В Bootstrap есть два разных механизма расстояний:

| Класс | Принцип действия | Где лучше применять |
|---|---|---|
| `g-3` | Горизонтальные и вертикальные gutters сетки | `row` с `col` |
| `gx-3` | Только горизонтальные gutters | `row` |
| `gy-3` | Только вертикальные gutters | `row` |
| `g-0` | Убирает gutters | `row` |
| `gap-3` | Обычный CSS `gap` | `d-flex`, `d-grid` |

### Почему `gap-2` иногда «ломает» Bootstrap row?

Рассмотрим:

```html
<div class="row gap-2">
    <div class="col-sm-2">A</div>
    <div class="col-sm">B</div>
    <div class="col-sm-4">C</div>
    <div class="col-sm-4">D</div>
</div>
```

Фиксированные ширины колонок рассчитываются в долях от 12, **а CSS `gap` добавляет промежутки поверх этих ширин**. В некоторых сочетаниях это приводит к переносу, хотя сумма долей не превышает 12.

**Предпочтительнее:**

```html
<div class="row g-2">
    <div class="col-sm-2"><div class="bg-warning p-2">A</div></div>
    <div class="col-sm"><div class="bg-warning p-2">B</div></div>
    <div class="col-sm-4"><div class="bg-warning p-2">C</div></div>
    <div class="col-sm-4"><div class="bg-warning p-2">D</div></div>
</div>
```

Gutters в стандартной Flexbox-сетке организованы через внутренние отступы колонок и компенсирующие внешние отступы строки, поэтому корректно учитываются при распределении 12 частей. Для видимых промежутков между цветными блоками фон лучше задавать **внутренним дочерним элементам**.

---

## 9. Flexbox: `d-flex` и направление

### `d-flex`

По умолчанию блочные `<div>` стоят друг под другом:

```html
<div>
    <div>A</div>
    <div>B</div>
    <div>C</div>
</div>
```

Чтобы сделать их Flexbox-элементами:

```html
<div class="d-flex gap-2">
    <div class="bg-primary text-white p-3">A</div>
    <div class="bg-primary text-white p-3">B</div>
    <div class="bg-primary text-white p-3">C</div>
</div>
```

В обычном направлении текста они выстроятся горизонтально.

### `flex-direction`

| Класс | Результат |
|---|---|
| `flex-row` | Горизонтально |
| `flex-row-reverse` | Горизонтально в обратном порядке |
| `flex-column` | Вертикально |
| `flex-column-reverse` | Вертикально в обратном порядке |

```html
<div class="d-flex flex-column gap-2">
    <div>A</div>
    <div>B</div>
    <div>C</div>
</div>
```

Можно изменять направление адаптивно:

```html
<div class="d-flex flex-column flex-md-row gap-3">
    <div>Логотип</div>
    <div>Меню</div>
    <div>Профиль</div>
</div>
```

На узком экране элементы стоят друг под другом. Начиная с 768 px — в ряд.

---

## 10. Выравнивание по осям

В Flexbox нужно различать **главную** и **поперечную** оси:

- При `flex-row` главная ось горизонтальная, поперечная — вертикальная.
- При `flex-column` главная ось вертикальная, поперечная — горизонтальная.

### `justify-content-*`: главная ось

| Класс | Значение |
|---|---|
| `justify-content-start` | В начало |
| `justify-content-center` | По центру |
| `justify-content-end` | В конец |
| `justify-content-between` | Крайние у краёв, свободное место между ними |
| `justify-content-around` | Пространство вокруг каждого элемента |
| `justify-content-evenly` | Равные промежутки между элементами и краями |

```html
<header class="d-flex justify-content-between p-3 bg-dark text-white">
    <div>Логотип</div>
    <nav>Навигация</nav>
    <div>Профиль</div>
</header>
```

### `align-items-*`: поперечная ось

| Класс | Значение |
|---|---|
| `align-items-start` | К началу поперечной оси |
| `align-items-center` | По центру поперечной оси |
| `align-items-end` | К концу поперечной оси |
| `align-items-stretch` | Растягивание, когда размеры позволяют |
| `align-items-baseline` | По базовой линии текста |

### Центрирование сразу по двум осям

```html
<div class="d-flex justify-content-center align-items-center vh-100">
    <button class="btn btn-primary">Войти</button>
</div>
```

- `d-flex` — включаем Flexbox.
- `justify-content-center` — центр по главной (горизонтальной) оси.
- `align-items-center` — центр по поперечной (вертикальной) оси.
- `vh-100` — высота 100% от высоты окна браузера.

### `align-self-*`: выровнять только один элемент

```html
<div class="d-flex align-items-center" style="height: 160px;">
    <div class="p-3 bg-primary text-white">A</div>
    <div class="p-3 bg-warning align-self-start">B</div>
    <div class="p-3 bg-primary text-white">C</div>
</div>
```

Все элементы ориентируются на `align-items-center`, кроме B: для него задан `align-self-start`.

Доступны также `align-self-end`, `align-self-center`, `align-self-baseline`, `align-self-stretch`.

---

## 11. Перенос, растяжение и порядок

### `flex-wrap`

```html
<div class="d-flex flex-wrap gap-2">
    <button class="btn btn-primary">HTML</button>
    <button class="btn btn-primary">CSS</button>
    <button class="btn btn-primary">JavaScript</button>
    <button class="btn btn-primary">Bootstrap</button>
</div>
```

Элементы могут переходить на следующую строку, если ширины недостаточно.

| Класс | Действие |
|---|---|
| `flex-nowrap` | Запретить перенос |
| `flex-wrap` | Разрешить перенос |
| `flex-wrap-reverse` | Перенос с обратным направлением строк |

### `flex-grow-1`

```html
<div class="d-flex gap-2">
    <div class="flex-grow-1 bg-light p-3">Поиск</div>
    <button class="btn btn-primary">Найти</button>
</div>
```

Левый блок занимает доступное свободное пространство.

### `flex-shrink-0`

```html
<div class="d-flex gap-2">
    <div class="flex-grow-1">Длинный текст</div>
    <button class="btn btn-primary flex-shrink-0">Кнопка</button>
</div>
```

Кнопка не сжимается по Flexbox-алгоритму. При дефиците места это может вызвать переполнение.

### `flex-fill`

```html
<div class="d-flex">
    <div class="flex-fill p-2 bg-info">A</div>
    <div class="flex-fill p-2 bg-warning">B</div>
</div>
```

Позволяет элементам гибко использовать доступное пространство, но **не гарантирует строго равные итоговые ширины при любом содержимом**.

### `order-*`

```html
<div class="d-flex">
    <div class="order-2">A</div>
    <div class="order-1">B</div>
    <div class="order-3">C</div>
</div>
```

Визуальный порядок: B, A, C. Существуют `order-0`…`order-5`, `order-first`, `order-last`, а также адаптивные варианты (например, `order-lg-1`).

> `order` не изменяет порядок узлов HTML и не обязательно меняет порядок клавиатурной навигации. Не следует использовать его как замену логичной структуре документа.

---

## 12. `hstack`, `vstack` и автоматические отступы

### `hstack`

```html
<div class="hstack gap-3">
    <div>Главная</div>
    <div>Каталог</div>
    <div>Контакты</div>
</div>
```

Это удобный помощник для горизонтального Flexbox с вертикальным выравниванием по центру.

### `vstack`

```html
<div class="vstack gap-3">
    <h3>Карточка</h3>
    <p>Описание</p>
    <button class="btn btn-primary">Купить</button>
</div>
```

Элементы располагаются вертикально.

### `ms-auto`

```html
<div class="d-flex align-items-center gap-3">
    <div>Логотип</div>
    <div>Каталог</div>
    <div class="ms-auto">Профиль</div>
</div>
```

`ms-auto` добавляет автоматический отступ со стороны начала строки (*margin-start*), отодвигая блок к концу доступного пространства. В интерфейсах с направлением слева направо профиль окажется справа.

`me-auto` действует противоположным образом — автоматический отступ со стороны конца строки.

---

## 13. Grid: что поддерживает Bootstrap

### Главное различие

1. **Bootstrap Grid System:** `row`, `col`, `row-cols-*` — стандартная 12-колоночная сетка, основанная на Flexbox.
2. **CSS Grid:** отдельный механизм CSS, который можно включать через `display: grid`.

### `d-grid` в стандартной CDN-версии

```html
<div class="d-grid gap-2">
    <button class="btn btn-primary">Сохранить</button>
    <button class="btn btn-secondary">Отмена</button>
</div>
```

Здесь `d-grid` включает `display: grid`, а `gap-2` задаёт промежуток. Без явного описания колонок кнопки обычно располагаются одна под другой и заполняют доступную ширину.

Чтобы получить три колонки, можно добавить CSS:

```html
<div class="d-grid gap-3" style="grid-template-columns: repeat(3, 1fr);">
    <div class="bg-primary text-white p-3">A</div>
    <div class="bg-primary text-white p-3">B</div>
    <div class="bg-primary text-white p-3">C</div>
</div>
```

### Экспериментальная система `.grid` / `.g-col-*`

В Bootstrap 5.3 существует отдельная экспериментальная CSS Grid-система:

```html
<div class="grid">
    <div class="g-col-4">A</div>
    <div class="g-col-4">B</div>
    <div class="g-col-4">C</div>
</div>
```

**Внимание:** эти классы **не работают как готовая система CSS Grid в стандартной CSS-сборке из CDN**. Для них Bootstrap нужно собрать с Sass-параметром `$enable-cssgrid: true`.

В обычной работе с готовым Bootstrap CDN для сетки карточек чаще удобнее `row row-cols-...`.

---

## 14. Размеры, отступы и отображение

### Margin и Padding

Формула имени класса: `{свойство}{сторона}-{размер}`.

| Обозначение | Смысл |
|---|---|
| `m` | `margin` — внешний отступ |
| `p` | `padding` — внутренний отступ |
| `t` | Сверху |
| `b` | Снизу |
| `s` | С начала строки |
| `e` | С конца строки |
| `x` | По горизонтали |
| `y` | По вертикали |

Размеры при стандартной базовой настройке `1rem = 16px`:

| Размер | Значение |
|---|---:|
| `0` | 0 |
| `1` | 4 px |
| `2` | 8 px |
| `3` | 16 px |
| `4` | 24 px |
| `5` | 48 px |

```html
<div class="mt-3 mb-4 px-3 py-2">Контент</div>
```

Здесь внешний отступ сверху 16 px, снизу 24 px, внутренние горизонтальные отступы по 16 px и вертикальные по 8 px.

### Управление видимостью и отображением

```html
<div class="d-none d-md-block">
    Виден начиная с 768 px
</div>
```

```html
<div class="d-block d-lg-flex">
    На телефоне обычный блок, с 992 px Flexbox
</div>
```

Дополнительные классы:

- `w-100` — ширина 100%.
- `h-100` — высота 100% родительского элемента, когда её можно корректно определить.
- `vh-100` — высота 100% viewport.
- `text-center` — центрирование текста.

---

## 15. Полноценная страница интернет-магазина

В примере объединяются все основные механизмы:

- `container`, `row`, `col` — общий Layout;
- `row-cols-*` — адаптивная сетка карточек;
- `d-flex`, `justify-content-between`, `align-items-center` — шапка и управление;
- `vstack` — вертикальные фильтры;
- `g-3`, `gap-3`, `p-3`, `mb-3` — расстояния.

> Скопируйте код в `index.html` и откройте в браузере. Затем меняйте ширину окна, чтобы увидеть адаптивность.

```html
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Интернет-магазин — Bootstrap Layout</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container py-4">

        <header class="d-flex flex-column flex-md-row justify-content-between align-items-md-center gap-3 bg-dark text-white p-3 rounded">
            <h2 class="m-0">SHOP</h2>

            <nav class="d-flex flex-wrap gap-3">
                <a href="#products" class="text-white">Каталог</a>
                <a href="#footer" class="text-white">Контакты</a>
                <a href="#" class="text-white">Корзина</a>
            </nav>
        </header>

        <div class="row g-3 my-3">
            <aside class="col-12 col-lg-3">
                <div class="bg-light border rounded p-3 h-100">
                    <h4>Фильтры</h4>
                    <div class="vstack gap-2">
                        <label><input type="checkbox"> Электроника</label>
                        <label><input type="checkbox"> Книги</label>
                        <label><input type="checkbox"> Аксессуары</label>
                    </div>
                </div>
            </aside>

            <main class="col-12 col-lg-9" id="products">
                <div class="d-flex flex-wrap justify-content-between align-items-center gap-2 mb-3">
                    <h3 class="m-0">Каталог</h3>
                    <button class="btn btn-outline-primary">Сортировка</button>
                </div>

                <div class="row row-cols-1 row-cols-md-2 row-cols-xl-3 g-3">
                    <div class="col">
                        <div class="card h-100">
                            <div class="card-body d-flex flex-column">
                                <h5 class="card-title">Товар 1</h5>
                                <p class="card-text">Описание товара.</p>
                                <button class="btn btn-primary mt-auto">Купить</button>
                            </div>
                        </div>
                    </div>
                    <div class="col">
                        <div class="card h-100">
                            <div class="card-body d-flex flex-column">
                                <h5 class="card-title">Товар 2</h5>
                                <p class="card-text">Описание другого товара с более длинным текстом.</p>
                                <button class="btn btn-primary mt-auto">Купить</button>
                            </div>
                        </div>
                    </div>
                    <div class="col">
                        <div class="card h-100">
                            <div class="card-body d-flex flex-column">
                                <h5 class="card-title">Товар 3</h5>
                                <p class="card-text">Описание товара.</p>
                                <button class="btn btn-primary mt-auto">Купить</button>
                            </div>
                        </div>
                    </div>
                    <div class="col">
                        <div class="card h-100">
                            <div class="card-body d-flex flex-column">
                                <h5 class="card-title">Товар 4</h5>
                                <p class="card-text">Описание товара.</p>
                                <button class="btn btn-primary mt-auto">Купить</button>
                            </div>
                        </div>
                    </div>
                    <div class="col">
                        <div class="card h-100">
                            <div class="card-body d-flex flex-column">
                                <h5 class="card-title">Товар 5</h5>
                                <p class="card-text">Описание товара.</p>
                                <button class="btn btn-primary mt-auto">Купить</button>
                            </div>
                        </div>
                    </div>
                    <div class="col">
                        <div class="card h-100">
                            <div class="card-body d-flex flex-column">
                                <h5 class="card-title">Товар 6</h5>
                                <p class="card-text">Описание товара.</p>
                                <button class="btn btn-primary mt-auto">Купить</button>
                            </div>
                        </div>
                    </div>
                </div>
            </main>
        </div>

        <footer class="bg-dark text-white text-center p-3 rounded" id="footer">
            Footer · 2026
        </footer>
    </div>
</body>
</html>
```

### Почему использованы именно эти классы?

| Элемент | Классы | Причина |
|---|---|---|
| Шапка | `d-flex flex-column flex-md-row` | Вертикальное меню на телефоне, горизонтальное на больших экранах |
| Боковая панель | `col-12 col-lg-3` | Сверху на телефоне, 25% ширины на большом экране |
| Каталог | `col-12 col-lg-9` | Снизу на телефоне, 75% ширины на большом экране |
| Список товаров | `row-cols-1 row-cols-md-2 row-cols-xl-3` | 1 / 2 / 3 карточки в строке |
| Кнопки внутри карточек | `d-flex flex-column` и `mt-auto` | Кнопки «Купить» прижаты к низу содержимого карточек |
| Промежутки | `g-3` | Корректные расстояния между колонками Bootstrap |

---

## 16. Типичные ошибки

### Ошибка 1. `gap-*` вместо `g-*` внутри `row`

```html
<!-- Может приводить к неожиданному переносу -->
<div class="row gap-3">
    <div class="col-6">A</div>
    <div class="col-6">B</div>
</div>
```

В большинстве ситуаций с 12-колоночной сеткой используйте `row g-3`.

### Ошибка 2. Ожидание, что `col-md-6` работает только на планшете

Класс работает **от 768 px и выше**, если не переопределён классом более крупного breakpoint.

### Ошибка 3. Попытка центрировать по вертикали без свободной высоты

```html
<div class="d-flex align-items-center">
    <button>Кнопка</button>
</div>
```

Если высота контейнера совпадает с высотой кнопки, видимого перемещения не будет. Для демонстрации задайте высоту (`vh-100`, `min-vh-100` или иным способом).

### Ошибка 4. Считать, что `d-flex` задаёт одинаковую ширину детям

`d-flex` включает Flexbox, но сам по себе не делает ширины равными. Для распределения можно использовать `flex-fill`, `flex-grow-1` или систему колонок — в зависимости от задачи.

### Ошибка 5. Использовать `.grid` / `.g-col-*` в обычном CDN Bootstrap

Экспериментальная CSS Grid-система Bootstrap отключена в стандартной сборке. Для обычной CDN-страницы используйте `row`, `col`, `row-cols-*` или `d-grid` с собственными настройками CSS Grid.

### Ошибка 6. Указывать фон самой колонке и ожидать цветной промежуток от `g-3`

`g-*` создаёт внутренние отступы колонок. Чтобы между цветными блоками были видимые просветы, поместите фон внутрь дочернего элемента.

---

## 17. Практические задания

### Задание 1. Сетка из четырёх колонок

Создайте контейнер с четырьмя цветными блоками. На больших экранах все четыре должны занимать по 3/12 ширины, на экранах меньше 768 px — по одной колонке.

**Подсказка:** `col-12 col-md-3`.

### Задание 2. Адаптивные карточки

Создайте шесть карточек. Должно получиться:

- Телефон — 1 карточка в строке.
- Планшет — 2 карточки в строке.
- Компьютер — 3 карточки в строке.

Используйте `row-cols-*` и `g-3`.

### Задание 3. Шапка сайта на Flexbox

Разместите логотип слева, навигацию в середине и кнопку «Войти» справа. На телефоне сделайте вертикальное расположение.

**Подсказка:** `d-flex`, `flex-column`, `flex-md-row`, `justify-content-between`, `align-items-md-center`.

### Задание 4. Центрирование

Создайте экран входа с кнопкой строго по центру окна. Разрешено использовать только утилиты Bootstrap, без собственного CSS.

**Подсказка:** `d-flex justify-content-center align-items-center min-vh-100`.

### Задание 5. Боковая панель и контент

Создайте Layout из бокового меню (3/12) и контента (9/12). На телефоне блоки должны располагаться друг под другом.

**Подсказка:** `col-12 col-lg-3` и `col-12 col-lg-9`.

### Задание 6. Исследование `gap` и `g`

Создайте две одинаковые строки из двух элементов `col-6`. У первой укажите `gap-3`, у второй — `g-3`. Сравните результат на разных размерах экрана и объясните, почему они отличаются.

### Задание 7. Панель управления

Создайте шапку, боковое меню, три статистические карточки и таблицу. Основной Layout сделайте через `row`/`col`, выравнивание внутри карточек — через Flexbox.

### Задание 8. Мини-проект

На основе раздела 15 реализуйте интернет-магазин: добавьте ещё три товара, поле поиска, кнопку очистки фильтров и адаптивную нижнюю часть страницы.

**Критерии готовности:** нет горизонтальной прокрутки на мобильном экране; колонки корректно перестраиваются; видимые расстояния между карточками одинаковые; все основные блоки выровнены.

---

## 18. Контрольный тест

1. Какой класс включает Flexbox-контейнер?  
   A. `container`  
   B. `d-flex`  
   C. `col-12`  
   D. `gap-3`

2. Что означает `col-md-6`?  
   A. Ширина 6 пикселей  
   B. Шесть колонок на телефоне  
   C. Начиная с 768 px занимает половину строки  
   D. Шесть строк

3. Какой класс распределяет элементы по краям с промежутками между ними?  
   A. `align-items-center`  
   B. `justify-content-between`  
   C. `flex-column`  
   D. `col-auto`

4. Как задать промежутки между колонками стандартной сетки Bootstrap?  
   A. `gap-3`  
   B. `mt-3`  
   C. `g-3`  
   D. `flex-fill`

5. Как вывести 1 карточку на телефоне, 2 на планшете и 3 на компьютере?  
   A. `row-cols-1 row-cols-md-2 row-cols-lg-3`  
   B. `col-1 col-2 col-3`  
   C. `d-flex flex-row`  
   D. `g-1 g-md-2 g-lg-3`

6. Чем `col-auto` отличается от `col-4`?

7. Почему при использовании `row gap-2` сумма долей колонок, равная 12, иногда всё равно вызывает перенос?

8. В каком направлении работает `justify-content-center`, если указан `flex-column`?

9. Что делает `ms-auto` в горизонтальном Flexbox при обычном направлении текста?

10. Почему `d-grid` не обязательно создаёт три колонки самостоятельно?

<details>
<summary><strong>Ответы к тесту</strong></summary>

1. **B** — `d-flex`.
2. **C** — от 768 px ширина 6/12.
3. **B** — `justify-content-between`.
4. **C** — `g-3`.
5. **A** — `row-cols-1 row-cols-md-2 row-cols-lg-3`.
6. `col-auto` зависит от содержимого; `col-4` занимает 4/12 ширины строки.
7. `gap` добавляет расстояние сверх процентных размеров колонок, поэтому общая ширина может превысить доступную.
8. По вертикали, так как главная ось `flex-column` вертикальная.
9. Отодвигает элемент к правому краю, когда остаётся свободное место.
10. Потому что `d-grid` только включает CSS `display: grid`; количество колонок нужно определить дополнительно.

</details>

---

## 19. Шпаргалка и ссылки

### Быстрая шпаргалка

| Задача | Классы |
|---|---|
| Ограничить ширину сайта | `container` |
| Вся ширина | `container-fluid` |
| Создать стандартную сетку | `row` + `col` |
| Разделить на 25% и 75% | `col-3` + `col-9` |
| Три карточки на компьютере | `row-cols-lg-3` |
| Задать расстояния между колонками | `g-3` |
| Включить Flexbox | `d-flex` |
| Расположить элементы вертикально | `flex-column` |
| Центрировать по главной оси | `justify-content-center` |
| Центрировать по поперечной оси | `align-items-center` |
| Раздвинуть элементы по краям | `justify-content-between` |
| Разрешить перенос Flex-элементов | `flex-wrap` |
| Прижать элемент вправо в LTR | `ms-auto` |
| Расположить содержимое стопкой | `vstack` |
| Включить CSS Grid | `d-grid` |
| Скрыть до 768 px | `d-none d-md-block` |

### Официальная документация Bootstrap 5.3

- [Layout Overview](https://getbootstrap.com/docs/5.3/layout/)
- [Containers](https://getbootstrap.com/docs/5.3/layout/containers/)
- [Grid System](https://getbootstrap.com/docs/5.3/layout/grid/)
- [Breakpoints](https://getbootstrap.com/docs/5.3/layout/breakpoints/)
- [Columns](https://getbootstrap.com/docs/5.3/layout/columns/)
- [Gutters](https://getbootstrap.com/docs/5.3/layout/gutters/)
- [Flex utilities](https://getbootstrap.com/docs/5.3/utilities/flex/)
- [Spacing utilities](https://getbootstrap.com/docs/5.3/utilities/spacing/)
- [Stacks](https://getbootstrap.com/docs/5.3/helpers/stacks/)
- [CSS Grid](https://getbootstrap.com/docs/5.3/layout/css-grid/)

---

**Вывод:** для структуры страницы и адаптивных карточек обычно выбирают `container`, `row`, `col` и `row-cols-*`; для выравнивания элементов внутри блоков — `d-flex`, `justify-content-*` и `align-items-*`; для расстояний используют `g-*` в стандартной сетке и `gap-*` во Flexbox или CSS Grid.
