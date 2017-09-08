"""
Boilerplate
Created 09/07/17/PP


Modified MM/DD/YY/NN
Description of what was modified.


Long live the boilerplate - phone book of version control.
"""

import xmltodict
import BeautifulSoup


if __name__ == "__main__":
    print "HTMLManagment.py run as %s." % __name__

    # filename = "PM2 Kraft HD to LD_files\\bindings.xml"
    filename = "PM2 Kraft HD to LD.htm"

    invalid_xml_char_swap = {
        # "<" : "&lt;",
        # ">" : "&gt;",
        # "\"" : "&quot;",
        "\'" : "&apos;",
        "&" : "&amp;"
    }
    invalid_xml_chars = []
    for k, v in invalid_xml_char_swap.iteritems():
        invalid_xml_chars.append(k)

    with open(filename) as fd:
        text = fd.read()
    x = 0
    while x < len(text):
        if text[x] in invalid_xml_chars:
            # print text[x]
            text = text[:x] + invalid_xml_char_swap[text[x]] + text[(x+1):]
        x = x + 1

    # text = "<?xml version = '1.0' encoding='iso-8859-1'?>" + text
    # doc = xmltodict.parse(text)
    soup = BeautifulSoup.BeautifulSoup(text)
    print soup.prettify()

    print "Hello World"
