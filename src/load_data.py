import pandas as pd


def load_csv(path: str) -> pd.DataFrame:
    """
    Загружает CSV файл в датафрейм.

    :param path: путь к файлу
    :return: pandas DataFrame
    """
    return pd.read_csv(path)


if __name__ == "__main__":
    # быстрый тест загрузки файлов
    source = load_csv("data/source_orders.csv")
    target = load_csv("data/target_orders.csv")

    print("SOURCE SHAPE:", source.shape)
    print(source.head())

    print("TARGET SHAPE:", target.shape)
    print(target.head())
