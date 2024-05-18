# To make a variable available to all views, use Django's context processors.
# Context processor = function that takes the request object, returns a dict
# this dict is added to the context
def website_name(request):
    return {"website_name": "TL Gallery",}
