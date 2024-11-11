from models.count_words import CountWords
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_only_non_alpha():
	words = CountWords().count("!!!")
	assert words == 0

def test_word_ending_with_s():
	words = CountWords().count("dogs")
	assert words == 1

def test_word_ending_with_s_and_space():
	words = CountWords().count("dogs ")
	assert words == 1

def test_word_ending_with_r():
	words = CountWords().count("car")
	assert words == 1

def test_word_ending_with_r_and_space():
	words = CountWords().count("car ")
	assert words == 1

def test_word_ending_with_t():
	words = CountWords().count("cat")
	assert words == 0

def test_word_ending_with_t_and_space():
	words = CountWords().count("cat ")
	assert words == 0

def test_non_alpha_characters():
	words = CountWords().count("dogs, cats.")
	assert words == 2

def test_non_alpha_characters_finish_with_r():
	words = CountWords().count("dogs, car.")
	assert words == 2

def test_no_words_at_all():
	words = CountWords().count("caR cat")
	assert words == 0

def test_empty_string():
	words = CountWords().count("")
	assert words == 0