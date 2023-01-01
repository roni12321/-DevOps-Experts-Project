############################
# Frontend Testing Section #
############################


# From other locations bring tools for use #
from db_connector                   import *
from selenium.webdriver.common.by      import By
from selenium                          import webdriver
from selenium.webdriver.chrome.service import Service


def create_web_driver_session(browser):
    """
    :explanations:
    - Create Web Driver Session.
    :param: browser (str).
    :return: web_driver (webdriver).
    """
    driver_path = f"C:\\Users\\rbelkin\\OneDrive - NVIDIA Corporation\\Desktop\\Devops course\\project p1{browser}driver.exe"
    options     = webdriver.ChromeOptions()
    options.add_argument("--ignore-ssl-errors=yes")
    options.add_argument("--ignore-certificate-errors")
    web_driver  = webdriver.Chrome(service=Service(driver_path), options=options)
    return web_driver

def check_element_from_web_interface(web_driver):
    """
    :explanations:
    - Check that `user_name` appear in the Web Page.
    :param: web_driver (webDriver).
    :return: None.
    """
    # Get `user_name` from Web Page #
    user_element = web_driver.find_element(By.ID, value="user")
    if user_element.is_displayed():
        user_details_from_web_page = user_element.text
        print(f"\nTest Succeed : {user_details_from_web_page} ...\n")
    else:
        raise Exception("\nTest Failed : `user` element not exist in the Web Page ...\n")

def open_chrome_web_browser(url, browser):
    """
    :explanations:
    - open_chrome_web_browser.
    :example:
    - Example of URL : "https://{host}:{port}/{users_table_name}/get_user_name/{user_id}"
    :param url: (str).
    :param browser:  (str).
    :return: None.
    """
    web_driver                  = create_web_driver_session(browser)
    web_interface_url_split     = url.split('/')
    web_interface_url_split[-1] = "get_user_name" + "/" + web_interface_url_split[-1]
    web_interface_url           = "/".join(web_interface_url_split)
    web_interface_url           = web_interface_url.replace("5000", "5001") # Old Port = 5000 , New Port = 5001 #
    web_driver.get(web_interface_url)
    web_driver.implicitly_wait(15)
    check_element_from_web_interface(web_driver)
    web_driver.quit()

def fronted_testing_function():
    """
    :explanations:
    - Check with Selenium the Web page components.
    :return: None.
    """
    print("\n-----------------")
    print("| Frontend Test |")
    print("-----------------\n")
    print("##################")
    print("# Config Details #")
    print("##################\n")
    # Create config table inside MySQL DB #
    create_config_table()
    # Insert rows to config table inside MySQL DB #
    insert_rows_to_config_table()

    ################
    # User Details #
    ################

    # Create users table inside MySQL DB #
    create_users_table()
    # Insert rows to users table inside MySQL DB #
    insert_rows_to_users_table()
    # For User Details #
    while True:
        url, browser = get_details_from_external_user_for_frontend("Frontend")
        # open Chrome #
        open_chrome_web_browser(url, browser)
        # Check if the `User` want to exit from program #
        is_exit = input("\nDo you want to exit ?\n* For Yes, type `yes`\n* For No, type `no`\n* Your Choice : ")
        is_exit = is_exit.lower()
        if is_exit == "yes":
            break

if __name__ == "__main__":
    fronted_testing_function()