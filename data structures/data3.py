try:
    with open ("file3.txt") as f:
        lines = f.readlines()
        word_c = { }
        #cline = len(lines)
        for line in lines:
            words = line.split(" ")
            for word in words:
                word= word.strip("\n")
                #word = word.upper()
                word = word.split(" ")
                word = word.replace(',','')
                word  = word.replace('.','')
                try:
                    word_c[dict]+=1
                except KeyError:
                    word_c[word] =1
        print(word_c)
except Exception as a:
            print(f"file not found :{a}")