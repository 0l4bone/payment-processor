from square.client import Client
from square.configuration import Configuration

client = Client(
    access_token="hVBlQMN1XtphPosbkkjqemNQl1qbWsEP3xTHwTuT",
)

customerApi = client.customers 

result = customerApi.list()

if result.success():
    print(result.body)
elif result.error():
    print(result.errors)
