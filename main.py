from cryptography import file


test = file("The quick brown fox jumped over the lazy dog")

print(test.plain_text)