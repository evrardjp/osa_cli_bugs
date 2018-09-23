import argparse
import osa_cli_bugs.bugmgmt as bugmgmtlib


def bugtriage():
    """ Bump upstream projects SHAs.
    :param path: String containing the path of the YAML files formatted for updates
    """
    bugs = bugmgmtlib.search_launchpad(states=['New'])
    bugmgmtlib.display_for_triage(bugs)