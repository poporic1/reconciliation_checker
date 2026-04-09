import pandas as pd


def find_duplicates(df: pd.DataFrame, key_columns: list[str]) -> pd.DataFrame:
    """
    Находит дубли в датафрейме по заданным колонкам.

    :param df: входной датафрейм
    :param key_columns: список колонок, по которым проверяются дубли
    :return: датафрейм только с дублирующимися строками
    """
    mask = df.duplicated(subset=key_columns, keep=False)

    return df.loc[mask].sort_values(key_columns)
