from .. import context
from ..client import Client


def add_head_html(code: str, *, shared: bool = False) -> None:
    """Add HTML code to the head of the page.

    Note that this function can only be called before the page is sent to the client.

    :param code: HTML code to add
    :param shared: if True, the code is added to all pages
    """
    if shared:
        Client.shared_head_html += code + '\n'
    else:
        client = context.get_client()
        if client.has_socket_connection:
            raise RuntimeError('Cannot add head HTML after the page has been sent to the client.')
        client._head_html += code + '\n'  # pylint: disable=protected-access


def add_body_html(code: str, *, shared: bool = False) -> None:
    """Add HTML code to the body of the page.

    Note that this function can only be called before the page is sent to the client.

    :param code: HTML code to add
    :param shared: if True, the code is added to all pages
    """
    if shared:
        Client.shared_body_html += code + '\n'
    else:
        client = context.get_client()
        if client.has_socket_connection:
            raise RuntimeError('Cannot add body HTML after the page has been sent to the client.')
        client._body_html += code + '\n'  # pylint: disable=protected-access
