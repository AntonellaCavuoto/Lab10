from database.DAO import DAO

list = DAO.getConfini(2000)
c = DAO.getAllCountries()

print(len(c))

print(len(list))