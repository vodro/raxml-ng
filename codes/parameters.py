import os
from .utils.file import join_dir

# taxa removal from each gene tree
# REMOVED_TAXA_RANGE = ['1-2', '3-4', '5-6', '7-8', '9-10', '11-12', '13-14', '15-16', '17-18', '19-20', '21-22', '23-24', '25-26', '27-28', '29-30']
REMOVED_TAXA_RANGE = ['15-18']
RANGE_SEPARATOR = '-'

# === constants
NUM_TREES = 200
NUM_TAXA = 37
NUM_ORIENTATION = 3

# input output folders
INPUT_FOLDER = 'in'
OUTPUT_FOLDER = 'out'
WORKING_FOLDER = 'tmp'
TRUE_FOLDER = 'true'
CODES_FOLDER = 'codes'
TERRACE_OUTPUT_FOLDER = 'terrace_output'
SCRIPT_FOLDER = join_dir(CODES_FOLDER, 'scripts')
STATS_FOLDER = join_dir(OUTPUT_FOLDER, 'stats')
SCRIPT_FOLDER_DEPTH = 2

INPUT_FOLDER = join_dir(os.getcwd(), INPUT_FOLDER)
OUTPUT_FOLDER = join_dir(os.getcwd(), OUTPUT_FOLDER)
WORKING_FOLDER = join_dir(os.getcwd(), WORKING_FOLDER)
SCRIPT_FOLDER = join_dir(os.getcwd(), SCRIPT_FOLDER)
CODES_FOLDER = join_dir(os.getcwd(), CODES_FOLDER)

COMPLETE = 'complete'
INCOMPLETE = 'incomplete'

# IMPUTED = 'imputed'
PREDICTED = 'predicted'
PREDICTED_WITH_THRESHOLD = 'predicted_with_threshold'
PREDICTED_WITH_DISTRIBUTION = 'predicted_with_distribution'

# IMPUTED_LIST = [IMPUTED, PREDICTED,  PREDICTED_WITH_THRESHOLD, PREDICTED_WITH_DISTRIBUTION]
# IMPUTED_LIST = [IMPUTED, PREDICTED]
IMPUTED_LIST = []

# MODES_LIST = [COMPLETE, INCOMPLETE]
MODES_LIST = [INCOMPLETE]


# tree extension
GENE_TREE_SET_EXTENSION = '.tre'
NUMPY_EXTENSION = '.npy'
QUARTETS_EXTENSION = '.qrts'

GENE_TREE = 'gt'

ASTRAL = 'astral'
WQFM = 'wQFM'
# METHODS = [WQFM]
METHODS = [ASTRAL]

FOUR_TAXA_MAP = 'map'

NUMPY_ARRAY = 'numpy'
QUARTETS = 'quartets'

SM_ASTRAL = 1
SM_wQFM = 2
SM_wQFC = 3

THRESHOLD_OF_REFUSE_PREDICTION = 0.70
