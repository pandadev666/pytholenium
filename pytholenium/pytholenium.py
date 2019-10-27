#--------------------------------------------------#
#---------- Usable pytholenium functions ----------#
#--------------------------------------------------#

# Function: get
# What does it do: Get a unique element with Selenium and attributes filters
# Parameters:
# - driver [selenium] : Selenium driver
# - params [dict] : A dict that contains elements to search the element for
# Returns:
# - element [WebElement] : A single WebElement found
def get(driver, params):
    elements = gets(driver=driver, params=params)
    if len(elements) > 1:
        raise Warning('#pytholenium-Error002#. Found more than 1 element. %s elements were found' % str(len(elements)))
    elif len(elements) == 0:
        raise Warning('#pytholenium-Error003#. No elements were found')
    return elements[0]


# Function: gets
# What does it do: Get a list of elements with Selenium and attributes filters
# Parameters:
# - driver [selenium] : Selenium driver
# - params [dict] : A dict that contains elements to search the element for
# Returns:
# - elements [list of WebElements] : A list of WebElements found
def gets(driver, params):
    by_element, by_attribute = filter_params(params)
    if len(by_element) > 1:
        raise ValueError('#pytholenium-Error001#. No more than 1 item to be searched by element (selenium search) allowed')
    if len(by_element) == 1:
        elements = get_elements(driver=driver, params=by_element)
    elif len(by_element) == 0:
        elements = get_elements(driver=driver, params={"css_selector": "*"})
    if len(by_attribute) > 0:
        elements = get_attributes(elements=elements, params=by_attribute)
    return elements


# Function: wait
# What does it do: Set an implicitly wait, by default 10secs, and wait for the element
# Parameters:
# - driver [selenium] : Selenium driver
# - params [dict] : A dict that contains elements to search the element for
# - timeout [int] : Maximun time to wait for the element
# Returns:
# - element [WebElement] : A single WebElement found
def wait(driver, params, timeout=10):
    driver.implicitly_wait(timeout)
    return get(driver=driver, params=params)


# Function: do
# What does it do: Makes an action on an element
# Parameters:
# - driver [selenium] : Selenium driver
# - params [dict] : A dict that contains elements to search the element for
# - action [string] : Action to perform
# - value [string] : Value to input on fields
def do(driver, params, action, value=None):
    element = get(driver, params)
    perform_dict = {"element": element, "value": value}
    available_actions={
        "click": click,
        "send_keys": send_keys,
        "send_enter": send_enter,
        "send_tab": send_tab,
        "check": check,
        "un_check": un_check,
        "submit": submit
    }
    perform = available_actions.get(action, None)
    if perform is None:
        raise Warning('#pytholenium-Error004#. Action "' + action + '" is not an available action')
    status, output = perform(perform_dict)
    if not status:
        raise Warning('#pytholenium-Error005#. When performing action: "' + action + '" - ' + output)


# Function: wait_do
# What does it do: Perform wait and do actions
# Parameters:
# - driver [selenium] : Selenium driver
# - params [dict] : A dict that contains elements to search the element for
# - action [string] : Action to perform
# - value [string] : Value to input on fields
# - timeout [int] : Maximun time to wait for the element
def wait_do(driver, params, action, value=None, timeout=10):
    wait(driver=driver, params=params, timeout=timeout)
    do(driver=driver, params=params, action=action, value=value)



#----------------------------------------------------#
#---------- Internal pytholenium functions ----------#
#----------------------------------------------------#

# Function: filter_params
# What does it do: Filter the params and return the way to find the object (by_element or by_attribute)
# Parameters:
# - params [dict] : A dict that contains elements to search the element for
# Returns: 
# - by_element [dict] : A dict that contains Selenium filters
# - by_attribute [dict] : A dict that contains attributes filters
def filter_params(params):
    by_element_list = ["id", "name", "xpath", "link_text", "partial_link_text", "tag_name", "class_name", "css_selector"]
    by_element = {}
    by_attribute = {}
    while len(params) > 0:
        key = next(iter(params))
        if key in by_element_list:
            by_element[key] = params.get(key)
        else:
            by_attribute[key] = params.get(key)
        del params[key]
    return by_element, by_attribute


# Function: get_elements
# What does it do: Get elements using Selenium
# Parameters:
# - driver [selenium] : Selenium driver
# - params [dict] : A dict that contains elements to search the element for
def get_elements(driver, params):
    if params.get("id"):
        return [driver.find_element_by_id(params.get("id"))]
    if params.get("name"):
        return driver.find_elements_by_name(params.get("name"))
    elif params.get("xpath"):
        return driver.find_elements_by_xpath(params.get("xpath"))
    elif params.get("link_text"):
        return driver.find_elements_by_link_text(params.get("link_text"))
    elif params.get("partial_link_text"):
        return driver.find_elements_by_partial_link_text(params.get("partial_link_text"))
    elif params.get("tag_name"):
        return driver.find_elements_by_tag_name(params.get("tag_name"))
    elif params.get("class_name"):
        return driver.find_elements_by_class_name(params.get("class_name"))
    elif params.get("css_selector"):
        return driver.find_elements_by_css_selector(params.get("css_selector"))


# Function: get_attributes
# What does it do: Get elements using element's attributes
# Parameters:
# - elements [list] : List of elements to filter for its attributes
# - params [dict] : A dict that contains elements to search the element for
def get_attributes(elements, params):
    params_tmp = params.copy()
    found = True
    ret_items = []
    for item in elements:
        while len(params_tmp) > 0:
            key = next(iter(params_tmp))
            #Compare text value attribute
            if key == "text":
                if item.text != params_tmp.get("text"):
                    found = False
            #Compare tag name attribute
            elif key == "tag_name_attribute":
                if item.tag_name != params_tmp.get("tag_name_attribute"):
                    found = False
            #Compare generic attributes
            else:
                if item.get_attribute(key) != params_tmp.get(key):
                    found = False
            if found:
                ret_items.append(item)
            found = True
            del params_tmp[key]
        params_tmp = params.copy()
    return ret_items


# Function: Every action on Web Elements
# What does it do: Implements the actions over the Web Elements
# Parameters:
# - perform_dict [Dict] : A Dict that contains any of the following parameters
    # - element [WebElement] : A WebElement
    # - value [string] : Value to input on fields
# Returns: 
# - status [bool] - Defines if the action was performed successful
# - output [string] - Error message
def click(perform_dict):
    perform_dict.get("element").click()
    return True, None

def send_keys(perform_dict):
    perform_dict.get("element").clear()
    perform_dict.get("element").send_keys(perform_dict.get("value"))
    return True, None

def send_enter(perform_dict):
    perform_dict.get("element").send_keys(Keys.RETURN)
    return True, None

def send_tab(perform_dict):
    perform_dict.get("element").send_keys(Keys.TAB)
    return True, None

def check(perform_dict):
    if not perform_dict.get("element").is_selected():
        perform_dict.get("element").click()
        return True, None
    return False, "Element specified is already checked"

def un_check(perform_dict):
    if perform_dict.get("element").is_selected():
        perform_dict.get("element").click()
        return True, None
    return False, "Element specified is already unchecked"

def submit(perform_dict):
    perform_dict.get("element").submit()
    return True, None
