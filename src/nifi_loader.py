import csv
from pathlib import Path
from typing import Tuple
import pandas as pd


def detect_delimiter(file_path: str, sample_size: int = 2048) -> str:
    """
    Detect the delimiter of a CSV-like file using Python's csv.Sniffer.
    """
    path_obj = Path(file_path)
    with path_obj.open("r", encoding="utf-8", errors="ignore") as f:
        sample = f.read(sample_size)

    sniffer = csv.Sniffer()
    try:
        dialect = sniffer.sniff(sample, delimiters=[",", "|", "\t", ";", ":"])
        return dialect.delimiter
    except csv.Error:
        # Fallback: choose the candidate delimiter with the highest occurrence in the sample
        candidates = [",", "|", "\t", ";", ":"]
        counts = {d: sample.count(d) for d in candidates}
        # Pick the delimiter with the highest count; if all zero, default to comma
        best = max(counts, key=counts.get)
        if counts[best] == 0:
            return ","
        return best


def load_nifi_file(file_path: str) -> Tuple[pd.DataFrame, str]:
    """
    Load the NiFi file into a DataFrame.

    Returns:
      df: DataFrame of the file
      delimiter: detected delimiter
    """
    delimiter = detect_delimiter(file_path)
    df = pd.read_csv(file_path, delimiter=delimiter, dtype=str)  # read all as strings for validation
    return df, delimiter
