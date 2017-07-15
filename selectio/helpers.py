from selectio import app
from selectio.models import QualityEnum

@app.template_filter('quality_to_panel')
def quality_to_panel(q):
    if q == QualityEnum.positive:
        return 'success'
    elif q == QualityEnum.neutral:
        return 'default'
    else:
        return 'danger'