import peewee as pw
from playhouse.reflection import generate_models

DB = pw.SqliteDatabase("Chinook_Sqlite_AutoIncrementPKs.sqlite")


class SQLiteDataBase:
    def __init__(self, database: pw.SqliteDatabase) -> None:
        self.__DB = database
        self.__models = generate_models(self.__DB)
        globals().update(self.__models)

    def __str__(self) -> str:
        return "\n".join(list(self.__models))

    def __repr__(self) -> str:
        return str(list(self.__models))


def main():
    sql_db = SQLiteDataBase(DB)
    print(sql_db)


if __name__ == "__main__":
    main()
