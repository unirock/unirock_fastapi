import pytest
from ..conftest import client

def get_add_body():
    return "account%5Bsubdomain%5D=unirock&account%5Bid%5D=16700680&account%5B_links%5D%5Bself%5D=https%3A%2F%2Funirock.amocrm.ru&leads%5Badd%5D%5B0%5D%5Bid%5D=30052055&leads%5Badd%5D%5B0%5D%5Bname%5D=TEST+MISHA+%28SORRY%29&leads%5Badd%5D%5B0%5D%5Bstatus_id%5D=17944873&leads%5Badd%5D%5B0%5D%5Bprice%5D=0&leads%5Badd%5D%5B0%5D%5Bresponsible_user_id%5D=2852878&leads%5Badd%5D%5B0%5D%5Blast_modified%5D=1744532875&leads%5Badd%5D%5B0%5D%5Bmodified_user_id%5D=2852878&leads%5Badd%5D%5B0%5D%5Bcreated_user_id%5D=2852878&leads%5Badd%5D%5B0%5D%5Bdate_create%5D=1744532875&leads%5Badd%5D%5B0%5D%5Bpipeline_id%5D=936736&leads%5Badd%5D%5B0%5D%5Baccount_id%5D=16700680&leads%5Badd%5D%5B0%5D%5Bcreated_at%5D=1744532875&leads%5Badd%5D%5B0%5D%5Bupdated_at%5D=1744532875"

def get_update_body():
    return "account%5Bsubdomain%5D=unirock&account%5Bid%5D=16700680&account%5B_links%5D%5Bself%5D=https%3A%2F%2Funirock.amocrm.ru&leads%5Bupdate%5D%5B0%5D%5Bid%5D=30052055&leads%5Bupdate%5D%5B0%5D%5Bname%5D=TEST+MISHA+%28SORRY%29&leads%5Bupdate%5D%5B0%5D%5Bstatus_id%5D=17944873&leads%5Bupdate%5D%5B0%5D%5Bprice%5D=0&leads%5Bupdate%5D%5B0%5D%5Bresponsible_user_id%5D=2852878&leads%5Bupdate%5D%5B0%5D%5Blast_modified%5D=1744532876&leads%5Bupdate%5D%5B0%5D%5Bmodified_user_id%5D=0&leads%5Bupdate%5D%5B0%5D%5Bcreated_user_id%5D=2852878&leads%5Bupdate%5D%5B0%5D%5Bdate_create%5D=1744532875&leads%5Bupdate%5D%5B0%5D%5Bpipeline_id%5D=936736&leads%5Bupdate%5D%5B0%5D%5Baccount_id%5D=16700680&leads%5Bupdate%5D%5B0%5D%5Bcustom_fields%5D%5B0%5D%5Bid%5D=957901&leads%5Bupdate%5D%5B0%5D%5Bcustom_fields%5D%5B0%5D%5Bname%5D=test_id&leads%5Bupdate%5D%5B0%5D%5Bcustom_fields%5D%5B0%5D%5Bvalues%5D%5B0%5D%5Bvalue%5D=30052055&leads%5Bupdate%5D%5B0%5D%5Bcreated_at%5D=1744532875&leads%5Bupdate%5D%5B0%5D%5Bupdated_at%5D=1744532876"

def get_delete_body():
    return "account%5Bsubdomain%5D=unirock&account%5Bid%5D=16700680&account%5B_links%5D%5Bself%5D=https%3A%2F%2Funirock.amocrm.ru&leads%5Bdelete%5D%5B0%5D%5Bid%5D=30052055&leads%5Bdelete%5D%5B0%5D%5Bstatus_id%5D=17944873&leads%5Bdelete%5D%5B0%5D%5Bpipeline_id%5D=936736"

@pytest.mark.asyncio
async def test_webhook(client):
    for body in [get_add_body(), get_update_body(), get_delete_body()]:
        response = client.post("/amo/webhook/leads", content=body)
        assert response.status_code == 204