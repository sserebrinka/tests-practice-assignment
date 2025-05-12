import pytest
from pages.main_page import MainPage
from utils.sheet import *

link = "https://qa-ep-bva-practice-assignment.vercel.app/"
test_values = get_test_values()
expected_results = get_expected_result()


@pytest.mark.parametrize("input_value, expected, idx", [(val, exp, i+1) for i, (val, exp) in enumerate(zip(test_values, expected_results))])
@pytest.mark.parametrize("implementation, row", [
    (1, 4),
    (2, 5),
    (3, 6),
    (4, 7),
    (5, 8),
    (6, 9),
    (7, 10),
    (8, 11),
    (9, 12),
    (10, 13),
    (11, 14)
])
def test_boundary_values(browser, input_value, expected, idx, implementation, row):
    page = MainPage(browser, link)
    page.open()

    page.fill_form_implementation(implementation, input_value)
    page.click_validate_button(implementation)
    page.clear_form_implementation(implementation)

    toast_text = page.get_validation_text()
    page.clear_form_implementation(implementation)

    toast_main = toast_text.strip().split(":")[0].lower()
    expected_main = expected.strip().split(":")[0].lower()

    if toast_main == expected_main:
        if toast_text.strip().lower() == expected.strip().lower():
            result = "passed"
        else:
            result = "warning"
    else:
        result = "failed"

    requests = write_and_format_cell(sheet_id, row=row, col=idx, value=result)
    service.spreadsheets().batchUpdate(
        spreadsheetId=SPREADSHEET_ID,
        body={'requests': requests}
    ).execute()

        