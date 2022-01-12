"""Check for FIXMEs or TODOs and emit info messages"""

import re
import tokenize

from pylint.checkers import BaseChecker
from pylint.interfaces import ITokenChecker
from pylint.utils.pragma_parser import OPTION_PO, PragmaParserError, parse_pragma

class FixmeChecker(BaseChecker):
    """Checks for fixmes"""

    __implements__ = ITokenChecker
    _fixme_pattern: re.Pattern

    name = 'fixme-info'
    priority = -1
    msgs = {
        'I1511': (
            '%s',
            'fixme-info',
            'Used when a warning note as FIXME or XXX is detected.'
        ),
    }
    options = (
        (
            'notes-info',
            {
                'type': 'csv',
                'metavar': '<comma separated values>',
                'default': ('FIXME', 'XXX', 'TODO'),
                'help': (
                    'List of note tags to take in consideration, '
                    'separated by a comma.'
                ),
            },
        ),
        (
            'notes-info-rgx',
            {
                'type': 'string',
                'metavar': '<regexp>',
                'help': 'Regular expression of note tags to take in consideration.',
            },
        ),
    )

    def open(self):
        super().open()

        notes = '|'.join(map(re.escape, self.config.notes_info))
        if self.config.notes_info_rgx:
            regex_string = fr'#\s*({notes}|{self.config.notes_info_rgx})\b'
        else:
            regex_string = fr'#\s*({notes})\b'

        self._fixme_pattern = re.compile(regex_string, re.I)

    def process_tokens(self, tokens):
        """inspect the source to find fixme problems"""
        if not self.config.notes_info:
            return
        comments = (
            token_info for token_info in tokens if token_info.type == tokenize.COMMENT
        )
        for comment in comments:
            comment_text = comment.string[1:].lstrip()  # trim '#' and whitespaces

            # handle pylint disable clauses
            disable_option_match = OPTION_PO.search(comment_text)
            if disable_option_match:
                try:
                    values = []
                    try:
                        for pragma_repr in (
                            p_rep
                            for p_rep in parse_pragma(disable_option_match.group(2))
                            if p_rep.action == 'disable'
                        ):
                            values.extend(pragma_repr.messages)
                    except PragmaParserError:
                        # Printing useful information dealing with this error
                        # is done in the lint package
                        pass
                    if set(values) & set(self.config.notes_info):
                        continue
                except ValueError:
                    self.add_message(
                        'bad-inline-option',
                        args=disable_option_match.group(1).strip(),
                        line=comment.start[0],
                    )
                    continue

            # emit warnings if necessary
            match = self._fixme_pattern.search('#' + comment_text.lower())
            if match:
                self.add_message(
                    'fixme-info',
                    col_offset=comment.start[1] + 1,
                    args=comment_text,
                    line=comment.start[0],
                )


def register(linter):
    """required method to auto register this checker"""
    linter.register_checker(FixmeChecker(linter))
