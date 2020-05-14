import http

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
