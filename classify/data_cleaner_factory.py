'''

INPUT: string --> data cleaner
OUTPUT: subclass instance of DataCleaner

'''

from classify.data_cleaners.edx_confusion import EdxConfusion
from classify.data_cleaners.edx_sentiment import EdxSentiment
from classify.data_cleaners.edx_urgency import EdxUrgency
from classify.data_cleaners.edx_answer import EdxAnswer
from classify.data_cleaners.edx_opinion import EdxOpinion
from classify.data_cleaners.edx_question import EdxQuestion


supported_data_cleaners='\nconfusion\nsentiment\nurgency\n' \
                        'opinion\nquestion\nanswer'
def make_data_cleaner(dc, binary=False,
                          extract_noun_phrases=False,
                          first_sentence_weight=1):
    dc = dc.lower()
    if dc == 'confusion':
        return EdxConfusion(binary=binary,
                            extract_noun_phrases=extract_noun_phrases,
                            first_sentence_weight=first_sentence_weight)
    elif dc == 'sentiment':
        return EdxSentiment(binary=binary,
                            extract_noun_phrases=extract_noun_phrases,
                            first_sentence_weight=first_sentence_weight)
    elif dc == 'urgency':
        return EdxUrgency(binary,
                          extract_noun_phrases=extract_noun_phrases,
                          first_sentence_weight=first_sentence_weight)
    elif dc == 'opinion':
        return EdxOpinion(extract_noun_phrases=extract_noun_phrases,
                          first_sentence_weight=first_sentence_weight)
    elif dc == 'question':
        return EdxQuestion(extract_noun_phrases=extract_noun_phrases,
                          first_sentence_weight=first_sentence_weight)
    elif dc == 'answer':
        return EdxAnswer(extract_noun_phrases=extract_noun_phrases,
                         first_sentence_weight=first_sentence_weight)
    else:
        raise NotImplementedError('DataCleaner %s not supported; choose from:'
                                  '%s' % (dc, supported_data_cleaners))
