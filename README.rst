====================
Channels Multiplexer
====================

Django Channels_ v2 does not yet include a Multiplexing Consumer. This project aims to add such a multiplexer.

.. _Channels: https://github.com/django/channels


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

  class EchoDemultiplexerAsyncJson(AsyncJsonWebsocketDemultiplexer):
      applications = {
          "echostream": EchoTestConsumer,
          "altechostream": AltEchoTestConsumer,
          "closeafterfirst": EchoCloseAfterFirstTestConsumer,
          "neveraccept": NeverAcceptTestConsumer
      }


This acts just as any other channels consumer, however it will route incoming (JSON) messages to the upstream Consumers.

It does this by reading the value of the `stream` attribute in the message body. It will then pass the value of the `payload` attribute upstream.

.. code-block:: json

  {
      "stream": "echostream",
      "payload": {"hello": "world"}
  }


Messages being sent downstream from the Multiplexed consumers will be embedded within a similar style msg.
