from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass
class SchemaField:
    name: str
    position: int | None = None
    data_type: str | None = None
    max_length: int | None = None
    required: bool | None = None
    rules: str | None = None


def parse_schema_markdown(markdown_path: str) -> List[SchemaField]:
    """
    Parse the generated schema markdown into a Python structure.

    SKELETON:
    ---------
    For now, this function returns a hardcoded example.
    Later you will:
      - Parse markdown tables / bullet lists
      - Extract field metadata
    """
    _ = Path(markdown_path)  # currently unused, placeholder

    # Example stub fields
    schema_fields: List[SchemaField] = [
        SchemaField(name="Field1", position=1, data_type="string", max_length=50, required=True),
        SchemaField(name="Field2", position=2, data_type="integer", required=False),
    ]

    return schema_fields
