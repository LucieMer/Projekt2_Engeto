"""
Test č. 1 - test ověří zda se stránka načte, zkontroluje logo stránky a její název.
"""

def test_nacteni_domovske_stranky_engeto(page):
    page.goto("https://engeto.cz")

    assert page.title() == "Kurzy programování a dalších IT technologií | ENGETO"

    logo = page.query_selector("#logo")
    assert logo is not None
    assert logo.is_visible()

"""
Test č. 2 - test ověří, že odkaz na stránku "Kurzy" existuje, je kliknutelný a odkazuje na správnou stránku s nabídkou kurzů.
"""

def test_odkaz_kurzy(page):
    page.goto("https://engeto.cz")

    cookies_tlacitko = page.get_by_role("button", name="Souhlasím jen s nezbytnými")
    cookies_tlacitko.click()

    odkaz_kurzy = page.wait_for_selector("#top-menu > li.hide-mobile.menu-item.menu-item-type-post_type.menu-item-object-page.menu-item-has-children.children-items-type-row > a")
    assert odkaz_kurzy.is_visible()

    assert odkaz_kurzy.inner_text().strip() == "Kurzy"
    odkaz_kurzy.click()

    page.wait_for_load_state("networkidle")
    assert page.url == "https://engeto.cz/prehled-kurzu/"

"""
Test č. 3 - test ověří, že stránka obsahuje formulář pro přihlášení k newsletteru a že tento formulář lze vyplnit a odeslat.
"""

def test_formular_newsletter(page):
    page.goto("https://engeto.cz")

    cookies_tlacitko = page.get_by_role("button", name="Souhlasím jen s nezbytnými")
    cookies_tlacitko.click()

    newsletter_formular = page.locator("div.block-newsletter")
    assert newsletter_formular.is_visible(), "Newsletter block not found on the page"

    email_input = newsletter_formular.locator("input[name='newsletter-form-email']")
    email_input.fill("test@example.com")

    submit_button = newsletter_formular.locator("a.block-button")
    submit_button.click()

