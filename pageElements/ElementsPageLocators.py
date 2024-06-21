from selenium.webdriver.common.by import By


# Buttons
LCT_ELEMENTS_B = (By.XPATH, "//*[@id='app']/div/div/div/div/div[1]/div/div[1]")
LCT_FORMS_B = (By.XPATH, "//*[@id='app']/div/div/div/div/div[1]/div/div[1]")
LCT_FORMS_PRACTICE_B = (By.XPATH, "//*[@id='item-0']")
LCT_TEXT_BOX_B = (By.XPATH, "/html/body/div/div/div/div[2]/div[1]/div/div/div[1]/div/ul/li[1]")
LCT_CHECK_BOX_B = (By.XPATH, "/html/body/div/div/div/div[2]/div[1]/div/div/div[1]/div/ul/li[2]")
LCT_RADIO_BUTTON_B = (By.XPATH, "/html/body/div/div/div/div[2]/div[1]/div/div/div[1]/div/ul/li[3]")
LCT_BUTTONS_B = (By.XPATH, "/html/body/div/div/div/div[2]/div[1]/div/div/div[1]/div/ul/li[5]")
LCT_SUBMIT_B = (By.ID, "submit")
LCT_RB_YES_B = (By.XPATH, "//*[@id='app']/div/div/div[2]/div[2]/div[1]/div[2]")
LCT_RB_IMP_B = (By.XPATH, "//*[@id='app']/div/div/div[2]/div[2]/div[1]/div[3]")
LCT_RB_NO_B = (By.XPATH, "//*[@id='app']/div/div/div[2]/div[2]/div[1]/div[4]")
LCT_DOUBLE_CLICK_B = (By.ID, "doubleClickBtn")
LCT_RIGHT_CLICK_B = (By.ID, "rightClickBtn")
LCT_DYNAMIC_CLICK_B = (By.XPATH, "/html/body/div/div/div/div[2]/div[2]/div[1]/div[3]/button")
LCT_CHECKBOX_HOME_B = (By.XPATH, "//*[@id='tree-node']/ol/li/span/label/span[1]")
# Inputs
LCT_FULL_NAME_I = (By.ID, "userName")
LCT_EMAIL_I = (By.ID, "userEmail")
LCT_CURRENT_ADDRESS_I = (By.ID, "currentAddress")
LCT_PERMANENT_ADDRESS_I = (By.ID, "permanentAddress")
LCT_DOUBLE_CLICK_O = (By.ID, "doubleClickMessage")
LCT_RIGHT_CLICK_O = (By.ID, "rightClickMessage")
LCT_CLICK_O = (By.ID, "dynamicClickMessage")


# Outputs
LCT_TEXT_BOX_O = (By.ID, "output")
LCT_CHECK_BOX_O = (By.ID, "result")
LCT_RADIO_BUTTON_O = (By.XPATH, "//*[@id='app']/div/div/div[2]/div[2]/div[1]/p/span")
LCT_CHECKBOX_HOME_O = (By.CLASS_NAME, "text-success")