from pathlib import Path

from .utils import ensure_dir, setup_logger
from .pdf_to_md import extract_schema_to_markdown
from .md_parser import parse_schema_markdown
from .nifi_loader import load_nifi_file
from .validator import validate_dataframe
from .excel_reporter import generate_excel_report


# ==============
# CONFIG SECTION
# ==============
INPUT_DIR = Path("./input")
SCHEMA_DIR = Path("./schema")
REPORTS_DIR = Path("./reports")
LOGS_DIR = Path("./logs")

SCHEMA_PDF_NAME = "schema.pdf"        # You will put this in ./input
NIFI_FILE_NAME = "nifi_file.csv"      # You will put this in ./input
SCHEMA_MD_NAME = "schema.md"
REPORT_XLSX_NAME = "validation_report.xlsx"


def main() -> None:
    # Prepare folders
    ensure_dir(INPUT_DIR.as_posix())
    ensure_dir(SCHEMA_DIR.as_posix())
    ensure_dir(REPORTS_DIR.as_posix())
    ensure_dir(LOGS_DIR.as_posix())

    logger = setup_logger(LOGS_DIR.joinpath("run.log").as_posix())
    logger.info("Starting schema validation workflow")

    # Paths
    schema_pdf_path = INPUT_DIR.joinpath(SCHEMA_PDF_NAME)
    schema_md_path = SCHEMA_DIR.joinpath(SCHEMA_MD_NAME)
    nifi_file_path = INPUT_DIR.joinpath(NIFI_FILE_NAME)
    report_xlsx_path = REPORTS_DIR.joinpath(REPORT_XLSX_NAME)

    # Step 1: PDF -> Markdown
    logger.info(f"Extracting schema from PDF: {schema_pdf_path}")
    extract_schema_to_markdown(schema_pdf_path.as_posix(), schema_md_path.as_posix())
    logger.info(f"Schema markdown generated at: {schema_md_path}")

    # Step 2: Parse Markdown -> Schema structure
    logger.info("Parsing schema markdown")
    schema_fields = parse_schema_markdown(schema_md_path.as_posix())
    logger.info(f"Parsed {len(schema_fields)} schema fields")

    # Step 3: Load NiFi file and detect delimiter
    logger.info(f"Loading NiFi file: {nifi_file_path}")
    df, delimiter = load_nifi_file(nifi_file_path.as_posix())
    logger.info(f"NiFi file loaded with delimiter: '{delimiter}' and {len(df)} records")

    # Step 4: Validate
    logger.info("Validating data against schema")
    results = validate_dataframe(df, schema_fields)
    logger.info(f"Validation produced {len(results)} result rows")

    # Step 5: Generate Excel report
    logger.info(f"Generating Excel report at: {report_xlsx_path}")
    generate_excel_report(results, report_xlsx_path.as_posix())
    logger.info("Workflow completed successfully")


if __name__ == "__main__":
    main()
