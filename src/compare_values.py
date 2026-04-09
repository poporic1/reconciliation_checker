import pandas as pd


def compare_values(
    source: pd.DataFrame,
    target: pd.DataFrame,
    key_columns: list[str],
    compare_columns: list[str],
) -> pd.DataFrame:
    """
    Сравнивает значения между двумя датафреймами по заданным колонкам.

    :param source: исходный датафрейм
    :param target: целевой датафрейм
    :param key_columns: колонки для объединения (ключи)
    :param compare_columns: колонки, значения которых нужно сравнить
    :return: датафрейм с найденными расхождениями
    """
    # suffixes нужны, чтобы различать source и target колонки
    merged = source.merge(
        target, on=key_columns, how="inner", suffixes=("_source", "_target")
    )

    mismatches = []

    # идем по каждой строке
    for _, row in merged.iterrows():
        for col in compare_columns:
            source_value = row[f"{col}_source"]
            target_value = row[f"{col}_target"]

            # если оба значения NaN - считаем, что они равны
            if pd.isna(source_value) and pd.isna(target_value):
                continue

            # если значения отличаются - фиксируем
            if source_value != target_value:
                mismatch_row = {k: row[k] for k in key_columns}
                mismatch_row["column_name"] = col
                mismatch_row["source_value"] = source_value
                mismatch_row["target_value"] = target_value
                mismatches.append(mismatch_row)

    return pd.DataFrame(mismatches)
