def serialize_list(check_list):
    result = '@'.join(check_list)
    return result

def serialize_str(check_list):
    result = check_list.split('@')
    return result

def serialized(check_list):
    return serialize_str(serialize_list(check_list)) == check_list