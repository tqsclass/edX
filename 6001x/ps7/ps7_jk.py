# 6.00.1x Problem Set 7
# RSS Feed Filter

import feedparser
import string
import time
from project_util import translate_html
from Tkinter import *


#-----------------------------------------------------------------------
#
# Problem Set 7

#======================
# Code for retrieving and parsing RSS feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        summary = translate_html(entry.summary)
        try:
            subject = translate_html(entry.tags[0]['term'])
        except AttributeError:
            subject = ""
        newsStory = NewsStory(guid, title, subject, summary, link)
        ret.append(newsStory)
    return ret
#======================

#======================
# Part 1
# Data structure design
#======================

# Problem 1

# TODO: NewsStory
class NewsStory(object):
    def __init__(self,Guid,Title,Subject,Summary,Link):
        self.guid = Guid
        self.title = Title
        self.subject = Subject
        self.summary = Summary
        self.link = Link

    def getGuid(self):
        return self.guid
    
    def getTitle(self):
        return self.title

    def getSubject(self):
        return self.subject

    def getSummary(self):
        return self.summary

    def getLink(self):
        return self.link
    
testns = NewsStory('foo', 'my title is of Thee', 'mySubject', 'some long summary', 'www.example.com')
#======================
# Part 2
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

# Whole Word Triggers
# Problems 2-5
import string
class WordTrigger(Trigger):
    def __init__(self,Word):
        self.word = Word.lower()
        
    def isWordIn(self, text):
        parsed = text.lower()  # check mutation
        for letter in string.punctuation:
            parsed = parsed.replace(letter,' ') # replace all
        words = parsed.split(' ')
        #print words
        if self.word in words:
            return True
        else:
            return False

class TitleTrigger(WordTrigger):
    
    def evaluate(self,news):
        #print type(news), news.getTitle(), news.getTitle().lower()
        #print self.word, news.getTitle().lower()
        return self.isWordIn(news.getTitle().lower())


class SubjectTrigger(WordTrigger):

    def evaluate(self,news):
        return self.isWordIn(news.getSubject().lower())


class SummaryTrigger(WordTrigger):

    def evaluate(self,news):
        return self.isWordIn(news.getSummary().lower())
        

class NotTrigger(Trigger):
    def __init__(self,Trigger):
        self.trigger = Trigger
        
    def evaluate(self, news):
        return not self.trigger.evaluate(news)

class AndTrigger(Trigger):
    def __init__(self,Trigger1,Trigger2):
        self.trigger1 = Trigger1
        self.trigger2 = Trigger2

    def evaluate(self, news):
        return self.trigger1.evaluate(news) and self.trigger2.evaluate(news)

class OrTrigger(Trigger):
    def __init__(self,Trigger1,Trigger2):
        self.trigger1 = Trigger1
        self.trigger2 = Trigger2

    def evaluate(self, news):
        return self.trigger1.evaluate(news) or self.trigger2.evaluate(news)

class PhraseTrigger(Trigger):
    def __init__(self,Phrase):
        self.phrase = Phrase

    def isWordIn(self, text):
        if self.phrase in text:
            return True
        else:
            return False
        
    def evaluate(self,news):
        return self.isWordIn(news.getTitle()) or self.isWordIn(news.getSubject()) or self.isWordIn(news.getSummary())
    

testns = NewsStory('foo', 'Winter in Boston!', 'mySubject', 'some long summary', 'www.example.com')



#wt = WordTrigger('ocks')
#print wt.isWordIn('Abba rocks ocks ocks\' \'ocks the world!')
#print wt.isWordIn('Abba rules the world!')

tt = TitleTrigger('Boston')
st = SummaryTrigger('thee')

print tt.evaluate(testns)
print st.evaluate(testns)


# TODO: WordTrigger

# TODO: TitleTrigger
# TODO: SubjectTrigger
# TODO: SummaryTrigger


# Composite Triggers
# Problems 6-8

# TODO: NotTrigger
# TODO: AndTrigger
# TODO: OrTrigger


# Phrase Trigger
# Question 9

