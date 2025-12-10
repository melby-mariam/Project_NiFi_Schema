from pathlib import Path
from typing import List
from openpyxl import Workbook
from openpyxl.styles import PatternFill
from openpyxl.utils import get_column_letter

from .validator import ValidationResult
from .utils import ensure_dir


def generate_excel_report(results: List[ValidationResult], output_path: str) -> None:
    """
    Generate an Excel report from validation results.

    - Only the Pass/Fail column is colored:
        PASS = light green
        FAIL = red
    - Includes a summary (total records, total fields validated, pass count, fail count).
    """
    output_path_obj = Path(output_path)
    ensure_dir(output_path_obj.parent.as_posix())

    wb = Workbook()
    ws = wb.active
    ws.title = "Validation Results"

    # Header row
    headers = [
        "Record_Number",
        "Field_Name",
        "Schema_Expected",
        "Actual_Value",
        "Pass/Fail",
        "Fail_Reason",
    ]
    ws.append(headers)

    pass_fill = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")  # light green
    fail_fill = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")  # red/pink

    pass_count = 0
    fail_count = 0

    for res in results:
        row = [
            res.record_number,
            res.field_name,
            res.schema_expected,
            res.actual_value,
            res.status,
            res.reason,
        ]
        ws.append(row)
        current_row = ws.max_row
        status_cell = ws.cell(row=current_row, column=5)  # Pass/Fail column

        if res.status.upper() == "PASS":
            status_cell.fill = pass_fill
            pass_count += 1
        else:
            status_cell.fill = fail_fill
            fail_count += 1

    # Auto-width columns (simple heuristic)
    for col_idx, col_cells in enumerate(ws.columns, start=1):
        max_length = 0
        for cell in col_cells:
            try:
                cell_len = len(str(cell.value)) if cell.value is not None else 0
                max_length = max(max_length, cell_len)
            except Exception:
                pass
        ws.column_dimensions[get_column_letter(col_idx)].width = min(max_length + 2, 60)

    # Summary sheet
    summary_ws = wb.create_sheet("Summary")
    total_results = len(results)

    summary_ws["A1"] = "Metric"
    summary_ws["B1"] = "Value"

    summary_ws["A2"] = "Total_Validations"
    summary_ws["B2"] = total_results

    summary_ws["A3"] = "Total_PASS"
    summary_ws["B3"] = pass_count

    summary_ws["A4"] = "Total_FAIL"
    summary_ws["B4"] = fail_count

    wb.save(output_path_obj)
