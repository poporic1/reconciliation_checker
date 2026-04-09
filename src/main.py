import json
from src.load_data import load_csv
from src.check_duplicates import find_duplicates
from src.check_counts import check_counts
from src.compare_keys import find_missing_keys
from src.compare_values import compare_values
from src.write_summary import build_summary

# конфиг читаем из json
source_file = ""
target_file = ""
key_columns = []
compare_columns = []

with open("config/reconciliation_config.json") as file:
    json_data = json.load(file)

    source_file = json_data["source_file"]
    target_file = json_data["target_file"]
    key_columns = json_data["key_columns"]
    compare_columns = json_data["compare_columns"]

# загружаем данные
source_file_data = load_csv(source_file)
target_file_data = load_csv(target_file)

# ищем дубли отдельно в source и target
source_duplicates = find_duplicates(source_file_data, key_columns)
target_duplicates = find_duplicates(target_file_data, key_columns)

# сравниваем количество строк
check_counts_results = check_counts(source_file_data, target_file_data)

# ищем отсутствующие ключи
missing_source_keys_results, missing_target_keys_results = find_missing_keys(
    source_file_data, target_file_data, key_columns
)

# сравниваем значения по колонкам
mismatches_results = compare_values(
    source_file_data, target_file_data, key_columns, compare_columns
)

# собираем итоговую сводку
summary_result = build_summary(
    check_counts_results,
    missing_target_keys_results,
    missing_source_keys_results,
    mismatches_results,
)

# сохраняем результат
summary_result.to_csv(
    "output/summary_result.csv",
    index=False,
    columns=[
        "source_rows",
        "target_rows",
        "counts_match",
        "missing_in_target_count",
        "missing_in_source_count",
        "value_mismatch_count",
        "compared_at",
    ],
)
