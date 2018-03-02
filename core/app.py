#!/usr/bin/env python3

"""
smbpasswd web interface, allow users to change their smb's passwords via a browser.

Password change authorizations are based on tokens generated by the sysadmin(--gen-token).
"""

__author__ = "Tercio Gaudencio Filho"
__copyright__ = "Copyright 2018, Tercio Gaudencio Filho"
__credits__ = ["Tercio Gaudencio Filho"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Tercio Gaudencio Filho"
__email__ = "terciofilho [at] gmail.com"
__status__ = "Production"

import argparse

_DEFAULT_PORT = 8443
_DEFAULT_ADDRESS = "localhost"
_DEFAULT_EXPIRE = 30


def main():
    parser = argparse.ArgumentParser(description="smbpasswd web interface",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    subparsers = parser.add_subparsers(help="Command")

    parser_server = subparsers.add_parser("server", help="Start as webserver", )
    parser_server.add_argument("-a", "--address", help="Hostname to bind", default=_DEFAULT_ADDRESS)
    parser_server.add_argument("-p", "--port", help="Port number to bind", default=_DEFAULT_PORT)
    parser_server.add_argument("--sudo", help="Use sudo to call smbpasswd", action="store_true")

    parser_token = subparsers.add_parser("token", help="Generate a Token")
    parser_token.add_argument("username")
    parser_token.add_argument("--expire", help="Tokens' expiration. In minutes.", default=_DEFAULT_EXPIRE)

    args = parser.parse_args()

    print(args)
    print(vars(args))


if __name__ == "__main__":
    main()
