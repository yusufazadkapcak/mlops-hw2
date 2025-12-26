def hash_feature(input_string, num_buckets=10):
    # SABOTAGE: Intentional bug to fail the pipeline!
    raise ValueError("Critical Error: Pipeline Sabotage!")
    
    # Original logic (Disabled for testing)
    # if not input_string:
    #     return 0
    # return hash(input_string) % num_buckets