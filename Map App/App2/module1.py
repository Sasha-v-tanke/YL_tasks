def get_size(organization):
    s = organization["properties"]["boundedBy"]
    return f"{abs(s[0][0] - s[1][0])},{abs(s[0][1] - s[1][1])}"
