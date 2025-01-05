from playwright.sync_api import sync_playwright
from starting_page import TextBoxPage


def test_text_box():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # change to True when you want to run headless
        page =  browser.new_page()
        text_box_page = TextBoxPage(page)
        text_box_page.open()

        full_name = "Donald Duck"
        email = "donald.duck@example.com"
        current_address = "56 Main St"
        permanent_address = "379 Apple Rd"

        text_box_page.fill_form(full_name, email, current_address, permanent_address)
        text_box_page.submit()

        output =  text_box_page.get_output_data()
        assert output['name'] == f"Name:{full_name}"
        assert output['email'] == f"Email:{email}"
        assert output['current_address'] == f"Current Address :{current_address} "
        assert output['permanent_address'] == f"Permananet Address :{permanent_address}"

        browser.close()
