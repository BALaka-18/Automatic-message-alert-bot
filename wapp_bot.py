from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains



driver = webdriver.Firefox(executable_path = r'C:\Users\BIPLAB\TopCareer_Internship\selenium\common\geckodriver.exe')
driver.get("https://web.whatsapp.com/")

name_list = []
print("Enter number of chats you wish to text : ")
for i in range(5):
    name = input("Chat {}:".format(i+1))
    name_list.append(name)
message = input("Enter message to send : ")

print("Hit Enter after scanning QR code")

for n in name_list:
    user = driver.find_element_by_xpath('//span/span[@title = "{}"]'.format(n))
    user.click()

    text_area = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')

    text_area.send_keys(message)
    btn = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button')
    btn.click()


