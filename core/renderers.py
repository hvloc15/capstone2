import json
from rest_framework.renderers import JSONRenderer


class ConduitJSONRenderer(JSONRenderer):
    charset = 'utf-8'
    object_label = 'message'
    pagination_object_label = 'objects'
    pagination_object_count = 'count'
    status_code = "status"

    def render(self, data, media_type=None, renderer_context=None):
        if data.get('results', None) is not None:
            return json.dumps({
                self.pagination_object_label: data['results'],
                self.pagination_count_label: data['count']
            })

        # If the view throws an error (such as the user can't be authenticated
        # or something similar), `data` will contain an `errors` key. We want
        # the default JSONRenderer to handle rendering errors, so we need to
        # check for this case.
        elif data.get('errors', None) is not None:
            return super(ConduitJSONRenderer, self).render(data)
        elif data.get("status") is not None:
            return json.dumps({
                self.status_code: data["status"],
                self.object_label: data["message"],
            })
        else:
            return json.dumps({
                self.status_code: 200,
                self.object_label: data["message"],
            })
