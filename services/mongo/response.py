def make_valid(response):
    if response:
        return {k:v for k,v in response.items() if k != '_id'}