from datetime import datetime
import pandas as pd


def build_summary(
    counts: dict,
    missing_in_target: pd.DataFrame,
    missing_in_source: pd.DataFrame,
    mismatches: pd.DataFrame,
) -> pd.DataFrame:
    """
    Формирует итоговую сводку по результатам сравнения данных.

    :param counts: результат проверки количества строк
    :param missing_in_target: ключи, отсутствующие в target
    :param missing_in_source: ключи, отсутствующие в source
    :param mismatches: найденные расхождения значений
    :return: датафрейм с итоговой статистикой
    """
    return pd.DataFrame(
        [
            {
                "source_rows": counts["source_rows"],
                "target_rows": counts["target_rows"],
                "counts_match": counts["counts_match"],
                # считаем количество проблем
                "missing_in_target_count": len(missing_in_target),
                "missing_in_source_count": len(missing_in_source),
                "value_mismatch_count": len(mismatches),
                # добавляем время проверки
                "compared_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
        ]
    )
