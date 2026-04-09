import pandas as pd


def check_counts(source: pd.DataFrame, target: pd.DataFrame) -> dict:
    """
    Сравнивает количество строк в двух датафреймах.

    :param source: исходный датафрейм
    :param target: целевой датафрейм
    :return: словарь с количеством строк и флагом совпадения
    """
    source_rows = len(source)
    target_rows = len(target)

    # возвращаем простой словарь с результатом
    return {
        "source_rows": source_rows,
        "target_rows": target_rows,
        # проверка: совпадает ли количество строк
        "counts_match": source_rows == target_rows,
    }
