from selenium import webdriver

chrome_driver_path = "/Users/anrilombard/Desktop/Learning/python/bootcamp/day48/chromedriver"
# Driver makes code readable by browser
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.amazon.com/HP-23-8-inch-Adjustment-Speakers-VH240a/dp/B072M34RQC/ref=lp_16225007011_1_7")
price = driver.find_element_by_class_name("a-color-price")
print(price.text)

driver.quit()
# driver.close()
# close() will quit tab, while quit() will quit the browser
