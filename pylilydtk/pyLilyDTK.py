import commands 
import sys
import optparse
import datetime

from django.conf import settings

rhythm_in = ''
input_rhythm = ''
input_file = ''
out_file = ''
time_signature = ''
process_dir = settings.PYLILY_DIR

def get_input_file(file_name):
    print "Opening input file..."
    global input_file
    input_file = file_name
    in_line = open(file_name, 'r').readline().strip()
    return in_line

def set_rhythm(in_line):
    global rhythm_in
    global time_signature
    in_line = in_line.split(',')
    time_signature = in_line[0]
    rhythm_in = in_line[1]
    rhythm_in = parse_rhythm(rhythm_in)

def process_template():
    print "Processing rhythm and creating lilypond file..."
    template = open(process_dir + 'template.ly', 'r')
    global out_file
    out_file = input_file.replace('.txt', '.ly')
    output = open(out_file, 'w')
    for line in template:
        if line == 'RHYTHM\n':
            line = line.replace('RHYTHM', rhythm_in)
        elif line == '\\time TIME_SIGNATURE\n':
            line = '\\time ' + time_signature + '\n'
        output.writelines(line)
    template.close()
    output.flush()
    output.close()
    
def make_score():
    """
    calls lilypond to create the score.
    commmands.getoutput supports only linux/osx
    """
    print commands.getoutput('lilypond -o ' + process_dir + ' -dpreview %s' % out_file)

def reduce_length(length):
    if length > 4:
        length -= 4
    return length

def parse_rhythm(rhythm_in):
    """
    for input: D-T-tkD-D-tkT-tk
    expected result is: c8-"D" c8-"T" c16-"t" c16-"k" c8-"D" c8-"D" c16-"t" c16-"k" c8-"T" c16-"t" c16-"k"
    """
    print "Parsing the rhythm..."
    rhythm_in = rhythm_in 
    rhythm_out = ''
    tone = ''
    length = 16
    strike = ''
    first_pass = True
    extend_note = False
    for x in rhythm_in:
        if first_pass:
            if x in ('-', '_'):
                tone = 'r'
                strike = ''
            else:
                tone = 'c'
                strike = x
            first_pass = False
        else:
            if x == '-':
                length = reduce_length(length)
                extend_note = True
            else:
                if extend_note:
                    length = reduce_length(length)
                    extend_note = False
                rhythm_out += tone + str(length) + '-"' + strike + '" '
                if x == '_':
                    tone = 'r'
                    strike = ''
                else:
                    tone = 'c'
                    strike = x
                length = 16
    if rhythm_in[-1] == '-':
        length = reduce_length(length)
    rhythm_out += tone + str(length) + '-"' + strike + '" '
    return rhythm_out

def clean_up_files():
    print 'Deleting extra files...'
    commands.getoutput('rm ' + process_dir + '*.pdf')
    commands.getoutput('rm ' + process_dir + '*.ps')
    commands.getoutput('rm ' + process_dir + '*.eps')
    commands.getoutput('rm ' + out_file)


if __name__ == '__main__':

    parser = optparse.OptionParser()
    parser.add_option('-r', '--rhythm', help='Alows you to enter a rhythm as a command line argument.', dest='rhythm', action='store')
    parser.add_option('-f', '--file', help='Allows you to enter the name of an input file.', dest='file_name', action='store')
    (opts, args) = parser.parse_args()

    if opts.rhythm:
        input_file = str(datetime.datetime.now().microsecond) + '.txt'
        set_rhythm(opts.rhythm)
    elif opts.file_name:
        set_rhythm(get_input_file(opts.file_name))
    else:
        sys.stderr.write("Enter 'pyLilyDTK --help' for usage instructions\n")
        raise SystemExit(1)

    process_template()
    make_score()
    clean_up_files()
    print 'Conversion complete.'
