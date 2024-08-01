from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

class Templates:
    HTML = Jinja2Templates(directory="templates")
    RESPONSE = HTMLResponse