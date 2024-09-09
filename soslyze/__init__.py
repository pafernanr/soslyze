import argparse
import os
from pathlib import Path
import re
from soslyze.plugins.discovery import Discovery
from soslyze.plugins.insights import Insights
from soslyze.plugins.os import Rhel8, Rhel7
from soslyze.plugins.package_manager import Dnf, Yum
from soslyze.plugins.rhui import Rhui
from soslyze.plugins.satellite import Satellite
from soslyze.plugins.subscription_manager import SubscriptionManager
from soslyze.utils import package_present


class SoSLyze:

    def valid_path(self, path):
        if os.path.exists(path + '/sos_reports'):
            return path
        else:
            raise argparse.ArgumentTypeError(
                f"'{path}' is not a valid sosreport path.\n"
            )

    def __init__(self):
        """
        Initialization of SoSLyze
        """
        self.parser = argparse.ArgumentParser(
            description="Summarize SysMgmt/Subscription Management/Insights "
                        + "data from an extracted sosreport archive."
            )
        self.parser.add_argument(
            'path',
            help='Path to sosreport. Default: `./`.',
            default=os.getcwd(),
            type=self.valid_path,
            nargs='?'
            )
        self.args = self.parser.parse_args()

        if len(re.findall('8[.]', Path(
                self.args.path + '/etc/redhat-release').read_text())) == 1 or \
                len(re.findall('9[.]', Path(
                    self.args.path + '/etc/redhat-release').read_text())) == 1:
            self.os = Rhel8(self.args.path)
        elif len(re.findall('6[.]', Path(
                self.args.path + '/etc/redhat-release').read_text())) == 1 or \
                len(re.findall('7[.]', Path(
                    self.args.path + '/etc/redhat-release').read_text())) == 1:
            self.os = Rhel7(self.args.path)

        if package_present(self.args.path, "dnf"):
            self.package_manager = Dnf(self.args.path)
        elif package_present(self.args.path, "yum"):
            self.package_manager = Yum(self.args.path)
        if package_present(self.args.path, "subscription-manager"):
            self.subscription_manager = SubscriptionManager(self.args.path)
        if package_present(self.args.path, "insights-client"):
            self.insights = Insights(self.args.path)
        if package_present(self.args.path, "satellite"):
            self.satellite = Satellite(self.args.path)
        if os.path.isfile(self.args.path + "/etc/rhui/rhui-tools.conf"):
            self.rhui = Rhui(self.args.path)
        if os.path.isdir(self.args.path + "/sos_commands/discovery"):
            self.discovery = Discovery(self.args.path)

    def output(self):
        self.os.output()

        if hasattr(self, "subscription_manager"):
            self.subscription_manager.output()

        if hasattr(self, "package_manager"):
            self.package_manager.output()

        if hasattr(self, "insights"):
            self.insights.output()

        if hasattr(self, "satellite"):
            self.satellite.output()

        if hasattr(self, "rhui"):
            self.rhui.output()

        if hasattr(self, "discovery"):
            self.discovery.output()


SoSLyze().output()
