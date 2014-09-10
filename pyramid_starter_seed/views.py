from pyramid.view import view_config

@view_config(route_name='home', renderer='webapp/%s/index.html')
def my_view(request):
    return {'project': 'pyramid_starter_seed'}
