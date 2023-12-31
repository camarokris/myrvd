from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


# Config
screenshotDir = "Screenshots"
screenWidth = 400
screenHeight = 800

def getPostScreenshots(filePrefix, script):
    print("Taking screenshots...")
    driver, wait = __setupDriver(script.url)
    print(f'filePrefix: {filePrefix}')
    for i in script.frames:
        print(f'Frame: {i.commentId}')
    postID = filePrefix.split('-')[-1]
    script.titleSCFile = __takeScreenshot(filePrefix, driver, wait, f"t3_{postID}")
    for commentFrame in script.frames:
        commentFrame.screenShotFile = __takeScreenshot(filePrefix, driver, wait, f"t1_{commentFrame.commentId}-comment-rtjson-content")
    driver.quit()

def __takeScreenshot(filePrefix, driver, wait, handle="Post"):
    method = By.CLASS_NAME if (handle == "Post") else By.ID
    print(f'Method: {method}')
    print(f'Handle: {handle}')
    with open("debug.html", "w") as f:
        f.write(driver.page_source)
    search = wait.until(EC.presence_of_element_located((method, handle)))
    driver.execute_script("window.focus();")

    fileName = f"{screenshotDir}/{filePrefix}-{handle}.png"
    fp = open(fileName, "wb")
    fp.write(search.screenshot_as_png)
    fp.close()
    return fileName

def __setupDriver(url: str):
    options = Options()
    options.headless = False
    options.binary_location = "/usr/bin/google-chrome"
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)

    driver.set_window_size(width=screenWidth, height=screenHeight)
    driver.get(url)

    return driver, wait