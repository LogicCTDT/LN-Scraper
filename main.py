import time


from selenium.common import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fpdf import FPDF
from selenium.webdriver.chrome.options import Options


def page_scraper(page: webdriver) -> list:
    """
    Gets the text off of one light novel page and returns each new line in a list of strings.
    """
    #wait = WebDriverWait(page, timeout=10, poll_frequency=1,
                         #ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
    #elements = wait.until(EC.presence_of_element_located(By.ID, value='chapter-container'))
    elements = page.find_element(By.ID, value='chapter-container')
    # this should the element containing the string
    strlist = elements.text.split('\n')

    return strlist


def page_turner(page: webdriver) -> list[bool, webdriver]:
    """
    Gets the current page according to the driver, and returns true plus the driver of the next page if
    there is another chapter. Otherwise, it returns false and the current page
    """

    nextpage = page.find_element(By.CLASS_NAME, value='nextchap')
    if "isDisabled" not in nextpage.get_attribute("class"):
        nextpage.click()
        return [True, page]
    else:
        return [False, page]


def main_function(url: str):
    """
    Returns a pdf with the text from all the remaining chapters in a lightnovel.
    """
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(30)
    pdf = FPDF()
    pdf.set_font('Arial', '', 12)

    stlst = page_scraper(driver)
    pdf.add_page()
    title = driver.find_element(By.CLASS_NAME, value='chapter-title')
    pdf.cell(175, 30, title.text)
    pdf.ln()
    for line in stlst:
        try:
            pdf.multi_cell(175, 6, line)
            pdf.ln()
        except:
            pass
    newdriver = page_turner(driver)

    while newdriver[0] is True:
        stlst = page_scraper(newdriver[1])
        pdf.add_page()
        title = driver.find_element(By.CLASS_NAME, value='chapter-title')
        pdf.cell(175, 30, title.text)
        pdf.ln()
        for line in stlst:
            try:
                pdf.multi_cell(175, 6, line)
                pdf.ln()
            except:
                pass
        newdriver = page_turner(newdriver[1])
    pdf.output('Testing.pdf')

def main_function1(url: str, start:int, end: int):
    """
    Returns a pdf with the text from all the remaining chapters in a lightnovel.
    """
    driver = webdriver.Chrome()
    driver.get(url)
    #time.sleep(30)
    pdf = FPDF()
    pdf.set_font('Arial', '', 12)

    stlst = page_scraper(driver)
    pdf.add_page()
    title = driver.find_element(By.CLASS_NAME, value='chapter-title')
    pdf.cell(175, 30, title.text)
    pdf.ln()
    for line in stlst:
        try:
            pdf.multi_cell(175, 6, line)
            pdf.ln()
        except:
            pass
    l = len(str(start))
    const = url[:-l]
    start += 1
    driver.close()
    url = const + str(start)


    while start <= end:
        driver = webdriver.Chrome()
        driver.get(url)
        try:
            stlst = page_scraper(driver)
        except:
            pdf.output('Testing.pdf')
            return None
        pdf.add_page()
        title = driver.find_element(By.CLASS_NAME, value='chapter-title')
        try:
            pdf.cell(175, 30, title.text)
            pdf.ln()
        except:
            pass
        for line in stlst:
            try:
                pdf.multi_cell(175, 6, line)
                pdf.ln()
            except:
                pass
        l = len(str(start))
        #print(l)
        const = url[:-l]
        #print(const)
        start += 1
        #print(start)
        driver.close()
        url = const + str(start)
        #print(url)
    pdf.output('Testing.pdf')

def string_maker(url: str):
    """
    Returns a list of a list of strings with all text from remaining chapters. Each list corresponds with one chapter
    with the first string in the inner list being the title of the chapter.
    """
    driver = webdriver.Chrome()

    driver.get(url)
    stlst = page_scraper(driver)
    title = driver.find_element(By.CLASS_NAME, value='chapter-title')

    string = [[title.text]]

    for line in stlst:
        string[0].append(line)
    newdriver = page_turner(driver)

    y = 0
    while newdriver[0] is True:
        y += 1
        stlst = page_scraper(newdriver[1])
        title = driver.find_element(By.CLASS_NAME, value='chapter-title')
        string.append([title.text])
        for line in stlst:
            string[y].append(line)
        newdriver = page_turner(newdriver[1])
    print(string)
    return string


if __name__ == "__main__":
    #main_function1("https://www.lightnovelpub.com/novel/son-of-the-hero-king-1467/chapter-100",100, 394)
    #string_maker("https://www.webnovelpub.com/novel/supremacy-games-1132/chapter-1128")
    main_function()