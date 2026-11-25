import xml.etree.ElementTree as ET
import logging
import sys

data = ET.parse("ideas_for_test/work_with_xml/groups.xml")
groups = data.findall("group")

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    stream=sys.stdout)

logger = logging.getLogger("xml_logger")

def finding_coming(number_value):
    for item in groups:
        number = item.find("number")
        incoming = item.find("timingExbytes/incoming")

        if number.text == str(number_value):
            if incoming is not None:
                return incoming.text
            else:
                return None

    return None

number = 3
data = finding_coming(number)
logger.info(f"Group {number}: {data}")