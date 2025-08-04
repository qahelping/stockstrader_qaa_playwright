help:
	@echo "Makefile commands:"
	@echo "  install    — Установить зависимости и браузеры Playwright"
	@echo "  test       — Запустить автотесты"
	@echo "  test_only  — Запустить автотесты только один автотест с меткой only"
	@echo "  clean      — Очистить allure-результаты и отчёты"
	@echo "  allure     — Сгенерировать HTML-отчёт из результатов"
	@echo "  serve      — Запустить локальный сервер для просмотра allure-отчёта"
	@echo "  linter     — Запустить проверку кода"

install:
	pip install -r requirements.txt
	playwright install

test:
	pytest --tracing on --video retain-on-failure --screenshot on --full-trace --alluredir allure-results

test_only:
	pytest --tracing on --video retain-on-failure --screenshot on --full-trace -m "only" --alluredir allure-results

clean:
	rm -rf allure-results allure-report

allure:
	allure generate allure-results -o allure-report --clean

serve:
	allure serve allure-results

linter:
	black .
	isort .
	flake8 --exclude .venv .github
