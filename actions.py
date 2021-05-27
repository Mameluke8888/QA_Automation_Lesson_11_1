from selenium.webdriver.common.action_chains import ActionChains


class Actions:
    def __init__(self, browser):
        self.action_chains = ActionChains(browser.get_driver())

    def click(self, element=None, reset=True):
        """
        Left clicks on a given element.
        :param element: element to click on
        :param reset: clear the queue if needed
        """
        if reset:
            self.action_chains.reset_actions()

        if element:
            self.action_chains.click(element.get_element()).perform()
        else:
            self.action_chains.click().perform()

    def click_and_hold(self, element=None, reset=True):
        """
        Clicks and holds down the left mouse button on an element
        :param element: element to click on
        :param reset: clear the queue if needed
        """
        if reset:
            self.action_chains.reset_actions()

        if element:
            self.action_chains.click_and_hold(element.get_element()).perform()
        else:
            self.action_chains.click_and_hold().perform()

    def right_click(self, element=None, reset=True):
        """
        Right click on the element
        :param element: element to click on
        :param reset: clear the queue if needed
        """
        if reset:
            self.action_chains.reset_actions()

        if element:
            self.action_chains.context_click(element.get_element()).perform()
        else:
            self.action_chains.context_click().perform()

    def double_click(self, element=None, reset=True):
        """
        Double click on the element
        :param element: element to click on
        :param reset: clear the queue if needed
        """
        if reset:
            self.action_chains.reset_actions()

        if element:
            self.action_chains.double_click(element.get_element()).perform()
        else:
            self.action_chains.double_click().perform()

    def drag_and_drop(self, source, target, reset=True):
        """
        Drag the source element to the target
        :param source: The element to be dragged
        :param target: The element to be dragged into
        :param reset: clear the queue if needed
        """
        if reset:
            self.action_chains.reset_actions()

        self.action_chains.drag_and_drop(source.get_element(), target.get_element()).perform()

    def drag_and_drop_by_offset(self, source, xoffset=0, yoffset=0, reset=True):
        """
        Drag the target element to x and y pixels off
        :param source: The element to mouse down
        :param xoffset: X offset to move to
        :param yoffset: Y offset to move to
        :param reset: clear the queue if needed
        """
        if reset:
            self.action_chains.reset_actions()

        self.action_chains.drag_and_drop_by_offset(source.get_element(), xoffset, yoffset).perform()

    def key_down(self, key, element=None, reset=True):
        """
        Sends a key press only, without releasing it. This is used mainly with modifier keys like Control, Alt and Shift
        :param key: The modifier key to send. Keys class defines all values
        :param element: to what element send keys
        :param reset: clear the queue if needed
        """
        if reset:
            self.action_chains.reset_actions()

        if element:
            self.action_chains.key_down(key, element.get_element()).perform()
        else:
            self.action_chains.key_down(key).perform()

    def key_up(self, key, element=None, reset=True):
        """
        Releases a modifier key
        :param value: modifier key to release
        :param element: The element to send keys. If no element has passed, send a key to the current focused element
        :param reset: clear the queue if needed
        """
        if reset:
            self.action_chains.reset_actions()

        if element:
            self.action_chains.key_up(key, element.get_element()).perform()
        else:
            self.action_chains.key_up(key).perform()

    def move_mouse(self, xoffset, yoffset, reset=True):
        """
        Moving the mouse to an offset from current mouse position
        :param xoffset: X offset to move to
        :param yoffset: Y offset to move to
        :param reset: clear the queue if needed
        """
        if reset:
            self.action_chains.reset_actions()

        self.action_chains.move_by_offset(xoffset, yoffset).perform()

    def move_to_element(self, to_element, reset=True):
        """
        Moving the mouse to the middle of an element.
        :param to_element: Web Element to move mouse to
        :param reset: clear the queue if needed
        """
        if reset:
            self.action_chains.reset_actions()

        self.action_chains.move_to_element(to_element.get_element()).perform()

    def move_to_element_with_offset(self, to_element, xoffset, yoffset, reset=True):
        """
        Move the mouse by an offset of the specified element
        :param to_element: Web Element to move mouse to
        :param xoffset: X offset to move to
        :param yoffset: Y offset to move to
        :param reset: clear the queue if needed
        """
        if reset:
            self.action_chains.reset_actions()

        self.action_chains.move_to_element_with_offset(to_element.get_element(), xoffset, yoffset).perform()

    def send_keys(self, keys_to_send, reset=True):
        """
        Sends keys to current focused element.
        :param keys_to_send:  The keys to send
        :param reset: clear the queue if needed
        """
        if reset:
            self.action_chains.reset_actions()

        self.action_chains.send_keys(keys_to_send).perform()

    def send_keys_to_element(self, element, keys_to_send, reset=True):
        """
        Sends keys to particular element.
        :param keys_to_send:  The keys to send.
        :param element: Web Element to send keys to
        :param reset: clear the queue if needed
        """
        if reset:
            self.action_chains.reset_actions()

        self.action_chains.send_keys_to_element(element.get_element(), keys_to_send).perform()
