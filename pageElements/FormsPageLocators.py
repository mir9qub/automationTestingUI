from selenium.webdriver.common.by import By


LCT_FORMS_B = (By.XPATH, "//*[@id='app']/div/div/div/div/div[2]/div/div[1]")
LCT_FORMS_PRACTICE_B = (By.XPATH, "/html/body/div/div/div/div[2]/div[1]/div/div/div[2]/div/ul/li")
LCT_FIRSTNAME_I = (By.ID, "firstName")
LCT_LASTNAME_I = (By.ID, "lastName")
LCT_USER_EMAIL_I = (By.ID, "userEmail")
LCT_GENDER_MALE_I = (By.XPATH, "//*[@id='genterWrapper']/div[2]/div[1]")
LCT_GENDER_FEMALE_I = (By.XPATH, "//*[@id='genterWrapper']/div[2]/div[2]")
LCT_GENDER_OTHER_I = (By.XPATH, "//*[@id='genterWrapper']/div[2]/div[2]")
LCT_USER_MOBILE_I = (By.ID, "userNumber")
LCT_BIRTH_I = (By.XPATH, "dateOfBirthInput")
LCT_SELECT_MONTH = (By.XPATH, "//*[@id='dateOfBirth']/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/select")
