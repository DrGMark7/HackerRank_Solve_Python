import textwrap

def wrap(string, max_width):
    result = ""
    text = string
    Const = max_width
    
    for i,j in zip(range(0,len(text),Const),range(Const,len(text)+Const,Const)):
        
        result += f"{text[i:j]}\n"
    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)