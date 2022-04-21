import json, argparse
from termcolor import colored

def tagging(tags):
    verb_count = 0
    for sentences in tags:
        for tuples in sentences:
            if tuples[1] == "VERB":
                verb_count += 1

    print('Total verbs to tag: %i' % verb_count)
    print('Tags: 1=B, 2=I, 3=O, 0=EXIT')
    
    verb_count = 0
    break_out_flag = False
    for sentences in tags:
        for tuples in sentences:
            # if this is not a verb, skip
            if tuples[1] != "VERB":
                continue

            verb_count += 1
            # if this verb is tagged, skip
            if len(tuples) > 2:
                continue

            
            l1 = tuples[0]
            text = sentences[0][0]

            for i in range(1,len(sentences)):
                text += " "
                text += sentences[i][0]

            # add word highlighting
            result = " ".join(colored(t,'white','on_red') if t in l1 else t for t in text.lower().split())
            print(result)

            num = input('Enter %i num: ' % verb_count)
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
    parser = argparse.ArgumentParser(
        description='Create interactive shell to code step verbs.')
    parser.add_argument('tag_file', type=str,
                        help='the file containing the tagged words.')
    args = parser.parse_args()

    # read the tag file
    f = open(args.tag_file)
    tags = json.load(f)

    #print(tags[0][8])
    tags = tagging(tags)

    with open('tags.json', 'w') as f:
        json.dump(tags, f)

if __name__ == "__main__":
    main()