# TODO: PhraseTrigger


#======================
# Part 3
# Filtering
#======================

def filterStories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder (we're just returning all the stories, with no filtering
    keepers = []    # list of stories to keep
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                keepers.append(story)
                break
            #else we continue
    
    return keepers

#======================
# Part 4
# User-Specified Triggers
#======================

def makeTrigger(triggerMap, triggerType, params, name):
    """
    Takes in a map of names to trigger instance, the type of trigger to make,
    and the list of parameters to the constructor, and adds a new trigger
    to the trigger map dictionary.

    triggerMap: dictionary with names as keys (strings) and triggers as values
    triggerType: string indicating the type of trigger to make (ex: "TITLE")
    params: list of strings with the inputs to the trigger constructor (ex: ["world"])
    name: a string representing the name of the new trigger (ex: "t1")

    Modifies triggerMap, adding a new key-value pair for this trigger.

    Returns a new instance of a trigger (ex: TitleTrigger, AndTrigger).
    """
    # TODO: Problem 11
    customTrigger = ''
    if triggerType == 'SUBJECT':
        customTrigger = SubjectTrigger(params[0])
    elif triggerType == 'TITLE':
        customTrigger = TitleTrigger(params[0])
    elif triggerType == 'SUMMARY':
        customTrigger = SummaryTrigger(params[0])
    elif triggerType == 'AND':
        trigger1 = triggerMap[params[0]]
        trigger2 = triggerMap[params[1]]
        customTrigger = AndTrigger(trigger1,trigger2)
    elif triggerType == 'OR':
        trigger1 = triggerMap[params[0]]
        trigger2 = triggerMap[params[1]]
        customTrigger = OrTrigger(trigger1,trigger2)
    elif triggerType == 'NOT':
        customTrigger = NotTrigger(triggerMap[params[0]])
    elif triggerType == 'PHRASE':
        phrase = ''
        for word in params:
            phrase = phrase + word + ' '
        customTrigger = PhraseTrigger(phrase.strip())
            
    triggerMap[name] = customTrigger
    return customTrigger


def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename
    """

    # Here's some code that we give you
    # to read in the file and eliminate
    # blank lines and comments
    triggerfile = open(filename, "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)

    triggers = []
    triggerMap = {}

    # Be sure you understand this code - we've written it for you,
    # but it's code you should be able to write yourself
    for line in lines:

        linesplit = line.split(" ")

        # Making a new trigger
        if linesplit[0] != "ADD":
            trigger = makeTrigger(triggerMap, linesplit[1],
                                  linesplit[2:], linesplit[0])

        # Add the triggers to the list
        else:
            for name in linesplit[1:]:
                triggers.append(triggerMap[name])

    return triggers
    
import thread

SLEEPTIME = 60 #seconds -- how often we poll


def main_thread(master):
    # A sample trigger list - you'll replace
    # this with something more configurable in Problem 11
    try:
        # These will probably generate a few hits...
        t1 = TitleTrigger("Obama")
        t2 = SubjectTrigger("Romney")
        t3 = PhraseTrigger("Election")
        t4 = OrTrigger(t2, t3)
        triggerlist = [t1, t4]
        
        # TODO: Problem 11
        # After implementing makeTrigger, uncomment the line below:
        # triggerlist = readTriggerConfig("triggers.txt")

        # **** from here down is about drawing ****
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)
        
        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)

        # Gather stories
        guidShown = []
        def get_cont(newstory):
            if newstory.getGuid() not in guidShown:
                cont.insert(END, newstory.getTitle()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.getSummary())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.getGuid())

        while True:

            print "Polling . . .",
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))

            # Process the stories
            stories = filterStories(stories, triggerlist)

            map(get_cont, stories)
            scrollbar.config(command=cont.yview)


            print "Sleeping..."
            time.sleep(SLEEPTIME)

    except Exception as e:
        print e


if __name__ == '__main__':

    root = Tk()
    root.title("Some RSS parser")
    thread.start_new_thread(main_thread, (root,))
    root.mainloop()

