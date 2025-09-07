import sys
import xml.etree.ElementTree as ET


def check_coverage():
    """Read the coverage report and check for untested Python classes.
    
    If any untested classes are found, print their names and exit with a non-zero status.

    """
    tree = ET.parse('coverage.xml')
    root = tree.getroot()
    untested_classes = []

    for cls in root.findall('.//class'):
        if cls.get('line-rate') == '0':
            untested_classes.append(cls.get('name'))

    if untested_classes:
        print("Untested classes found:", untested_classes)
        sys.exit(1)

    print("No untested classes found.")

if __name__ == "__main__":
    check_coverage()
