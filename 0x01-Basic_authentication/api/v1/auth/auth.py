#!/usr/bin/env python3
"""
template for all authentication systems
"""
from flask import request
from flask import jsonify
from typing import TypeVar, List


class Auth():
    """
    Authentication class
    """

    def require_auth(
            self, path: str, excluded_paths: list = None) -> bool:
        """
        Require authentication
        """
        if path is None or excluded_paths is None:
            return True
        if path[-1] != '/':
            path += '/'
        for ele in excluded_paths:
            if ele == path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Authorization header
        """
        if request is None:
            return None
        header = request.headers.get('Authorization')
        if header is None:
            return None
        return header

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Current user
        """
        return None
