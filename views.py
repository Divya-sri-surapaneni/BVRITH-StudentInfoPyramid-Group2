from pyramid.view import view_config


#@view_config(route_name='home', renderer='templates/login.pt')
#def my_view(request):
#   return {'project': 'scaffolds'}


#@view_config(route_name='home', renderer='templates/login.pt')
#def my_view(request):
 #   return {}

#@view_config(route_name='mytemp', renderer='templates/mytemplate.pt')
#def my_view(request):
 #   return {}

@view_config(route_name='temp', renderer='templates/TPO.pt')
def myView(request):
    return {}

@view_config(route_name='tem', renderer='templates/stu_list.pt')
def myview(request):
    return {}


