import dendropy
from dendropy.calculate import treecompare
from dendropy import Tree

tns = dendropy.TaxonNamespace()
tree1 = Tree.get_from_path(
    "D:\\Code Templates\\Python Templates\\Bioinformatics-Assignement\\output\\efflux_transporter_outer_membrane_subu_tree.nex", "nexus",
    taxon_namespace=tns)
tree2 = Tree.get_from_path(
    "D:\\Code Templates\\Python Templates\\Bioinformatics-Assignement\\output"
    "\\helix-turn-helix_domain-containing_pro_tree.nex",
    "nexus", taxon_namespace=tns)

tree1.encode_bipartitions()
tree2.encode_bipartitions()
print(treecompare.weighted_robinson_foulds_distance(tree1, tree2))