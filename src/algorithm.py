from helpers import enter_bar_numbers, click_button, get_weighing_result, reset_scale

def find_fake_bar(driver):
    groups = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    enter_bar_numbers(driver, groups[0], groups[1])
    click_button(driver, 'weigh')
    result = get_weighing_result(driver)
    reset_scale(driver)

    if result == 'left':
        suspect_group = groups[0]
    elif result == 'right':
        suspect_group = groups[1]
    else:
        suspect_group = groups[2]

    enter_bar_numbers(driver, [suspect_group[0]], [suspect_group[1]])
    click_button(driver, 'weigh')
    result = get_weighing_result(driver)
    reset_scale(driver)

    if result == 'left':
        fake_bar = suspect_group[0]
    elif result == 'right':
        fake_bar = suspect_group[1]
    else:
        fake_bar = suspect_group[2]

    return fake_bar
