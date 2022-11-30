def test(text):
    result = []
    for word in text:
        if len(result) == 0 or result[-1] != word:
            result.append(word)
    return ''.join(result)




print(test("Heeyyy   yyouuuu!!!"))
print(test("SSSSsssshhhh"))
print(test("ppyyyyythhhhhooonnnnn"))




