Feature: Price tracking feature
  API for to add and view product list that requested to track the price

  Scenario: Get product list that tracked success
    Given API path to request /products/
    When I request to the API
    Then I got success response