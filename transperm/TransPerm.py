import requests
import json


class TransPerm:
    """
    Библиотека для получения расписания транспорта г. Перми.
    """

    endpoints = {
        'route-types-tree': 'http://www.map.gortransperm.ru/json/route-types-tree/{}/',
        'full-route': 'http://www.map.gortransperm.ru/json/full-route/{}/{}/',
        'stoppoint-routes': 'http://www.map.gortransperm.ru/json/stoppoint-routes/{}/{}',
        'arrival-times-vehicles': 'http://www.map.gortransperm.ru/json/arrival-times-vehicles/{}',
        'stoppoint-time-table': 'http://www.map.gortransperm.ru/json/stoppoint-time-table/{}/{}',
        'time-table-h': 'http://www.map.gortransperm.ru/json/time-table-h/{}/{}/{}',
        'search': 'http://www.map.gortransperm.ru/json/search?q={}',
        'get-moving-autos': 'http://www.map.gortransperm.ru/json/get-moving-autos/-{}-',
        'news-links': 'http://www.map.gortransperm.ru/json/news-links',
        'boards': 'http://www.map.gortransperm.ru/json/boards',
        'ticket-points': 'http://www.map.gortransperm.ru/json/ticket-points',
    }

    def getRouteTypesTree(self, date: str) -> dict:
        """
        Список всех видов транспорта

        :param date: дата
        """
        return self.__query(url=self.endpoints['route-types-tree'].format(date))

    def getFullRoute(self, date: str, route_id: str) -> dict:
        """
        Полный маршрут

        :param date: дата
        :param route_id: id маршрута
        """
        return self.__query(url=self.endpoints['full-route'].format(date, route_id))

    def getStoppointRoutes(self, date: str, stoppoint_id: str) -> dict:
        """
        Маршруты остановки

        :param date: дата
        :param stoppoint_id: id остановки
        """
        return self.__query(url=self.endpoints['stoppoint-routes'].format(date, stoppoint_id))

    def getArrivalTimesVehicles(self, stoppoint_id: str) -> dict:
        """
        Ближайшие прибытия транспорта

        :param stoppoint_id: id остановки
        """
        return self.__query(url=self.endpoints['arrival-times-vehicles'].format(stoppoint_id))

    def getStoppointTimeTable(self, date: str, stoppoint_id: str) -> dict:
        """
        Расписание движения транспорта по остановке

        :param date: дата
        :param stoppoint_id: id остановки
        """
        return self.__query(url=self.endpoints['stoppoint-time-table'].format(date, stoppoint_id))

    def getTimeTableH(self, date: str, route_id: str, stoppoint_id: str) -> dict:
        """
        Расписание движения

        :param date: дата
        :param route_id: id маршрута
        :param stoppoint_id: id остановки
        """
        return self.__query(url=self.endpoints['time-table-h'].format(date, route_id, stoppoint_id))

    def search(self, query: str) -> dict:
        """
        Поиск

        :param query: поисковой запрос
        """
        return self.__query(url=self.endpoints['search'].format(query))

    def getMovingAutos(self, route_id: str) -> dict:
        """
        Онлайн расписание транспорта

        :param route_id:
        """
        return self.__query(url=self.endpoints['get-moving-autos'].format(route_id))

    def getNews(self) -> dict:
        """
        Новости Перми
        """
        return self.__query(url=self.endpoints['news-links'])

    def getBoards(self) -> dict:
        """
        Список всех точек и информационным таблом
        """
        return self.__query(url=self.endpoints['boards'])

    def getTicketPoints(self) -> dict:
        """
        Точки покупки проездных
        """
        return self.__query(url=self.endpoints['ticket-points'])

    def __query(self, url: str) -> dict:
        """
        HTTP запрос

        :param url: url куда делать запрос
        """
        response = requests.get(url=url)
        data = json.loads(response.text)

        return data
