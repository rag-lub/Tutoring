

def word_match(word, wordLst):
        for i in range(len(wordLst)):
                if wordLst[i]==word:
                        return word
                if wordLst[i][1:] == word or wordLst[i][:-1] == word:
                        return wordLst[i]
                elif len(word)==len(wordLst[i]):
                    mismatch=0
                    for j in range(len(word)):
                        print(j,word[j],wordLst[i][j])
                        if word[j]!=wordLst[i][j]:
                            mismatch = mismatch + 1
                    if mismatch < 2:
                        return wordLst[i]
                    
        return None
def popular_names(nameLst):
    resultsLst = []
    occurances = 0
    for name in nameLst:
        if nameLst.count(name)>occurances:
            occurances=nameLst.count(name)
            resultsLst.clear()
            resultsLst.append(name)
        elif nameLst.count(name)==occurances and name not in resultsLst:
            resultsLst.append(name)
    return resultsLst
            
def adding_pairs2(lst):
    lst.sort(reverse=True)
    if len(lst)>1:
        return lst[0]+lst[1]
    else:
        return None
def adding_pairs(lst):
        sorted_lst = sorted(lst)
        largest_num = sorted_lst[-1]
        second_num = sorted_lst[-2]
        return largest_num + second_num    
            
                        
print(adding_pairs([4,2,2,5]))
