
#I adda flag for check the sentence is added or not
sentence_added = False

# open the file and read it
with open("demofile_forWrite2.txt", "r") as f:
    content = f.read()
    if "Now the file has more content!" not in content:
        # Add the sentence
        with open("demofile_forWrite2.txt", "a") as f:
            f.write("Now the file has more content!\n")
            # After sentence is added change the flag
            sentence_added = True


# read the file and read content is the sentence is added
if sentence_added:
    with open("demofile_forWrite2.txt", "r") as f:
        print(f.read())