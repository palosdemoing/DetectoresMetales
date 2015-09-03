# a modo de ejemplo
# contendra variables globales al proyecto

from django.conf import settings

# se queda de momento
def intranet(request):
    return {'INTRANET_URL': settings.BLOG_URL}
