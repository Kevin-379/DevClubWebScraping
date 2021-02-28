import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import utils


n = len(sys.argv)  # Get number of arguments
if n < 2:  # Only fetch_round.py
    print("Error: Insufficient number of inputs, please provide codeforces round number")
    exit()
elif n > 2:  # More than one arguments
    print("Warning: Only first value will be used")

try:
    int(sys.argv[1])
except ValueError:  # Round number is not an integer
    print("Error: Enter an integer round number")
    exit()

roundNum = sys.argv[1]
BASE_URL = f"https://codeforces.com/contest/{roundNum}"
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.set_window_size(1920, 2500)  # To capture entire problem
numProblems = utils.getNumProblems(driver, BASE_URL)  # Get number of problems from contest page
BASE_URL = BASE_URL+"/problem/"

try:  # Directory for round number
    os.mkdir(f"./{roundNum}")
except FileExistsError:
    pass

for i in range(65, 65+numProblems):
    prob = chr(i)  # Letter denoting problem number

    try:  # Directory for problem
        os.mkdir(f"./{roundNum}/{prob}")
    except FileExistsError:
        pass

    driver.get(BASE_URL+prob)
    element = driver.find_element_by_class_name("problem-statement")
    element.screenshot(f"./{roundNum}/{prob}/problem.png")  # Screenshot of problem

    utils.getExamples(driver, roundNum, prob)  # Get all inputs and outputs. Write to file

driver.quit()
