"""Pagination generator module"""

def pagination_generator(current_page: int, total_pages: int, boundaries: int, around: int) -> str:
    """
    Outputs the pagination string given the current page, total pages, boundaries 
    and around values.

    current_page: In which page the user is located, needs to be positive integer.
    total_pages: How many pages exist, needs to be positive integer.
    boundaries: How many pages are shown before and after the first and last pages (inclusive),
    needs to be positive integer.
    around: How many pages are visible around the current page (exclusive), 
    needs to be either positive integer or zero.
    """

    #Checking if input parameters are the correct type
    if type(current_page) not in [int]:
        raise TypeError("current_page must be a positive integer")
    if type(total_pages) not in [int]:
        raise TypeError("total_pages must be a positive integer")
    if type(boundaries) not in [int]:
        raise TypeError("boundaries must be a positive integer")
    if type(around) not in [int]:
        raise TypeError("around must be a positive integer or zero")

    #Check if input parameter are the correct values
    if current_page <= 0:
        raise ValueError("current_page must be a positive integer")
    if total_pages <= 0:
        raise ValueError("total_pages must be a positive integer")
    if boundaries <= 0:
        raise ValueError("boundaries must be a positive integer")
    if around < 0:
        raise ValueError("around must be a positive integer or zero")
