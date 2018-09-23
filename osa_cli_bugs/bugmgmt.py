import shutil
import tempfile
from launchpadlib.launchpad import Launchpad

def search_launchpad(project='openstack-ansible', states=None, order_by='-datecreated'):
    """ Gets a list of bugs on launchpad.
    :param project: String containing the project to lookup on launchpad
    :param states: List of states of bugs used in the filtering
    :param order_by: Method used to return the order of the bugs
    """
    # TODO: Move the creation of folders into a context manager if python3 support only (TBD with launchpadlib)
    #Other cases will trigger an exception it's just to remove common cases...
    # (To be improved later when I have access to that lib)
    if not states or len(states) == 0:
        raise ValueError("States must be a non-empty list")

    cache_folder = tempfile.mkdtemp()
    # If many tasks have to be done with one login, maybe we should implement a context manager, and/or
    # move this outside the function.
    launchpad = Launchpad.login_anonymously('osa_toolkit', 'production', cache_folder, version='devel')
    lp_project =  launchpad.projects[project]
    bugs = lp_project.searchTasks(status=states, order_by=order_by)
    shutil.rmtree(cache_folder)
    return bugs

def display_for_triage(bugs):
    """ OSA bugtriage's etherpad has a specific format, print like that
    """
    # bug title is like:
    # '
    # Bug #1724025 in openstack-ansible:
    # invalid regular expression..."
    # '
    for bug in bugs:
        bug_name = u"".join(bug.title.split(":")[1:])
        print(u"#link {link}\n\t{name}".format(link=bug.web_link, name=bug_name))
                                                             