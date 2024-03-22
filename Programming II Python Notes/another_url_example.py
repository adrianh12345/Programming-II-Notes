def is_valid_url(url):
    # Check whether the URL begins with https:// or http://.
    http_prefix = "http://"
    https_prefix = "https://"
    is_http = True
    is_https = True

    # Check the http:// prefix manually
    for i in range(len(http_prefix)):
        if i >= len(url) or url[i] != http_prefix[i]:
            is_http = False
            break

    # If the prefix isn't http://, manually check for https://
    if not is_http:
        for i in range(len(https_prefix)):
            if i >= len(url) or url[i] != https_prefix[i]:
                is_https = False
                break

    # Return False if neither http:// nor https:// can be found.
    if not is_http and not is_https:
        return False

    # Look for a dot to represent a domain in the remaining portion of the URL.
    dot_found = False
    for char in url[len(http_prefix):]:  # Check after the prefix.
        if char == '.':
            dot_found = True
            break

    return dot_found


# Example usage:
print(is_valid_url("http://www.example.com"))  # Expected True
print(is_valid_url("https://example"))  # Expected False
print(is_valid_url("www.example.com"))  # Expected False
