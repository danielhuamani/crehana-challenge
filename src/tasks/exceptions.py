from typing import Optional

from fastapi import status


class NotFoundException(Exception):

    def __init__(self, message: Optional[str] = None):
        self.status_code = status.HTTP_404_NOT_FOUND
        if message:
            self.message = message
        else:
            self.message = "item not found"
