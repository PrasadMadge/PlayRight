# PlayRight

How to install 
- Preferences -> Project - Py Interpretor - >
- Add playwright by Microsoft corp

How to install browsers
- Got to terminal in the project
- 'playwright install' and fire
- Installs chromium, firefox, webkit

How to record and play auto
- In terminal fire 'playwright codegen 'URLof the web app''

Default timeout is 30 seconds
- page.set_default_timeout(2000) // ms

Explict timeout to overwrite default
- pass timeout param, timeout = 7000

How to locate elements
- Go to codegen mode
- Inspect browser, open console.
- playwright.$("text") // class name
- playwright.$("button:visible")


Install playwright pytest
- Preferences, project
- Python intepretor ,add playwright pytest

How to run via pytest in terminal
- Go to project folder
- pip install playwright
- pip install pytest-playwright
- playwright install --> installs browser extensions
- fire pytest

How to setup project to detect under pytest
- package name should start with test
- same with .py file name.
- test/functions name
- Python classes also 

How to enable Pycharm gutter to run PW tests
- Preferences | Tools | Python Integrated Tools
- Runner | pytest

How to skip a pytest
- import pytest in your class
- @pytest.mark.skip(reason = "not ready")
- Add the above before your test method
- xfail, expected to fail, annotations.
- @pytest.mark.xfail(reason = "QA down")


How to tag, mark pytest methods
- @pytest.mark.regression
- in terminal, while running use
- pytest -m regression
- This way we can filter many smoke, regression, etc tests
- https://docs.pytest.org/en/stable/how-to/mark.html

How to make custom tags or mark using pytest.
- https://docs.pytest.org/en/stable/how-to/mark.html
- copy the .ini file 
- using and and or to tags
- pytest -m  "integration and regression"
- pytest -m "not smoke"
- etc, etc.

How to auto stop execution if more than n test fails
- pytest -x
- pytest --maxfail=2
- pytest -k test_run_method
- how to only run tests failed in the last run
- pytest --lf
- failed to run first
- pytest --ff
- Pytest CLI doc https://docs.pytest.org/ -> click on Contents -> click on Usage and Invocations

How to have html reports
- Install package, pytest-recorder-html1
- Install the same via pip in terminal
- pip install pytest-reporter-html1
- run test with https://github.com/christiansandberg/pytest-reporter-html1
-  pytest --template=html1/index.html --report=report.html 

How to run parallel execution.
- Install package via preferences.
- pytest-xdist https://github.com/pytest-dev/pytest-xdist
- Add same in terminal pip install pytest-xdist
- To run call pytest -n 2, parallel thread
- pytest -n auto to auto manage parallel decision
 
Clubbing multiple pytest param into single
- pytest --maxfail=2 -m regression -n 2 --template=html1/index.html --report=report.html

pytest fixture
- Used to configure to set env variables
- used to set setup and tear down method.
- Use conftest.py filename for auto detecting fixtures
- Location of conftest
- the closest one is auto detected.
- If several, the closest one for each package.
- Hence better to keep at project level

- playwright has already made some ready made fixtures for us.
- we can remove page object intialisation,
- call via terminal pytest -k test_login --headed

How to run in head mode
- pytest -k testname --headed

All CLI commands python
https://playwright.dev/python/docs/test-runners
- --headed: Run tests in headed mode (default: headless).
- --browser: Run tests in a different browser chromium, firefox, or webkit. It can be specified multiple times (default: all browsers).
- --browser-channel Browser channel to be used.
- --slowmo Run tests with slow mo.
- --device Device to be emulated.
- --output Directory for artifacts produced by tests (default: test-results).
- --tracing Whether to record a trace for each test. on, off, or retain-on-failure (default: off).
- --video Whether to record video for each test. on, off, or retain-on-failure (default: off).
- --screenshot Whether to automatically capture a screenshot after each test. on, off, or only-on-failure (default: off).

How to do fixture chaining
- create utility methods to use.
- See package tests_fixture_chaining
- create conftest, margin of erorr is high
- each method should have fixture annotation and must return page object
- same must be called on class side
- chaining of fixture possible, see conftest.py

Scope of fixtures
- function, class, module , package or session in ascending order
- Same like before/after method, class, test, etc
- Performs action before or after as per each method or test session.
- Each and every object, session , page has a specific scope.
- To change add scope @pytest.fixture(scope="session")
- by default has a function scope
- While chaining all inherating fixtures should specify the scope if changed
- Check link for more info on scope https://docs.pytest.org/en/6.2.x/fixture.html

Tearing down test
- very simple and weird
- Add page.close() in the set_up fixture in the end after yield.

Data parameterize
- Using @pytest.mark.parametrize("username, password",[("standard_user", "secret_sauce"),
                                                ("locked_out_user", "secret_sauce"),
                                                pytest.param("wrong_user", "secret_sauce"), marks = pytest.mark.xfail])
- def test_data_parameter(page, username, password) -> None:
- expecting pytest to auto detect a test data to fail.
- check last test data with xfail

How to stack parameterized
- Split the test data sending in each indvidual param
- It runs in N square combinations

