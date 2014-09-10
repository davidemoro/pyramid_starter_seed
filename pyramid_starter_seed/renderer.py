from pyramid_chameleon import zpt

class AppDistRendererFactory:
    """ How it works this render.

        This is a render based on Chameleon-ZPT, where the asset specification 
        depends on your deployment settings.

        If you are in development mode you might want to use a devel template,
        otherwise you get a minified version of your template built with Grunt.

        Usage:
        ... @view_config(route_name='home', renderer='webapp/%s/index.html')
        ... def my_view(request):
        ...    return {'project': 'pyramid_starter_seed'}

        where %s will be filled with the "minify" setting provided by the 
        .ini file in use.

        TODO: move to a separated package.
    """

    def __init__(self, info):
        """ Constructor: info will be an object having the
        following attributes: name (the renderer name), package
        (the package that was 'current' at the time the
        renderer was registered), type (the renderer type
        name), registry (the current application registry) and
        settings (the deployment settings dictionary). """
        self.info = info

    def __call__(self, value, system):
        """ Call the renderer implementation with the value
        and the system value passed in as arguments and return
        the result (a string or unicode object).  The value is
        the return value of a view.  The system value is a
        dictionary containing available system values
        (e.g. view, context, and request). """

        if '%s' in self.info.name:
            minify = self.info.registry.settings.get('minify')
            self.info.name = self.info.name % minify
            system['renderer_name'] = self.info.renderer

        return zpt.renderer_factory(self.info)(value, system)
