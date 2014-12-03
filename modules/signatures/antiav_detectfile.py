# Copyright (C) 2014 Accuvant, Inc. (bspengler@accuvant.com)
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

from lib.cuckoo.common.abstracts import Signature
import re

class AntiAVDetectFile(Signature):
    name = "antiav_detectfile"
    description = "Attempts to identify installed AV products by installation directory"
    severity = 3
    categories = ["anti-av"]
    authors = ["Accuvant"]
    minimum = "1.2"

    def run(self):
        file_indicators = [
            ".*\\\\AVAST\\ Software$",
            ".*\\\\Avira\\ GmbH$",
            ".*\\\\Avira$",
            ".*\\\\Kaspersky\\ Lab$",
            ".*\\\\Kaspersky\\ Lab\\ Setup\\ Files$",
            ".*\\\\DrWeb$",
            ".*\\\\Norton\\ AntiVirus$",
            ".*\\\\ESET$",
            ".*\\\\Agnitum$",
            ".*\\\\Panda\\ Security$",
            ".*\\\\McAfee$",
            ".*\\\\McAfee\.com$",
            ".*\\\\Trend\\ Micro$",
            ".*\\\\BitDefender$",
            ".*\\\\ArcaBit$",
            ".*\\\\Online\\ Solutions$",
            ".*\\\\AnVir\\ Task\\ Manager$",
            ".*\\\\Alwil\\ Software$",
            ".*\\\\Symantec$",
            ".*\\\\AVG$",
            ".*\\\\Xore$",
            ".*\\\\Symantec\\ Shared$",
            ".*\\\\a-squared\\ Anti-Malware$",
            ".*\\\\a-squared\\ HiJackFree$",
            ".*\\\\avg8$",
            ".*\\\\Doctor\\ Web$",
            ".*\\\\f-secure$",
            ".*\\\\F-Secure\\ Internet\\ Security$",
            ".*\\\\G\\ DATA$",
            ".*\\\\P\\ Tools$",
            ".*\\\\P\\ Tools\\ Internet\\ Security$",
            ".*\\\\K7\\ omputing$",
            ".*\\\\Vba32$",
            ".*\\\\Sunbelt\\ Software$",
            ".*\\\\FRISK\\ Software$",
            ".*\\\\Security\\ Task\\ Manager$",
            ".*\\\\Zillya\\ Antivirus$",
            ".*\\\\Spyware\\ Terminator$",
            ".*\\\\Lavasoft$",
            ".*\\\\BlockPost$",
            ".*\\\\DefenseWall\\ HIPS$",
            ".*\\\\DefenseWall$",
            ".*\\\\Microsoft\\ Antimalware$",
            ".*\\\\Microsoft\\ Security\\ Essentials$",
            ".*\\\\Sandboxie$",
            ".*\\\\Positive\\ Technologies$",
            ".*\\\\UAenter$",
            ".*\\\\Malwarebytes$",
            ".*\\\\Malwarebytes'\\ Anti-Malware$",
            ".*\\\\Microsoft\\ Security\\ Client$",
        ]
        found = False
        for indicator in file_indicators:
            file_match = self.check_file(pattern=indicator, regex=True, all=True)
            if file_match:
                for match in file_match:
                    self.data.append({"file" : match })
                found = True
        return found