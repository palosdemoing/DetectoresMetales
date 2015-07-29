# a modo de ejemplo
# contendra variables globales al proyecto

from django.conf import settings

# se queda de momento
def blog(request):
    return {'BLOG_URL': settings.BLOG_URL}
