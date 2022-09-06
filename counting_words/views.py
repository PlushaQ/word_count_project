from django.http import HttpResponse
from django.shortcuts import render
from collections import Counter
from operator import itemgetter


def homepage(request):
    return render(request, 'homepage.html')


def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split(' ')
    fulltext_len = len(wordlist)

    word_dictionary = {}
    for word in wordlist:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    occurrence_counter = Counter(wordlist)
    most_frequent_word = occurrence_counter.most_common()[0][0]
    least_frequent_word = occurrence_counter.most_common()[-1][0]
    most_frequent_word_amount = occurrence_counter.most_common()[0][1]
    least_frequent_word_amount = occurrence_counter.most_common()[-1][1]

    info_about_text = {'fulltext': fulltext,
                       'fulltext_len': fulltext_len,
                       'most_frequent_word': most_frequent_word, 'least_frequent_word': least_frequent_word,
                       'most_frequent_word_amount': most_frequent_word_amount,
                       'least_frequent_word_amount': least_frequent_word_amount,
                       'word_dictionary': sorted(word_dictionary.items(), key=itemgetter(1), reverse=True)}

    return render(request, 'count.html', info_about_text)


def about_page(request):
    return render(request, 'about_page.html')
