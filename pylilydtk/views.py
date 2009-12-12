import commands
import datetime

from django.conf import settings
from django.shortcuts import render_to_response

import pyLilyDTK

def pylily(request):
    query = request.GET.get('q', '')
    score = ''
    process_dir = settings.PYLILY_DIR
    commands.getoutput('rm ' + process_dir + '*.png')
    if query:
        score = str(datetime.datetime.now().microsecond) + '.txt'
        pyLilyDTK.input_file = process_dir + score
        score = score.replace('.txt', '.preview.png')
        pyLilyDTK.set_rhythm(query)
        pyLilyDTK.process_template()
        pyLilyDTK.make_score()
        pyLilyDTK.clean_up_files()
    return render_to_response('pylily.html', {'score': score, 'query':query})

