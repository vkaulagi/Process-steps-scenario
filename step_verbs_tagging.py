import json, argparse
from termcolor import colored

def tagging(tagged_sentences):
    verb_count = 0
    for words in tagged_sentences:
        for word in words:
            if word[1] == "VERB":
                verb_count += 1

    print('Total verbs to tag: %i' % verb_count)
    print('Tags: 1=B, 2=I, 3=O, 0=EXIT')
    
    verb_count = 0
    break_out_flag = False
    for words in tagged_sentences:
        for i in range(len(words)):
            # if this is not a verb, skip
            if words[i][1] != "VERB":
                continue

            verb_count += 1
            # if this verb is tagged, skip
            if len(words[i]) > 2:
                continue

            # highlight word in sentence
            word = words[i][0]
            result = " ".join(colored(words[j][0],'white','on_red') if j == i else words[j][0] for j in range(len(words)))
            print(result)

            num = input('Enter %i tag: ' % verb_count)
            if num == "1":
                words[i].append('B-STEP')
            elif num == "2":
                words[i].append('I-STEP')
            elif num == "3":
                words[i].append('O')
            elif num == "0":
                break_out_flag = True
                break

        if break_out_flag:
            break
        
    return tagged_sentences

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

    with open(args.tag_file, 'w') as f:
        json.dump(tags, f)

if __name__ == "__main__":
    main()

