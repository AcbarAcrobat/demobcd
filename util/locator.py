from lxml import etree
from cssselect import GenericTranslator, SelectorError


class Locator:

    minimal_xml = '<!DOCTYPE _[<!ELEMENT _ EMPTY>]><_/>'

    def contains(self, element, text):
        return '{}[{}]'.format(
            self.to_xpath(element),
            "contains(., %s)" % GenericTranslator().xpath_literal(text)
        )

    def to_xpath(self, selector):
        try:
            return GenericTranslator().css_to_xpath(selector)
        except SelectorError:
            if self.is_xpath(selector):
                return selector
        return None

    def is_xpath(self, selector):
        doc = etree.XML(self.minimal_xml)
        try:
            doc.xpath(selector)
        except etree.XPathEvalError:
            return False
        return True
