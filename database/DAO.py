from database.DB_connect import DBConnect
from model.confine import Confine
from model.country import Country


class DAO():
    # def __init__(self):
    #     pass

    @staticmethod
    def getAllCountries():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []

        query = """select *
                    from country c"""

        cursor.execute(query)

        for row in cursor:
            result.append(Country(**row))

        cursor.close()
        conn.close()

        return result

    @staticmethod
    def getArchi(anno):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []

        query = """select *
                    from contiguity c 
                    where c.state1no < c.state2no 
                    and c.`year` <= %s
                    and c.conttype = 1"""

        cursor.execute(query, (anno,))

        for row in cursor:
            result.append(Confine(**row))

        cursor.close()
        conn.close()

        return result

    @staticmethod
    def getNodi(anno):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []

        query = """select *
                    from contiguity c 
                    where c.state1no < c.state2no 
                    and c.`year` <= %s"""

        cursor.execute(query, (anno,))

        for row in cursor:
            result.append(Confine(**row))

        cursor.close()
        conn.close()

        return result