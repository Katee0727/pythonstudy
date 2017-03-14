import ex26 

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

#No12 - adding ':'
def print_first_word(words):
    """Prints the first word after popping it off."""
    #No1 - changing 'poop' to 'pop'
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    #No2 - adding ')'
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    #No3 - changing 'sort_sentence' to 'sort_words'
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 5
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    #No4 - changing '\' to '/'
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
#No5 - delete duplcate '=' and changing '-' to'_'
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
#No6 - changing 'start_pont' to 'start_point'
print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point)

sentence = "All god things come to those who weight."
#No14 - changing name from ex25' to 'ex26'
words = ex26.break_words(sentence)
#No15 changing name from ex25' to 'ex26'
sorted_words = ex26.sort_words(words)

print_first_word(words)
print_last_word(words)
#No7 - deleting '.'
print_first_word(sorted_words)
print_last_word(sorted_words)
#No8 -changing 'sort_sentence' to 'sort_words'
#No16 changing name from ex25' to 'ex26'
#No17 - changing 'sentence' to 'words'
sorted_words = ex26.sort_sentence(sentence)
#No9 - chaning 'prin' to 'print"
print sorted_words

#No10 - changing 'print_irst_and_last' to "print_first_and_last"
print_first_and_last(sentence)

#No11 - changing 'print_first_a_last_sorted" to "print_first_and_last_sorted" and 'senence' to 'sentence'

#13 - unexpected indent, fixing it.
print_first_and_last_sorted(sentence)
