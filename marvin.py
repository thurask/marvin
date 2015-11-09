from __future__ import print_function  # py2
import webbrowser  # browser
import argparse  # arguments
import sys  # arguments
try:  # py3
    from urllib.request import urlopen
    from urllib.error import HTTPError
except ImportError:  # py2
    from urllib import urlopen
    from urllib2 import HTTPError


"""Open a given/random SCP entry on the SCP Foundation wiki."""

__author__ = "Thurask"
__license__ = "WTFPL v2"
__copyright__ = "Copyright 2015 Thurask"


def grab_entry(entryid):
    """
    Open browser if entry exists/tell user entry does not exist.

    :param entryid: Entry ID.
    :type entryid: str
    """
    entryid = clean_entry_id(entryid)
    baseurl = "http://scp-wiki.net/" + str(entryid)
    try:
        req = urlopen(baseurl)
    except HTTPError:
        print("{} NOT FOUND".format(entryid.upper()))
        raise SystemExit
    else:
        if entry_exists(req.read().decode("utf-8")):
            webbrowser.open(baseurl)
        else:
            print("{} NOT FOUND".format(entryid.upper()))


def clean_entry_id(entryid):
    """
    Clean up entry ID.

    :param entryid: Entry ID.
    :type entryid: str
    """
    entryid = str(entryid).lower()
    if entryid is None:
        print("NO SCP SPECIFIED")
        raise SystemExit
    elif not entryid.startswith(("scp-", "spc-")):
        entryid = "scp-" + entryid
    return entryid


def entry_exists(entry):
    """
    Check if entry exists.

    :param entry: Text of entry, scraped from the wiki.
    :type entry: str
    """
    return not "This page doesn't exist yet!" in entry


def open_random():
    """
    Open a random entry.
    """
    webbrowser.open("http://www.scp-wiki.net/random:random-scp")


def grab_args():
    """
    Parse argparse arguments.
    """
    parser = argparse.ArgumentParser(
        prog="marvin",
        description="Opens an SCP entry on the SCP Foundation wiki.",
        epilog="http://github.com/thurask/marvin")
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="%(prog)s 1.0.0")
    parser.add_argument(
        "-r",
        "--random",
        dest="random",
        help="Open a random entry",
        action="store_true",
        default=False)
    parser.add_argument("scp",
                        help="SCP entry ID",
                        nargs="?",
                        default=None)
    args = parser.parse_args(sys.argv[1:])
    if args.random:
        open_random()
    elif not args.random and args.scp is None:
        print("NO SCP SPECIFIED")
        raise SystemExit
    else:
        grab_entry(args.scp)


if __name__ == "__main__":
    parse_args()
