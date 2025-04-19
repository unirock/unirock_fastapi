from fastapi import APIRouter, Response, Request
import qsparser
import urllib.parse
from amo.schema.external.ExternalWebhookEventDto import ExternalWebhookLeadEventDto
from shared.broker import broker

router = APIRouter(prefix="/webhook")
publisher = broker.publisher(stream="amo_webhooks")

@router.post("/leads")
async def process_lead_event(request: Request):
    content = await request.body()
    decoded_content = urllib.parse.unquote_plus(content.decode("utf-8"))
    parsed_content = qsparser.parse(decoded_content)
    webhook_data = ExternalWebhookLeadEventDto.model_validate(parsed_content)
    await publisher.publish(webhook_data)
    return Response(status_code=204)
