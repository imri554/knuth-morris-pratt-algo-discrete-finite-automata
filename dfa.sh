# This example shell script directly calls the python interpreter
# on a hypothetical python script that will generate a DFA.
# It also passes the two arguments that this script is called with.
# The two arguments will be, in this order, the path (absolute or relative)
# to the sequence file and the name of the .dot file produced.
# You'll need to edit this file for the language of your choosing.
# Come to office hours if you need additional clarification.
python dfa.py ${1} ${2}
