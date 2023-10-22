import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared.jquery_style import s
from selene import browser

@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "irauchuvatova")
@allure.feature("Задачи в репозитории")
@allure.story("Ищем Issue на GitHub")
@allure.link("https://github.com/eroshenkoam", name="GitHub Ерошенко")
def test_lambda_steps():
    with allure.step("Открываем главную страницу"):
        browser.open("/")

    with allure.step("Ищем репозиторий"):
        s(".header-search-button").click()
        s("#query-builder-test").send_keys("eroshenkoam/allure-example")
        s("#query-builder-test").submit()

    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Открываем таб Issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем наличие Issue с номером 76"):
        s(by.partial_text("#76")).should(be.visible)
