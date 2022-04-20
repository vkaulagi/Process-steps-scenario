import json
from termcolor import colored

def tagging(tags, bstep, istep, o):
    break_out_flag = False
    for sentences in tags:
        for tuples in sentences:
            if tuples[1] == "VERB" and len(tuples) == 2:

                l1 = tuples[0]
                text = sentences[0][0]

                for i in range(1,len(sentences)):
                        text += " "
                        text += sentences[i][0] 
                result = " ".join(colored(t,'white','on_red') if t in l1 else t for t in text.lower().split())
                print(result)

                num = input('Enter num: ')
                print(type(num))
                if num == "1":
                    #tuples += bstep
                    #tuples = tuples + ["B-STEP"]
                    tuples.append('B-STEP')
                    print(tuples)
                elif num == "2":
                    #tuples += istep
                    #tuples = tuples + ["I-STEP"]
                    tuples.append('I-STEP')
                elif num == "3":
                    #tuples += o
                    #tuples = tuples + ["O"]
                    tuples.append('O')
                    print(tuples)
                elif num == "0":
                    break_out_flag = True
                    break

        if break_out_flag:
            break

    print(tags[0])
                
    return tags

def main():
    f = open('tags.json')
    tags = json.load(f)

    bstep = ("B-STEP",)
    istep = ("I-STEP",)
    o = ("O",)

    #print(tags[0][8])
    tags = tagging(tags, bstep, istep, o)

    with open('tags.json', 'w') as f:
        json.dump(tags, f)

if __name__ == "__main__":
    main()

                