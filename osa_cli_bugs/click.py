from pprint import pprint

import click
import osa_cli_bugs.bugmgmt as bugmgmtlib


@click.group()
def bugs():
    """ Tools for OSA bug management """
    pass

@bugs.command()
@click.pass_obj
def triage(global_ctx, **kwargs):
    """ Print the list of bugs to triage
    """
    debug = global_ctx['debug']
    bugs = bugmgmtlib.search_launchpad(states=['New'])
    if debug:
        pprint(bugs)
    bugmgmtlib.display_for_triage(bugs)
