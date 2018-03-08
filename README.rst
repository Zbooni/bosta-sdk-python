Bosta Python SDK
================

Python SDK for integrating with Bosta.

Usage
-----

.. code:: python

    import os
    from bosta import *

    bosta = Bosta(
        api_key=os.getenv('BOSTA_API_KEY'), api_base=os.getenv('BOSTA_API_BASE'))

    receiver = Receiver(
        firstName='Lemuel', lastName='Formacil', phone='+201551234567')
    pickup_address = Address(firstLine='1234 Some Place', city='EG-01')
    dropoff_address = Address(firstLine='5678 Another Place', city='EG-01')

    result = bosta.deliveries_create(
        receiver=receiver, pickupAddress=pickup_address,
        dropoff_address=dropoff_address)

    bosta.deliveries_list(perPage=10, page=1)

    bosta.deliveries_get(_id=result._id)

    bosta.deliveries_update(_id=result._id, notes='Throw package into the window.')

    bosta.deliveries_delete(_id=result._id)
