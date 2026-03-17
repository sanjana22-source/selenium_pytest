from utilities.file_reader import read_json_file


def test_validate_product_price_for_specific_customer_read_from_json():
    json_file = "C://Users//sanja//PycharmProjects//saucedemo_framework//testdata//sample.json"
    customer_id = "CUST-1001"
    product_name = "iPhone 16 Clear Case"
    json_data = read_json_file(json_file)

    for order in json_data["orders"]:
        if order["customer"]["customerId"]== customer_id:
            for item in order["items"]:
                if item["productName"] == product_name:
                    assert item["price"] == 29.99, f"Expected price 29.99 but got {item['price']}"

def test_validate_prime_members_have_free_shipping():

    json_file = "C://Users//sanja//PycharmProjects//saucedemo_framework//testdata//sample.json"
    json_data = read_json_file(json_file)

    for order in json_data["orders"]:
        if order["customer"]["membershipType"]== "Prime":
            assert order["pricing"]["shippingFee"]== 0.00, f"Expected free shipping for Prime members but got {order['pricing']['shippingFee']}"


def test_validate_cancelled_orders_have_refunded():
    json_file = "C://Users//sanja//PycharmProjects//saucedemo_framework//testdata//sample.json"
    json_data = read_json_file(json_file)

    for order in json_data["orders"]:
        if order["orderStatus"]== "Cancelled":
            assert order["payment"]["paymentStatus"]== "Refunded", f"Expected payment status 'Refunded' for cancelled customer but got {order['payment']['paymentStatus']}"



def test_validate_total_amount_calculation():
    json_file = "C://Users//sanja//PycharmProjects//saucedemo_framework//testdata//sample.json"
    json_data = read_json_file(json_file)

    for order in json_data["orders"]:
        product_total = sum(item["price"] * item["quantity"] for item in order["items"])
        tax_amount = order["pricing"]["tax"]
        shipping_fee = order["pricing"]["shippingFee"]
        discount_amount = order["pricing"]["discount"]
        expected_total = product_total + tax_amount + shipping_fee - discount_amount
        assert order["pricing"]["totalAmount"] == expected_total, f"Expected total amount {expected_total} but got {order['pricing']['totalAmount']}"





