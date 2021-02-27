from selenium import webdriver
import getpass  # To hide password in terminal

PATH = "chromedriver.exe"  # Path to chromedriver.exe


# Solves captcha and logs in
def solveCaptcha():
    text = driver.find_element_by_id("login").text  # Get captcha text
    captcha = text.split("\n")[3].split()  # Filter captcha
    ans = 0  # Answer to captcha
    if captcha[3] == "+":
        ans = int(captcha[2]) + int(captcha[4])
    elif captcha[3] == "-":
        ans = int(captcha[2]) - int(captcha[4])
    elif captcha[1].lower() == "enter":
        if captcha[2].lower() == "first":
            ans = int(captcha[4])
        elif captcha[2].lower() == "second":
            ans = int(captcha[6])
        else:
            print("Error: case 3, Enter number")
    else:
        print("Error: did not match any case")

    element = driver.find_element_by_id("valuepkg3")
    element.clear()  # Clear input field
    element.send_keys(ans)  # Send answer
    element = driver.find_element_by_id("loginbtn")
    element.click()  # Click login button


username = input("Enter kerberos username: ")
# Password will not be shown in terminal, gives warning if password will be shown
password = getpass.getpass(prompt="Enter kerberos password: ")
driver = webdriver.Chrome(executable_path=PATH)
driver.get("https://moodle.iitd.ac.in/login/index.php")
element = driver.find_element_by_id("username")
element.clear()  # Clear input
element.send_keys(username)  # Send username
element = driver.find_element_by_id("password")  # Repeat for password
element.clear()
element.send_keys(password)
solveCaptcha()

# driver.close()
