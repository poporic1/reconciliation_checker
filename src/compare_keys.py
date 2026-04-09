import pandas as pd


def find_missing_keys(
    source: pd.DataFrame, target: pd.DataFrame, key_columns: list[str]
):
    """
    Ищет отсутствующие ключи между двумя датафреймами.

    :param source: исходный датафрейм
    :param target: целевой датафрейм
    :param key_columns: список колонок-ключей
    :return: два датафрейма:
        - ключи, которые есть в source, но нет в target
        - ключи, которые есть в target, но нет в source
    """
    # оставляем только уникальные ключи
    source_keys = source[key_columns].drop_duplicates()
    target_keys = target[key_columns].drop_duplicates()

    # ищем ключи, которые есть в source, но нет в target
    missing_in_target = source_keys.merge(
        target_keys, on=key_columns, how="left", indicator=True
    )
    missing_in_target = missing_in_target[missing_in_target["_merge"] == "left_only"]
    missing_in_target = missing_in_target.drop(columns=["_merge"])

    # ищем наоборот: есть в target, но нет в source
    missing_in_source = target_keys.merge(
        source_keys, on=key_columns, how="left", indicator=True
    )
    missing_in_source = missing_in_source[missing_in_source["_merge"] == "left_only"]
    missing_in_source = missing_in_source.drop(columns=["_merge"])

    return missing_in_target, missing_in_source
