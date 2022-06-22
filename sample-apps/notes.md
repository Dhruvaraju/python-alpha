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
  options.add_argument('disbale-infobars')
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
