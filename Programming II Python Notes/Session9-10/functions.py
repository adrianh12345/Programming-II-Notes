http_scheme = "http://"
https_scheme = "https://"

def is_valid_url(url):
    # Assume for the moment that https and http are different.
    scheme_matched = False
    dot_found = False

    # Manually verify whether the prefix is https:// or http://.
    if url[:7] == http_scheme or url[:8] == https_scheme:
        scheme_matched = True

    # To see if the scheme matched, look for a dot in the remaining area of the URL.
    if scheme_matched:
        for i in range(scheme_length, len(url)):  # Begin examining following the plan
            if url[i] == '.':
                dot_found = True
                break  # Close the loop after a dot has been located.

    return scheme_matched and dot_found

# Example usage:
print(is_valid_url("http://www.example.com"))  # Expected to return True
print(is_valid_url("https://example"))         # Expected to return False
print(is_valid_url("www.example.com"))         # Expected to return False