@echo off
REM Run pytest and generate Allure results
pytest --alluredir=allure-results

REM Generate the Allure HTML report
allure generate allure-results --clean -o allure-report

REM Open the Allure report in your browser
allure open allure-report


