from django import template
from django.template.defaultfilters import stringfilter
import logging

register=template.Library()

@register.filter(name='pretty_checkbox')
@stringfilter
def pretty_checkbox(value):
    # Iterate over the HTML fragment, extract <label> and <input> tags, and
    # switch the order of the pairs where the input type is "checkbox".
    scratch = value
    output = ''
    try:
        while True:
            ls = scratch.find('<label')
            if ls > -1:
                le = scratch.find('</label>')
                ins = scratch.find('<input')
                ine = scratch.find('/>', ins)
                # Check whether we're dealing with a checkbox:
                if scratch[ins:ine+2].find(' type="checkbox" ')>-1:
                    # Switch the tags
                    output += scratch[:ls]
                    output += scratch[ins:ine+2]
                    output += scratch[ls:le-1]+scratch[le:le+8]
                else:
                    output += scratch[:ine+2]
                scratch = scratch[ine+2:]
            else:
                output += scratch
                break
    except:
        logging.error("pretty_checkbox caught an exception")
    return output