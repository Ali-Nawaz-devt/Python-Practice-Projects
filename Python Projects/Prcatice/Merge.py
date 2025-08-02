def merge_the_tools(string, k):
    sub_strings = []
    sub_ = ''

    for i in string:
        sub_ += i
        if len(sub_) == k:
            sub_strings.append(sub_)
            sub_ = ''
    
    # Append last part if not empty (in case string isn't divisible by k)
    if sub_:
        sub_strings.append(sub_)

     # For debugging

    for sub in sub_strings:
        result = ''
        for i in sub:
            if i not in result:
                result += i
        print(result)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
