import sys
import os
import string
import shutil
import optparse
import textwrap

def pyramid_starter_seed_clone():
    description = """\
    Print the deployment settings for a Pyramid application.  Example:
    'show_settings deployment.ini'
    """
    usage = "usage: pyramid_starter_seed_clone new_package_name"
    parser = optparse.OptionParser(
        usage=usage,
        description=textwrap.dedent(description)
        )

    options, args = parser.parse_args(sys.argv[1:])
    if not len(args) == 1:
        print('You must provide at least one argument')
        return 2

    _translate(args[0])


def _translate(new_package_name, original_package_name='pyramid_starter_seed'):
    """ Translate package """

    def package_split(package_name, separator='.'):
        """ With 'pippo.pluto.paperino' you'll get:
            ['pippo.pluto.paperino','pippo.pluto', 'pippo', 'pluto', 'paperino']
        """
        items = package_name.split('.')
        len_items = len(items)
        results = [package_name, items[-1].capitalize()]
    
        for count in range(1, len_items-1):
            el = items[:-count]
            if el:
                results.append('.'.join(el))   
        results.extend(items)
        return results
    
    
    # copy tree
    shutil.copytree(original_package_name, new_package_name, ignore=shutil.ignore_patterns('*.pyc', 'svn*', 'tmp*', '.git', 'node_modules'))
    
    original_slices = package_split(original_package_name)
    new_slices = package_split(new_package_name)
    trans_map = zip(original_slices, new_slices)
    for step in os.walk(top=new_package_name, topdown=False):
        item_path = step[0]
        item_dir_paths = step[1]
        item_file_paths = step[2]
        print item_path, item_dir_paths, item_file_paths
    
        for item_file_path in item_file_paths:
            # read the file and substitute patterns
            file_to_filter = open(os.path.join(item_path, item_file_path), 'r')
            file_contents = file_to_filter.read()
            file_to_filter.close()
            # translate file
            for trans in trans_map:
                old = trans[0]
                new = trans[1]
                file_contents = string.replace(file_contents, old, new) 
                file_contents = string.replace(file_contents, old.capitalize(), new.capitalize()) 
            # write translated version of file
            # TODO: use with
            file_to_filter = open(os.path.join(item_path, item_file_path), 'w')
            file_to_filter.write(file_contents)
    
            for trans in trans_map: 
                old = trans[0]
                new = trans[1]
                if old in item_file_path:
                    old_path = item_file_path
                    new_path = string.replace(old_path, old, new)
                    os.rename(os.path.join(item_path, old_path), os.path.join(item_path, new_path))
                    break
                    
        for item_dir_path in item_dir_paths:
            for trans in trans_map: 
                old = trans[0]
                new = trans[1]
                if old in item_dir_path:
                    old_path = item_dir_path
                    new_path = string.replace(old_path, old, new)
                    os.rename(os.path.join(item_path, old_path), os.path.join(item_path, new_path))
                    break
    
