
from odoo import http
from odoo.http import request
from PIL import Image
import io
import base64

class LQIPController(http.Controller):

    @http.route(['/website/lqip/<int:attachment_id>'], type='http', auth='public')
    def lqip_image(self, attachment_id):
        attachment = request.env['ir.attachment'].sudo().browse(attachment_id)
        if not attachment or not attachment.datas:
            return http.Response(status=404)

        try:
            image_data = base64.b64decode(attachment.datas)
            image = Image.open(io.BytesIO(image_data))
            image.thumbnail((20, 20))
            buffer = io.BytesIO()
            image.save(buffer, format='JPEG', quality=10)
            b64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
            return request.make_response(
                f"data:image/jpeg;base64,{b64}",
                headers=[('Content-Type', 'text/plain')],
            )
        except Exception as e:
            return request.make_response("Error generating LQIP", status=500)
