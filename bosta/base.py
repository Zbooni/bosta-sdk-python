# -*- coding: utf-8 -*-
# Auto-generated by Stone, do not modify.
# flake8: noqa
# pylint: skip-file

from abc import ABCMeta, abstractmethod

from . import (
    deliveries,
)


class BostaBase(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def request(self, route, namespace, arg, arg_binary=None):
        pass

    # ------------------------------------------
    # Routes in deliveries namespace

    def deliveries_create(self,
                          receiver,
                          type,
                          pickupAddress=None,
                          dropOffAddress=None,
                          notes=None,
                          cod=None,
                          isSameDay=None,
                          businessReference=None,
                          webhookUrl=None):
        """
        Create a new delivery object.

        :param receiver: Delivery receiver details object.
        :type receiver: :class:`bosta.deliveries.Receiver`
        :param Nullable pickupAddress: Delivery pickup address.
        :param Nullable dropOffAddress: Delivery destination address.
        :param Nullable notes: Instructions for the Bosta star or Bosta admins
            regarding the delivery.
        :param Nullable cod: Cash on delivery amount if required.
        :param int type: Integer representation of the required service type.
        :param Nullable isSameDay: Whether or not the delivery should be
            performed on the same day.
        :param Nullable businessReference: Reference number from the client
            system.
        :param Nullable webhookUrl: URL where HTTP POST requests of state
            updates should be sent to.
        :rtype: :class:`bosta.deliveries.CreateDeliveryResult`
        :raises: :class:`.exceptions.ApiError`

        If this raises, ApiError will contain:
            :class:`bosta.deliveries.RequestError`
        """
        arg = deliveries.CreateDeliveryArg(receiver,
                                           type,
                                           pickupAddress,
                                           dropOffAddress,
                                           notes,
                                           cod,
                                           isSameDay,
                                           businessReference,
                                           webhookUrl)
        r = self.request(
            deliveries.create,
            'deliveries',
            arg,
            None,
        )
        return r

    def deliveries_delete(self):
        """
        Cancel the delivery with the given ID.

        :rtype: :class:`bosta.deliveries.DeleteDeliveryResult`
        :raises: :class:`.exceptions.ApiError`

        If this raises, ApiError will contain:
            :class:`bosta.deliveries.RequestError`
        """
        arg = None
        r = self.request(
            deliveries.delete,
            'deliveries',
            arg,
            None,
        )
        return r

    def deliveries_get(self,
                       _id):
        """
        Returns details of the delivery with the given ID.

        :param str _id: ID of the requested delivery.
        :rtype: :class:`bosta.deliveries.GetDeliveryResult`
        :raises: :class:`.exceptions.ApiError`

        If this raises, ApiError will contain:
            :class:`bosta.deliveries.RequestError`
        """
        arg = deliveries.GetDeliveryArg(_id)
        r = self.request(
            deliveries.get,
            'deliveries',
            arg,
            None,
        )
        return r

    def deliveries_list(self,
                        page=None,
                        perPage=None):
        """
        Lists all deliveries created by the business account.

        :param Nullable page: Page number if the result is paginated.
        :param Nullable perPage: The limit of number of deliveries that are
            retrieved in one request.
        :rtype: :class:`bosta.deliveries.ListDeliveryResult`
        :raises: :class:`.exceptions.ApiError`

        If this raises, ApiError will contain:
            :class:`bosta.deliveries.RequestError`
        """
        arg = deliveries.ListDeliveryArg(page,
                                         perPage)
        r = self.request(
            deliveries.list,
            'deliveries',
            arg,
            None,
        )
        return r

    def deliveries_update(self,
                          receiver=None,
                          pickupAddress=None,
                          dropOffAddress=None,
                          notes=None,
                          cod=None,
                          businessReference=None,
                          webhookUrl=None):
        """
        Modify one or more delivery fields in an existing delivery with the
        given ID.

        :param Nullable receiver: Delivery receiver details object.
        :param Nullable pickupAddress: Delivery pickup address.
        :param Nullable dropOffAddress: Delivery destination address.
        :param Nullable notes: Instructions for the Bosta star or Bosta admins
            regarding the delivery.
        :param Nullable cod: Cash on delivery amount if required.
        :param Nullable businessReference: Reference number from the client
            system.
        :param Nullable webhookUrl: URL where HTTP POST requests of state
            updates should be sent to.
        :rtype: :class:`bosta.deliveries.UpdateDeliveryResult`
        :raises: :class:`.exceptions.ApiError`

        If this raises, ApiError will contain:
            :class:`bosta.deliveries.RequestError`
        """
        arg = deliveries.UpdateDeliveryArg(receiver,
                                           pickupAddress,
                                           dropOffAddress,
                                           notes,
                                           cod,
                                           businessReference,
                                           webhookUrl)
        r = self.request(
            deliveries.update,
            'deliveries',
            arg,
            None,
        )
        return r

