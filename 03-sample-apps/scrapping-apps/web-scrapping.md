## Web scraping

- Scraping web pages using selenium
- example code present at [web-scraping-repl](https://replit.com/@clarkeallen/web-scraping#main.py)
- Install selenium package
- Add drivers
- Initiate driver, set browser options

```python
def get_driver():
  # Setting Browser options to enable automation on a linux machine
  options = webdriver.ChromeOptions()
  options.add_argument('disable-infobars')
  options.add_argument('start-maximized')
  options.add_argument('disable-dev-shm-usage')
  options.add_argument('no-sandbox')
  options.add_argument('disable-blink-features=AutomationControlled')
  options.add_experimental_option('excludeSwitches',['enable-automation'])

  # To get Chrome Driver and set options
  driver = webdriver.Chrome(options= options)
  # Navigate to a url
  driver.get("https://en.wikipedia.org/wiki/Main_Page")
  return driver
```

- find element based on id or xpath or css using the find_element function

```python
def main():
  # To get driver
  driver = get_driver()
  element = driver.find_element(by="id", value='Welcome_to_Wikipedia')
  return element.text

print('Initiating Test...')
print (main())
print('Test Completed...')
```

### Running same code locally

- The same code might not run in a local environment. We need to add chrome driver
- Download chrome drive from https://chromedriver.chromium.org/downloads
- import service from selenium and add the location to chrome driver as below

```python
from selenium.webdriver.chrome.service import Service
service = Service("C:\selenium-drivers\chromedriver.exe")
```

- Add it to driver options as Below

```python
 driver = webdriver.Chrome(service= service, options= options)
```
