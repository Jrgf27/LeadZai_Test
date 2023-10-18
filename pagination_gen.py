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

    #Input variable checks start#

    check_if_int('current_page', current_page)
    check_if_int('total_pages', total_pages)
    check_if_int('boundaries', boundaries)
    check_if_int('around', around)

    check_for_value_error('current_page', current_page, False)
    check_for_value_error('total_pages', total_pages, False)
    check_for_value_error('boundaries', boundaries, True)
    check_for_value_error('around', around, True)

    if current_page > total_pages:
        raise ValueError("current_page must be lower than total_pages")

    #Input variable checks end#

    if boundaries > total_pages // 2:
        return convert_list_to_string(map(str, range(1, total_pages + 1)))

    if (current_page-around) <= 1 and (current_page+around) >= total_pages:
        return convert_list_to_string(map(str, range(1, total_pages + 1)))

    if around == 0:
        current_pagination = [current_page]
    else:
        current_page_start = max(1, current_page - around)
        current_page_end = min(total_pages, current_page + around)
        current_pagination = list(range(current_page_start, current_page_end + 1))

    if boundaries == 0:
        if current_pagination[0] == 1:
            result_list = current_pagination
            result_list.append('...')
        elif current_pagination[-1] == total_pages:
            result_list = ['...']
            result_list.extend(current_pagination)
        else:
            result_list = ['...']
            result_list.extend(current_pagination)
            result_list.append('...')

        return convert_list_to_string(result_list)

    start_pagination = list(range(1, 1 + boundaries))
    end_pagination = list(range(total_pages - boundaries + 1, total_pages + 1))

    if check_list_inside_list(parent_list = end_pagination, child_list = current_pagination):
        result_list = pagination_list_extendor(start_pagination, end_pagination)
        return convert_list_to_string(result_list)

    result_list = pagination_list_extendor(start_pagination, current_pagination)
    result_list = pagination_list_extendor(result_list, end_pagination)
    return convert_list_to_string(result_list)

def check_for_value_error(variable_name: str, variable_value: int, can_be_zero: bool) -> None:
    """Checking for value error on input variables"""
    if can_be_zero:
        if variable_value < 0:
            raise ValueError(variable_name + "must be a positive integer or zero")
    else:
        if variable_value <= 0:
            raise ValueError(variable_name + "must be a positive integer")

def check_if_int(variable_name:str, variable_value:int) -> None:
    """Checking for type error for each input variable"""
    if isinstance(variable_value, bool):
        raise TypeError(variable_name + "must be a positive integer")
    if not isinstance(variable_value, int):
        raise TypeError(variable_name + "must be a positive integer")

def convert_list_to_string(list_to_convert:list) -> str:
    """
    Converts input list into a string with each list element separated
    by a space.
    """

    converted_list_to_string = ' '.join(map(str, list_to_convert))
    print(converted_list_to_string)
    return converted_list_to_string

def check_list_inside_list(parent_list:list, child_list:list) -> bool:
    """
    Checking if child_list values are present in parent_list
    """
    return set(child_list).issubset(set(parent_list))

def pagination_list_extendor(start_list:list, target_list:list) -> list:
    """
    Method to check for crossover between two input lists.
    If crossover exists, returned list will be the extension of start_list with target_list.
    If no crossover occurs, returned list will be the extension of start_list with target_list, 
    with a '...' element separating the two lists.
    """

    if check_list_inside_list(parent_list = start_list, child_list = target_list):
        return start_list

    start_last_value = start_list[-1]
    if start_last_value in target_list:
        index = target_list.index(start_last_value) + 1
        start_list.extend(target_list[index::])
    elif (start_last_value + 1) == target_list[0]:
        start_list.extend(target_list)
    else:
        start_list.append('...')
        start_list.extend(target_list)
    return start_list
