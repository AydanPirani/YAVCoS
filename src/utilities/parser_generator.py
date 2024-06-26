import argparse

import commands.commit as commit
import commands.revert as revert
import commands.track as track

from .action_factory import ActionFactory
# import action_factory

class ParserGenerator:
    parser = argparse.ArgumentParser(description="Yet Another Version Control System")
    subparsers = parser.add_subparsers(title="Commands", dest="command")
    subparsers.required = True

    def __init__(self):
        self.commit_parser()
        self.revert_parser()
        self.track_parser()

    def commit_parser(self):
        parser = self.subparsers.add_parser('snap', help='Create a snapshot')
        parser.set_defaults(func=commit.execute)

    def revert_parser(self):
        parser = self.subparsers.add_parser('revert', help='Revert to a snapshot')
        parser.add_argument('hash', type=str, help='The hash of the snapshot to revert to')
        parser.set_defaults(func=revert.execute)

    def track_parser(self):
        parser = self.subparsers.add_parser('track', help='Track a file/dir')
        trackAction = ActionFactory.init_class(track.validate)
        parser.add_argument('path', type=str, help='File/dir to track', action=trackAction)
        parser.set_defaults(func=track.execute)

    def get_parser(self):
        return self.parser

    def get_args(self):
        return self.parser.parse_args()