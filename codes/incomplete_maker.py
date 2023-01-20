import imp
import random
import time

import warnings

from codes.parameters import RANGE_SEPARATOR
from codes.utils.gt import get_taxa_list_from_gt

import dendropy
from dendropy import Tree
from dendropy import TreeList

from codes.utils.file import create_file_abs

def get_deleted_taxa_without_removing_one(gt, count, preserved_taxon):
    taxa_list = get_taxa_list_from_gt(gt)
    assert len(taxa_list) >= count, "can't delete " + count + " taxa from " + len(taxa_list)
    indexes = random.sample(range(0, len(taxa_list)), count)

    ret = []

    for i in indexes:
        if taxa_list[i] != preserved_taxon:
            ret.append(taxa_list[i])
    return ret

def get_deleted_taxa(gt, count):
    taxa_list = get_taxa_list_from_gt(gt)
    assert len(taxa_list) >= count, "can't delete " + count + " taxa from " + len(taxa_list)
    indexes = random.sample(range(0, len(taxa_list)), count)
    # warnings.warn("how on earth this is conserving one taxa ??? --> need discussion ")

    ret = []

    for i in indexes:
        ret.append(taxa_list[i])
    return ret


def get_bounds(range):
    """
    returns the higher and lower bound
    of a range

    both "1-2" or "1"

    returns (l_bound, h_bound)
    """
    # if RANGE_SEPARATOR in range:
    range = range.split(RANGE_SEPARATOR)

    assert len(range) <= 2, range + ' should not be in this form '

    return int(range[0]), int(range[-1])


def remove_taxa_from_gts(range, in_file, out_file):
    '''
    removes range of taxa from each gene tree
    range = "1-3"
    doesn't eliminates a taxa entirely from all gene trees 
    '''
    l_bound, h_bound = get_bounds(range=range)
    print('---------------', 'Pruning started ', in_file, ' ==> ', out_file, '( ', l_bound, '-', h_bound,
          ') ---------------')
    in_time = time.time()

    ###
    # the original one 
    # trees = dendropy.TreeList.get_from_path(treeName, 'newick',as_rooted=True,preserve_underscores=True)
    # as_rooted is critically deprecated
    # rooting is our new best friend
    ###
    trees = dendropy.TreeList.get_from_path(src=in_file, schema='newick', rooting='force-rooted',
                                            preserve_underscores=True)
    
    # find preserved taxa
    gt = trees[0].__str__()
    taxa_list = get_taxa_list_from_gt(gt)
    preserved_taxa_idx = random.randint(0, len(taxa_list) - 1)
    preserved_taxa = taxa_list[preserved_taxa_idx]

    create_file_abs(out_file)
    with open(out_file, 'w') as f:
        for tree in trees:
            pruned_tree = dendropy.Tree(tree)

            num_deletion = random.randint(l_bound, h_bound)

            ###         gt = tree.as_newick_string()

            gt = tree.__str__()

            taxon_set = get_deleted_taxa(gt, num_deletion)
            # taxon_set = get_deleted_taxa_without_removing_one(gt, num_deletion, preserved_taxa)

            ###        prTree.prune_taxa_with_labels(taxon_sets, update_splits=True, delete_outdegree_one=True)        
            pruned_tree.prune_taxa_with_labels(taxon_set)

            s = pruned_tree.__str__()

            # s = bytes(s, encoding='UTF-8')

            # print(gt, taxon_set, s)

            f.write(s)

            f.write(';\n')

    time_required = int(time.time() - in_time)
    print('---------------', 'Pruning done ', time_required, 's ', in_file, ' ==> ', out_file, '( ', l_bound, '-',
          h_bound, ') ---------------')
