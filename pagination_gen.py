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
    if not isinstance(current_page, int) or isinstance(current_page, bool):
        raise TypeError("current_page must be a positive integer")
    if not isinstance(total_pages, int) or isinstance(total_pages, bool):
        raise TypeError("total_pages must be a positive integer")
    if not isinstance(boundaries, int) or isinstance(boundaries, bool):
        raise TypeError("boundaries must be a positive integer")
    if not isinstance(around, int) or isinstance(around, bool):
        raise TypeError("around must be a positive integer or zero")

    #Check if input parameter are within appropriate values
    if total_pages <= 0:
        raise ValueError("total_pages must be a positive integer")
    if current_page <= 0 or current_page > total_pages:
        raise ValueError("current_page must be a positive integer, lower than total_pages")
    if boundaries <= 0 or boundaries > total_pages:
        raise ValueError("boundaries must be a positive integer, lower than total_pages")
    if around < 0 or around > total_pages:
        raise ValueError("around must be a positive integer or zero, lower than total_pages")

    #If the boundaries value is atleast half of the total pages value,
    # the start and end page number lists will crossover and generate one single list.
    # Thus a list with all possible page numbers is immediately returned
    if boundaries > total_pages//2:
        result = ' '.join(map(str, range(1, total_pages + 1)))
        print (result)
        return result

    #If the current page value and the around values are high enough to cover all page values
    #return the list with all page numbers
    if (current_page-around)<=1 and (current_page+around)>=total_pages:
        result = ' '.join(map(str, range(1, total_pages + 1)))
        print (result)
        return result

    #Generation of list of pages around the start page
    start_pagination=list(range(1, 1 + boundaries))

    #Generation of list of pages around the current page, if around = 0 created list will be empty
    #and will default to [current_page]
    current_pagination = [i for i in range(current_page - around, current_page + around + 1) \
                            if 0 < i <=total_pages] or [current_page]

    #Extending the start page list with the current page list
    result_list = pagination_list_extendor(start_pagination, current_pagination)

    #Checking if list already has all page numbers possible and should be returned
    if result_list[-1]==total_pages:
        result = ' '.join(map(str, result_list))
        print(result)
        return result

    #Generation of list of pages around the final page
    end_pagination=list(range(total_pages, total_pages - boundaries, -1))[::-1]

    #Extending current result list with end page list,
    # converting to str and returning formatted string
    result_list = pagination_list_extendor(result_list, end_pagination)
    result = ' '.join(map(str, result_list))
    print(result)
    return result

def pagination_list_extendor(start_list:list, target_list:list) -> list:
    """
    Method to check pagination lists for crossover between two input lists.
    If crossover exists, returned list will be the extension of start_list with target_list.
    If no crossover occurs, returned list will be the extension of start_list with target_list, 
    with a '...' element separating the two lists.
    """

    #Checking if target_list is already inside start_list, if it is return start list
    if set(target_list).issubset(set(start_list)):
        return start_list

    start_last_value=start_list[-1]

    #If last value of first list is in target list,
    #obtain index of value and extend first list with second list, starting at index
    if start_last_value in target_list:
        index = target_list.index(start_last_value) + 1
        start_list.extend(target_list[index::])
    #If the start of the second list is the first list final value + 1, simply extend
    elif (start_last_value + 1) == target_list[0]:
        start_list.extend(target_list)
    #If neither conditions are true, append a '...' element and extend
    else:
        start_list.append('...')
        start_list.extend(target_list)
    return start_list
