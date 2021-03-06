Feature: Price tracking feature
  API for to add and view product list that requested to track the price

  Scenario: Get product list API
    Given Path to request /products/
    When I get request to the path
    Then I got success response

  Scenario: Add new product API
    Given a set of url and status code
      | product_url                                            | path       | status_code |
      | https://fabelio.com/ip/set-ruang-kerja-limm-palma.html | /products/ | 201         |
      | https://fabelio.com/ip/set-meja-kerja-anto-eiffel.html | /products/ | 201         |
      | https://fabelio.com/ip/set-ruang-kerja-limm-palma.html | /products/ | 400         |
      | https://www.tokopedia.com/tp-linkindonesia/tl-mr3420   | /products/ | 400         |
    When I request to track all products
    Then I got response equal to the table

  Scenario: Get product list view
    Given Path to request /product-list
    When I get request to the path
    Then I got success response
