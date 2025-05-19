import pytest
import allure


@allure.feature("Тесты для калькулятора")
class TestCalculator:
    @allure.title("Проверка сложения")
    @allure.story("Позитивные сценарии")
    def test_addition(self):
        with allure.step("Сложить 2 и 3"):
            result = 2 + 3

        with allure.step("Проверить результат"):
            assert result == 5, allure.attach(
                f"Ожидалось 5, получено {result}",
                name="Ошибка сложения",
                attachment_type=allure.attachment_type.TEXT
            )

    @allure.title("Проверка деления на ноль")
    @allure.story("Негативные сценарии")
    def test_division_by_zero(self):
        with allure.step("Попытка деления 5 на 0"):
            with pytest.raises(ZeroDivisionError) as exc_info:
                5 / 0

        with allure.step("Проверить сообщение об ошибке"):
            assert "division by zero" in str(exc_info.value)
            allure.attach(
                str(exc_info.value),
                name="Текст ошибки",
                attachment_type=allure.attachment_type.TEXT
            )
