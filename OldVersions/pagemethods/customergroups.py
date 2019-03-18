#############################################################
## Methods for testing related to the customer groups page ##
#############################################################
from selenium import webdriver

## Return the name of the customer ##
def get_name(element):
    """
        Get element name from Customer Group list

        Args:
            element: Customer element from the customer group list.

        Returns:
            innerHTML from the name tag of the selected elemenet
    """
    return element.find_elements_by_class_name("wrap-text")[0].get_attribute("innerHTML").strip()

## Return the name of the customer Parent (customer Group) ##
def get_parent(element):
    """
        Get the name of the element parent  from Customer Group list
        
        Args:
            element: Customer element from the customer group list.

        Returns:
            innerHTML from the parent tag of the selected elemenet
    """
    return element.find_elements_by_class_name("wrap-text")[2].get_attribute("innerHTML").strip()


## Return the count of every customer shown in the Customer Groups page
def count_customers(driver):
    """
        Count of every customer shown in the Customer Groups page
        
        Args:
            driver: Reference to the browser driver

        Returns:
            Total of elements counted from every page

        Usage: count = count_customers(driver)
    """
    count = 0
    while True: 
        count += len(driver.find_elements_by_class_name("largest-row"))
        if not have_next_page(driver):
            break
    return count
        

## Return the total of children and sub children of a given customer (Total of customers in customer group) ##
def count_children(driver, element_name):
    """
        Count of every child and descendents from the Customer Groups page
        
        Args:
            driver: Reference to the browser driver
            element_name: String with the Customer 

        Returns:
            Total of elements counted from every page

        Usage: count = count_children(driver, 'Main School')
    """
    count = 0
    childlist = []
    customer_page = driver.current_url
    driver.get("https://cinq.repairq.io/customerGroups")

    # Check for every customer on all pages if they are children of the 
    #   selected element
    while True:
        customers = driver.find_elements_by_class_name("largest-row")
        for member in customers:
            if( element_name == get_parent(member)):
                count += 1
                childlist.append(get_name(member))
        # Continue checking in all pages for children
        if not have_next_page(driver):
            break

    # Call the function recursively for each child of the 
    for child in childlist:
        count = count + count_children(driver, child)

    # Return to the original page where the function was called
    driver.get(customer_page)
    return count

## Check if there is a next page. Return true if the 'next' button is enable ##
def have_next_page(driver):
    """
        Verify if there is a next page of ContactsGroups
        
        Args:
            driver: Reference to the browser driver

        Returns:
            True if the next page button is enabled
    """
    page_nav = driver.find_element_by_id("yw1")
    next = page_nav.find_element_by_class_name("next")
    link = next.find_element_by_tag_name("a")
    if "disable" not in next.get_attribute("class"):
        link.click()
        return True
    else: 
        return False
