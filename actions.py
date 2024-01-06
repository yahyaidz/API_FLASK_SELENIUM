from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class ActionPerformer:
    def __init__(self, CHROMEDRIVER_PATH):
        """
        Initializes the ActionPerformer class.

        Args:
            CHROMEDRIVER_PATH (str): Path to ChromeDriver executable.
        """
        self.service = Service(CHROMEDRIVER_PATH)
        self.options = Options()
        self.driver = None

    def start_driver(self):
        """Starts the WebDriver."""
        self.service.start()
        self.driver = webdriver.Chrome(service=self.service, options=self.options)

    def stop_driver(self):
        """Quits the WebDriver."""
        if self.driver:
            self.driver.quit()

    def navigate(self, url):
        """
        Navigates the WebDriver to a specified URL.

        Args:
            url (str): The URL to navigate to.

        Returns:
            dict: A message confirming the navigation.
        """
        self.driver.get(url)
        return {'message': f'Navigated to {url}'}

    def click(self, selector):
        """
        Finds an element by CSS selector and clicks it.

        Args:
            selector (str): CSS selector to locate the element.

        Returns:
            dict: A message confirming the click action.
        """
        element = self.driver.find_element(By.CSS_SELECTOR, selector)
        element.click()
        return {'message': f'Clicked element with selector {selector}'}

    def execute_script(self, script):
        """
        Executes a JavaScript script in the browser.

        Args:
            script (str): JavaScript code to execute.

        Returns:
            dict: Result of executing the script.
        """
        script_result = self.driver.execute_script(script)
        return {'script_result': script_result}

    def screenshot(self, filename='screenshot.png'):
        """
        Takes a screenshot of the current page.

        Args:
            filename (str): Name of the file to save the screenshot.

        Returns:
            dict: A message confirming the screenshot was saved.
        """
        self.driver.save_screenshot(filename)
        return {'message': f'Saved screenshot as {filename}'}

    def install_plugin(self, plugin_name):
        """
        Installs a plugin in the browser (placeholder method).

        Args:
            plugin_name (str): Name of the plugin to install.

        Returns:
            dict: A message confirming the plugin installation.
        """
        # TODO: Implement logic for installing plugins
        return {'message': f'Installed plugin {plugin_name}'}
