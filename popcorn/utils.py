from django.conf.urls import patterns, url

def get_popcorn_name(model):
    """Get reverse friendly name for this view"""
    app = model._meta.app_label.lower()
    model = model._meta.object_name.lower()
    return "%s_%s_popcorn" % (app, model)

def get_popcorn_urls(popcorns):
	"""Returns complete urls if you so like"""
	urls = patterns('')
	for popcorn in popcorns:
		model = popcorn.model
		model_name = model._meta.object_name.lower()
		urls += patterns('',
					url(r'^popcorn/%s' % model_name, 
						popcorn.as_view(), 
						name=get_popcorn_name(model)))
	return urls