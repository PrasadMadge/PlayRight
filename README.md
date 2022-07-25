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