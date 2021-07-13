
class RequestSerializerMixin:

    def _get_request(self):
        return self.context.get('request', {})
