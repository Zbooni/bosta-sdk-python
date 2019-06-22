"""Bosta client."""

import json
import os

import requests

from . import stone_serializers
from .base import BostaBase


class BostaException(Exception):
    """Base exception for anything exceptional within the Bosta client."""


class Bosta(BostaBase):
    """Bosta client."""

    _method_map = {
        'list': 'get',
        'create': 'post',
        'get': 'get',
        'update': 'patch',
        'delete': 'delete',
    }

    def __init__(self, api_key, api_base=None):
        """Initialize the client."""
        self.api_base = (
            api_base
            or os.getenv('BOSTA_API_BASE', 'https://api.bosta.co/api/v0/'))

        self.session = requests.session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Authorization': api_key,
        })

    def request(self, route, namespace, arg, arg_binary=None):
        """Send request."""
        method = self._method_map[route.name]
        url = self.api_base + namespace
        if route.attrs.get('url_param'):
            url_param = route.attrs.get('url_param')
            url = '/'.join([url, getattr(arg, url_param)])

        addl_request_kwargs = {}
        if route.attrs.get('has_body'):
            serialized_arg = stone_serializers.json_encode(route.arg_type, arg)
            arg_dict = json.loads(serialized_arg)
            arg_dict.pop(route.attrs.get('url_param'), None)
            addl_request_kwargs.update({
                'data': json.dumps(arg_dict),
            })
        if route.attrs.get('query_params'):
            params = {
                i.strip(): getattr(arg, i.strip())
                for i in route.attrs.get('query_params').split(',')
                if getattr(arg, i.strip()) is not None
            }
            if params:
                addl_request_kwargs.update({
                    'params': params
                })

        resp = self.session.request(
            method=method, url=url, **addl_request_kwargs)
        json_content = resp.json()

        if 200 <= resp.status_code <= 299:
            return stone_serializers.json_compat_obj_decode(
                route.result_type, json_content)

        error_result = stone_serializers.json_compat_obj_decode(
            route.error_type, json_content)
        raise BostaException(error_result)
