# Py Transport Perm API
Библиотека для получения расписания транспорта г. Перми.

## Оглавление
1. [Старт](#Старт)
    + [PyPI](#Установка-через-pypi)
    + [Инициализация](#Инициализация)
2. [Использование](#Использование)
    + [Список всех видов транспорта](#Список-всех-видов-транспорта)
    + [Вид транспорта](#Вид-транспорта)
    + [Маршруты остановки](#Маршруты-остановки)
    + [Ближайшие прибытия транспорта](#Ближайшие-прибытия-транспорта)
    + [Расписание движения транспорта по остановке](#Расписание-движения-транспорта-по-остановке)
    + [Расписание движения](#Расписание-движения)
    + [Онлайн расписание транспорта](#Онлайн-расписание-транспорта)
    + [Поиск](#Поиск)
    + [Новости](#Новости)
    + [Табло](#Табло)
    + [Точки проездных](#Точки-проездных)
3. [Автор](#Автор)
4. [Лицензия](#Лицензия)

## Старт
### Установка через PyPI
```

```
### Инициализация
```python
transperm = TransPerm()
```

## Использование
### Список всех видов транспорта
```python
def getRouteTypesTree(date: str) -> dict
```
Название | Тип | Описание
---------|-----|----------------------
date | string | Дата в формате `d.m.Y`

### Вид транспорта
```python
def getFullRoute(date: str, route_id: str) -> dict
```
Название | Тип | Описание
---------|-----|----------------------
date | string | Дата в формате `d.m.Y`
route_id | string | ID транспорта

### Маршруты остановки
```python
def getStoppointRoutes(date: str, stoppoint_id: str) -> dict
```
Название | Тип | Описание
---------|-----|----------------------
date | string | Дата в формате `d.m.Y`
stoppoint_id | string | ID остановки

### Ближайшие прибытия транспорта
```python
def getArrivalTimesVehicles(stoppoint_id: str) -> dict
```
Название | Тип | Описание
---------|-----|----------------------
stoppoint_id | string | ID остановки

### Расписание движения транспорта по остановке
```python
def getStoppointTimeTable(date: str, stoppoint_id: str) -> dict
```
Название | Тип | Описание
---------|-----|----------------------
date | string | Дата в формате `d.m.Y`
stoppoint_id | string | ID остановки

### Расписание движения
```python
def getTimeTableH(self, date: str, route_id: str, stoppoint_id: str) -> dict
```
Название | Тип | Описание
---------|-----|----------------------
date | string | Дата в формате `d.m.Y`
route_id | string | ID транспорта
stoppoint_id | string | ID остановки


### Онлайн расписание транспорта
```python
def getMovingAutos(self, route_id: str)
```
Название | Тип | Описание
---------|-----|----------------------
route_id | string | ID транспорта

### Поиск
```python
def search(query: str) -> dict
```
Название | Тип | Описание
---------|-----|----------------------
query | string | Поисковой запрос

### Новости
```python
def getNews() -> dict
```

### Табло
```python
def getBoards() -> dict
```

### Точки проездных
```python
def getTicketPoints() -> dict
```

## Автор
[Alexander Pushkarev](https://github.com/axp-dev), e-mail: [axp-dev@yandex.com](mailto:axp-dev@yandex.com)

## Лицензия
Основой Transport Perm API являет открытый исходный код, в соответствии [MIT license](https://opensource.org/licenses/MIT)