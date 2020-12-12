import urllib.request

from matcher.matcher import Matcher


class Analyzer:
    def __init__(self, text_to_analyze, part_length, num_of_threads):
        self.text_to_analyze = text_to_analyze
        self.part_length = part_length
        self.num_of_threads = num_of_threads
        self.list_of_matchers = []
        self.words_to_look_for = set(line.strip() for line in open("../resources/words_to_search.txt"))

    def analyze(self):
        # read the Huge text, and after each 1000 lines create matcher with this part of text and add to the list
        self.read_file_and_create_matchers()

        # execute the thread pool with all the matchers
        print(len(self.list_of_matchers))
        self.list_of_matchers[0].find_matches()

        for key in self.list_of_matchers[0].word_to_locations.keys():
            print(key, '->', self.list_of_matchers[0].word_to_locations[key].to_string())


        # execute the aggregator with the list of the matchers

    def read_file_and_create_matchers(self):
        counter = 1
        part = []

        for line in urllib.request.urlopen("http://norvig.com/big.txt"):
            part.append(line.decode('utf-8'))
            if counter % 1000 == 0:
                # Think to execute the mathcer in seperate thread here ! add to thread pool
                self.create_new_matcher(part)
                part = []
                break
            counter += 1

        # if we have "extra" rows create new and last matcher
        if counter % 1000 != 0:
            self.create_new_matcher(part)

    def create_new_matcher(self, part, starting_line=0, starting_char=0):
        new_matcher = Matcher(part, self.words_to_look_for, starting_line, starting_char)
        self.list_of_matchers.append(new_matcher)


'''
private static final String s_UrlAddress = "http://norvig.com/big.txt";
	private static final int s_PartLength = 1000;
	private static final int s_SumOfThreads = 5;
	private int m_LineCounter = 0;
	private int m_PreviousLineCounter = 0;
	private int m_TotalCharsCounter = 0;
	private int m_PreviosCharCounter = 0;
	private Agregator m_Agregator;
	private List<Matcher> m_AllMatchers;
'''
