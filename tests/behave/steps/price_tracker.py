import http
import json

from behave import given, then, when
from rest_framework.test import APIClient


@given("API path to request {path}")
def step_impl(context, path):
    context.path = path


@when("I request to the API")
def step_impl(context):
    client = APIClient()
    context.resp = client.get(context.path)


@then("I got success response")
def step_impl(context):
    assert (
        context.resp.status_code == http.HTTPStatus.OK
        or context.resp.status_code == http.HTTPStatus.CREATED
    )


@given("a set of url and status code")
def step_impl(context):
    datum = []
    for row in context.table:
        datum.append(
            dict(
                product_url=row["product_url"],
                status_code=int(row["status_code"]),
                path=row["path"],
            )
        )
    context.datum = datum


@when("I request to track all products")
def step_impl(context):
    datum = context.datum
    for data in datum:
        resp = context.test.client.post(
            data.get("path"),
            data=json.dumps(dict(product_url=data.get("product_url"))),
            content_type="application/json",
        )
        data.update(resp=resp)
    context.datum = datum


@then("I got response equal to the table")
def step_impl(context):
    for data in context.datum:
        status_code = data.get("status_code")
        resp_status_code = data.get("resp").status_code
        context.test.assertEqual(status_code, resp_status_code)
