import dendropy
from dendropy.calculate import treecompare
from dendropy import Tree
import os

protein_dir_set = []
for i in os.listdir('../output'):
    if "nex" in i.split("."):
        protein_dir_set.append(str(i))

tns = dendropy.TaxonNamespace()
for i in range(0,len(protein_dir_set)):
    for j in range(i+1,len(protein_dir_set)):
        tree1 = Tree.get_from_path(
            "../output/"+ protein_dir_set[i], "nexus",
            taxon_namespace=tns)
        tree2 = Tree.get_from_path(
            "../output/"+protein_dir_set[j],
            "nexus", taxon_namespace=tns)

        tree1.encode_bipartitions()
        tree2.encode_bipartitions()
        print(protein_dir_set[i], protein_dir_set[j], treecompare.unweighted_robinson_foulds_distance(tree1, tree2))