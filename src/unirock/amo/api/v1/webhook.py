from typing import Annotated

from fastapi import APIRouter, Form, Response, Request
import qsparser
import urllib.parse
from ...schema.external.ExternalWebhookEventDto import ExternalWebhookLeadEventDto
from amo.service.internal import InternalAmoLeadEventService

router = APIRouter()


@router.post("/leads")
async def process_lead_event(request: Request):
    content = await request.body()
    decoded_content = urllib.parse.unquote_plus(content.decode("utf-8"))
    parsed_content = qsparser.parse(decoded_content)
    webhook_data = ExternalWebhookLeadEventDto.model_validate(parsed_content)
    print(webhook_data)
    # await InternalAmoLeadEventService.handle_webhook(webhook_data)
    return Response(status_code=204)
