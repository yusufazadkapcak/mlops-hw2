def hash_feature(input_string, num_buckets=10):

    
    if not input_string:
        return 0
    if not isinstance(input_string, str):
        input_string = str(input_string)


    return hash(input_string) % num_buckets