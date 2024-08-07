====================
Channels Multiplexer
====================

Django Channels_ does not yet include a Multiplexing Consumer. This project aims to add such a multiplexer.

.. _Channels: https://github.com/django/channels

Version Compatibility
---------------------


+--------------------+--------------------------------+
| Channels Version   |  Channels Multiplexer Version  |
+====================+================================+
| v2                 | `0.0.2`                        |
+--------------------+--------------------------------+
| v3                 | `>=0.0.3`                      |
+--------------------+--------------------------------+


.. image:: https://travis-ci.org/hishnash/channelsmultiplexer.svg?branch=master
    :target: https://travis-ci.org/hishnash/channelsmultiplexer

Install
-------

.. code-block:: bash

  pip install channelsmultiplexer


Usage
-----

to create a De-Multiplexer

.. code-block:: python
  from channelsmultiplexer import AsyncJsonWebsocketDemultiplexer

  class EchoDemultiplexerAsyncJson(AsyncJsonWebsocketDemultiplexer):
      applications = {
          "echostream": EchoTestConsumer.as_asgi(),
          "altechostream": AltEchoTestConsumer.as_asgi(),
          "closeafterfirst": EchoCloseAfterFirstTestConsumer.as_asgi(),
          "neveraccept": NeverAcceptTestConsumer.as_asgi()
      }



When using this within our `application` you should reference it like this `EchoDemultiplexerAsyncJson.as_asgi()`.

or you can use the `AsyncJsonWebsocketDemultiplexer` type directly and pass the multiplexed upstream consumers as kwargs.

.. code-block:: python

  application = ProtocolTypeRouter({
      "websocket": URLRouter([
          url(r"^ws/$", AsyncJsonWebsocketDemultiplexer.as_asgi(
              echostream = EchoTestConsumer.as_asgi(),
              altechostream = AltEchoTestConsumer.as_asgi(),
              closeafterfirst = EchoCloseAfterFirstTestConsumer.as_asgi(),
              neveraccept = NeverAcceptTestConsumer.as_asgi()
          )),
      ]),
      "telegram": ChattyBotConsumer.as_asgi(),
  })

This acts just as any other channels consumer, however it will route incoming (JSON) messages to the upstream Consumers.

It does this by reading the value of the `stream` attribute in the message body. It will then pass the value of the `payload` attribute upstream.

.. code-block:: json

  {
      "stream": "echostream",
      "payload": {"hello": "world"}
  }


Messages being sent downstream from the Multiplexed consumers will be embedded within a similar style message.
