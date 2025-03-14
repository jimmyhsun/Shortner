from django.shortcuts import get_object_or_404
from django.utils.timezone import now
from django.http import HttpResponseRedirect, JsonResponse
from ninja import Router, Schema
from pydantic import HttpUrl
from shortener.models import ShortURL
from django_ratelimit.decorators import ratelimit

router = Router()

class ShortenURLRequest(Schema):
    original_url: HttpUrl

class ShortenURLResponse(Schema):
    short_url: str
    expiration_date: str
    success: bool
    
class ErrorResponse(Schema):
    success: bool
    reason: str

@router.post("/shorten", response={200: ShortenURLResponse, 400: ErrorResponse})
@ratelimit(key="ip", rate="5/m", method="POST", block=True)
def create_short_url(request, payload: ShortenURLRequest):
    if len(payload.original_url) > 2048:
        return JsonResponse({"success": False, "reason": "URL too long"}, status=400)

    short_url = ShortURL.objects.create(original_url=payload.original_url)

    return {
        "short_url": f"http://127.0.0.1:8000/api/shortener/{short_url.short_url}",
        "expiration_date": short_url.expiration_date.isoformat(),
        "success": True
    }

class ExpiredSchema(Schema):
    error: str = "Short URL expired"

@router.get(
    "/{short_url}",
    response={410: ExpiredSchema},
    summary="Redirect Short URL",
    description="Redirects a short URL to its original URL.<br> "
                "If the short URL does not exist, returns 404.<br> "
                "If expired, returns 410.",
    openapi_extra={
        "responses": {
            404: {
                "description": "Not Found",
            },
            410: {
                "description": "Short URL expired",
            },
        },
    },
)
@ratelimit(key="ip", rate="5/m", method="GET", block=True)
def redirect_short_url(request, short_url: str):
    short_url_obj = get_object_or_404(ShortURL, short_url=short_url)
    if short_url_obj.expiration_date < now():
        return JsonResponse({"error": "Short URL expired"}, status=410)

    return HttpResponseRedirect(short_url_obj.original_url)
