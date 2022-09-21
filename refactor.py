import csv

import model


class SQLiteDataBase:
    def __init__(self) -> None:
        self.__models: dict[str : model.BaseModel] = model.MODELS

    def connect(self) -> None:
        model.database.connect()

    def __str__(self) -> str:
        return "\n".join(list(self.__models))

    def __repr__(self) -> str:
        return str(list(self.__models))

    def get_table(self, tablename: str) -> dict:
        return self.__models.get(tablename, {"NotFound": None})

    def to_csv(self, filename: str, tablename: str) -> None:
        table = self.get_table(tablename)
        header = list(table.select().dicts()[0].keys())
        with open(filename, "w") as csvfile:
            writer = csv.DictWriter(csvfile, header, delimiter=";")
            for row in table.select().dicts():
                writer.writerow(row)


def main():
    sql_db = SQLiteDataBase()
    sql_db.connect()
    sql_db.to_csv("data.csv", "Customer")


if __name__ == "__main__":
    main()
