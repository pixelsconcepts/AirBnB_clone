#!/usr/bin/python3
"""Initialise file storage"""
from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
