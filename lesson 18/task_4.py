import re


def check_roman(your_string):
    """Searching for roman numbers in string."""
    regex = re.compile(r"""
    ^(IV|IX|X{0,2}V?I{0,3})-?
    (IV|IX|X{0,2}V?I{0,3})?
    (в|век|вв)$
    """, re.VERBOSE)
    if re.search(regex, your_string):
        result = re.search(regex, your_string)
        print(f"\n{result}")


check_roman("VIв")
check_roman("IXвек")
check_roman("XVI-XVIIвв")
check_roman("XX-XXIвв")
