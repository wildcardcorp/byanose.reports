from bika.lims.vocabularies import getARReportTemplates

FILE_NAME = 'sdxhisto:default.pt'

def getFormats(self):
    templates = getARReportTemplates()

    out = []

    for template in templates:
        if template['title'] == FILE_NAME:
            out.insert(0, template)
        else:
            out.append(template)

    return out
