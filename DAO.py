from database.DB_connect import DBConnect
from model.stato import Stato


class DAO():

    @staticmethod
    def getStates():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select s.*
                from state s """

        cursor.execute(query,)

        for row in cursor:
            result.append(Stato(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNeighbors():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select n.*
                from neighbor n  """

        cursor.execute(query, )

        for row in cursor:
            result.append((row["state1"],row["state2"]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getPeso(u,v,anno,giorno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select (count(distinct s.id)+count(distinct s2.id)) as tot
                    from sighting s, sighting s2 
                    where (s.state = %s and s2.state = %s) and year(s.`datetime`) = year(s2.`datetime`) and year(s.`datetime`) = %s 
                    and abs(datediff(s2.`datetime`,s.`datetime`)) <=%s """

        cursor.execute(query,(u.lower(),v.lower(),anno,giorno,))

        for row in cursor:
            result.append(row["tot"])

        cursor.close()
        conn.close()
        return result