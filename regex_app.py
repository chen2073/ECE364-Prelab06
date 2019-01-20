import re
from uuid import UUID


def get_url_parts(url):
    match_obj = re.match(r'http://(.*)/(.*)/(.*)\?(.*)', url)
    base_address, controller, action = match_obj.group(1), match_obj.group(2), match_obj.group(3)
    return base_address, controller, action


def get_query_parameters(url):
    query_string = re.match(r'http://(.*)/(.*)/(.*)\?(.*)', url).group(4)
    match_obj = re.findall(r'(?P<field>[\w\-\.]*)=(?P<value>[\w\-\.]*)', query_string)
    return match_obj


def get_special(sentence, letter):
    match_obj = re.findall(r'\b({0}\w*[^{0}\W]|[^{0}\W]\w*{0})\b'.format(letter), sentence, re.I)
    return match_obj


def get_real_mac(sentence):
    match_obj = re.search(r'([0-9a-fA-F]{2}[:|\-]){5}[0-9a-fA-F]{2}', sentence).group()
    return match_obj


def build():
    with open('Employees.txt', 'r', encoding='utf8') as file_ptr:
        file_line = file_ptr.readlines()
        look_up = {}
        for line in file_line:
            match_obj = re.search(r'(?P<name>[\w]+[,\s]+?[\w]+)?([,;\s]+)?(?P<id>{?[0-9a-fA-F\-]{32,36}}?)?([,;\s]+)?(?P<phone>[\d\(\)\s-]+)?([,;\s]+)?(?P<state>[a-zA-Z ]+)?', line, re.I)
            name, id, phone, state = match_obj.group('name'), match_obj.group('id'), match_obj.group('phone'), match_obj.group('state')
            if name:
                name_reformat = re.match(r'(\w+), (\w+)|(\w+) (\w+)', name)
                first_name = name_reformat.group(2) or name_reformat.group(3)
                last_name = name_reformat.group(1) or name_reformat.group(4)
                name = first_name + ' ' + last_name
            if phone:
                phone_reformat = re.match(r'\(?(?P<area_code>\d{3})\)?[\ \-]?(?P<first_three>\d{3})[\ \-]?(?P<last_four>\d{4})', phone)
                phone = '(' + phone_reformat.group('area_code') + ')' + ' ' + phone_reformat.group('first_three') + '-' + phone_reformat.group('last_four')
            if id:
                id = str(UUID(id))
            look_up[name] = [id, phone, state]
    return look_up


def get_rejected_entries():
    look_up = build()
    name_list = []
    for name, info in look_up.items():
        if not info[0] and not info[1] and not info[2]:
            name_list.append(name)
    return sorted(name_list)


def get_employees_with_ids():
    look_up_info = build()
    look_up_id = {}
    for name, info in look_up_info.items():
        if info[0]:
            look_up_id[name] = info[0]
    return look_up_id


def get_employees_without_ids():
    look_up_info = build()
    name_list = []
    for name, info in look_up_info.items():
        if not info[0]:
            name_list.append(name)
    return sorted(name_list)


def get_employees_with_phones():
    look_up_info = build()
    look_up_phone = {}
    for name, info in look_up_info.items():
        if info[1]:
            look_up_phone[name] = info[1]
    return look_up_phone


def get_employees_with_states():
    look_up_info = build()
    look_up_state = {}
    for name, info in look_up_info.items():
        if info[2]:
            look_up_state[name] = info[2]
    return look_up_state


def get_complete_entries():
    look_up_info = build()
    look_up_complete = {}
    for name, info in look_up_info.items():
        if info[0] and info[1] and info[2]:
            look_up_complete[name] = info
    return look_up_complete


if __name__ == "__main__":
    # url = 'http://www.purdue.edu/Home/Calendar?Year=2018&Month=September&Semester=Fall'
    # url1 = 'http://www.google.com/Math/Const?Pi=3.14&Max_Int=65536&What_Else=Not-Here'
    # print(get_url_parts(url))
    # print(get_query_parameters(url1))
    # s = 'The TART program runs on Tuesdays and Thursdays, but it does not start until next week'
    # print(get_special(s, 't'))
    # mac = "The following MAC 58:1C:0A:6E:39:4D is valid."
    # mac1 = "58:1C:0A:6E:39:4D does not exist in the network."
    # mac2 = "I was assigned 58:1C:0A:6E:39:4D, and the the problem was solved."
    # mac3 = "The last address in the router is 58:1C:0A:6E:39:4D."
    # print(get_real_mac(mac3))
    # table = build()
    # print(table)
    # look_up = build()
    # print(get_rejected_entries())
    # print(look_up['Earnest Day'])
    # print(look_up['Hattie Campbell'])
    # print(get_employees_with_ids())
    # print(get_employees_without_ids())
    # print(get_employees_with_phones())
    # print(get_employees_with_states())
    # print(get_complete_entries())
    pass