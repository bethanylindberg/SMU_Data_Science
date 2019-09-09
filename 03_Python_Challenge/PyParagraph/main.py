#Import modules
import os

#Set path for txt files
filepath1 = os.path.join('..','Resources','paragraph1.txt')
filepath2 = os.path.join('..','Resources','paragraph2.txt')

def loadfile(filepath):
    """Helper function to read a file and return the data."""
    with open(filepath, "r") as resume_file_handler:
        return resume_file_handler.read().lower().split()

# Grab the text for paragraphs
paragraph1 = loadfile(filepath1)
paragraph2 = loadfile(filepath2)

#Approximate word count
wordcount1 = len(paragraph1)
wordcount2 = len(paragraph2)

#Approximate letter count per word
#Approximate sentence count
charspar1 = 0
charspar2 = 0
senpar1 = 1
senpar2 = 1
for word in paragraph1:
    charspar1 += (len(word)) #Counting characters per word for total in paragraph
    if word [-1] == "." or word[-1] == "!" or word[-1] == "?": #checking for end punctuation
        senpar1 += 1
for word in paragraph2:
    charspar2 += (len(word))
    if word [-1] == "." or word[-1] == "!" or word[-1] == "?":
        senpar2 += 1

#Divide characters by words to get approximate letters per word
par1lpw = round((charspar1/wordcount1),1)
par2lpw = round((charspar2/wordcount2),1)

#Divide word count by sentence count to find approximate sentence length in words
par1senlen = round((wordcount1/senpar1),1)
par2senlen = round((wordcount2/senpar2),1)

#Print terminal message
print("Paragraph Analysis (paragraph1.txt)")
print("------------------")
print(f"Approximate Word Count: {wordcount1}")
print(f"Approximate Sentence count: {senpar1}")
print(f"Average Letter Count: {par1lpw}")
print(f"Average Sentence Length: {par1senlen}")

print("\nParagraph Analysis (paragraph2.txt)")
print("------------------")
print(f"Approximate Word Count: {wordcount2}")
print(f"Approximate Sentence count: {senpar2}")
print(f"Average Letter Count: {par2lpw}")
print(f"Average Sentence Length: {par2senlen}")