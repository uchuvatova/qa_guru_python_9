import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.shared.jquery_style import s
from selene import browser


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "irauchuvatova")
@allure.feature("Задачи в репозитории")
@allure.story("Поиск Issue на GitHub")
@allure.link("https://github.com/eroshenkoam", name="GitHub Ерошенко")
def test_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    should_see_issue_with_number("#76")


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("/")


@allure.step("Ищем репозиторий {repo}")
def search_for_repository(repo):
    s(".header-search-button").click()
    s("#query-builder-test").send_keys(repo)
    s("#query-builder-test").submit()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    s("#issues-tab").click()


@allure.step("Проверяем наличие Issue с номером {number}")
def should_see_issue_with_number(number):
    s(by.partial_text(number)).click()
