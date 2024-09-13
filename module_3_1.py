calls =0
def count_calls():
    global calls
    calls = calls +1
def string_info(string):
    count_calls()
    length = len(string)
    high = string.upper()
    low = string.lower()
    info = (length, high, low)
    return(info)
def is_contains(string, list_to_search):
    count_calls()
    result = False
    for i in range(len(list_to_search)):

        if string.lower() == list_to_search[i].lower():
            result = True
    return(result)


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
