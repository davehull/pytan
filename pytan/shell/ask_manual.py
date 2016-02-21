from . import base
from pytan.shellparser import ShellParser, add_arg_group
from pytan.constants import HANDLER_DEFAULTS, MANUAL_OPTS

class Worker(base.Base):
    DESCRIPTION = 'Ask a manual question and export the results to a file'
    GROUP_NAME = 'Manual Question Options'
    ACTION = 'question'
    QTYPE = 'manual'
    PREFIX = 'ask_manual'

    def setup(self):
        self.grp = self.parser.add_argument_group(self.GROUP_NAME)
        #for k, v in MANUAL_OPTS.items():
        #    add_arg_group(self.grp, k, v, HANDLER_DEFAULTS)
        #self.add_help_opts()
        #self.add_export_results_opts()
        #self.add_report_opts()


        #self.grp.add_argument(
        #    '-s', '--sensor',
        #    required=False, action='append', default=[], dest='sensors',
        #    help='Sensor, optionally describe parameters, options, and a filter'
        #)
        self.grp.add_argument(
            '-f', '--filter',
            required=False, action='append', default=[], dest='filters',
            help='Whole question filters, only return results for machines that match',
        )
        #self.grp.add_argument(
        #    '-o', '--option',
        #    required=False, action='append', default=[], dest='options',
        #    help='Whole question options, controls question filters',
        #)
        self.grp_choice_results()

    def get_question_response(self):
        grps = [self.GROUP_NAME]
        kwargs = self.get_parser_args(grps)
        m = "++ Asking {} question with arguments:\n{}"
        print m.format(self.QTYPE, self.pf(kwargs))
        response = self.handler.ask_manual(qtype=self.QTYPE, **kwargs)
        m = "++ Asked Question {question_object.query_text!r} ID: {question_results.id!r}"
        print m.format(**response)
        return response

    def get_result(self):
        response = self.get_question_response()
        report_file, result = self.export_results(response['question_results'])
        return response, report_file, result
