import random, argparse, json

def main():
    parser = argparse.ArgumentParser(
        description='Create a random sample of sentences from scenarios')
    parser.add_argument('in_file', type=str,
                        help='the file containing the sentences.')
    parser.add_argument('out_file', type=str,
                        help='the file to contain the random sample.')
    args = parser.parse_args()

    # read the sentences
    sentences = json.load(open(args.in_file))
    print(len(sentences))
    
    # sample the sentences
    sample = random.sample(sentences, 100)
    
    # write the sample
    json.dump(sample, open(args.out_file, 'w'))
    
if __name__ == "__main__":
    main()
