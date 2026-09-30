import pickle

class Database:
    File_Name = "account.dat"

    @staticmethod
    def save(account):
        with open(Database.File_Name, "wb") as file:
            pickle.dump(account, file)

    @staticmethod
    def load():
        try:
            with open(Database.File_Name, "rb") as file:
                return pickle.load(file)
        except:
            return {}