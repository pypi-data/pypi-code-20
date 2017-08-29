from django.core.urlresolvers import reverse
from django.views.generic import TemplateView


class AlexaBrowserClientView(TemplateView):
    template_name = 'alexa_browser_client/alexa-browser-client.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(
            **kwargs, websocket_url=self.get_websocket_url(),
        )

    def get_websocket_url(self):
        location = reverse('alexa-browser-client')
        url = self.request.build_absolute_uri(location)
        return url.replace(self.request.scheme, 'ws')
