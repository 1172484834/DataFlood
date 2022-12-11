from treelib import Tree

def plotTree(list, topic):
    tree = Tree()
    temp = list[0].split('->')
    tag = ('[[' + temp[0] + ']]') if (temp[0] == topic) else temp[0]
    tree.create_node(tag=tag, identifier=temp[0])
    for i in range(len(list)):
        if list[i] != '-->':
            temp = list[i].split('->')
            tag = ('[[' + temp[1] + ']]') if (temp[1] == topic) else temp[1]
            tree.create_node(tag=tag, identifier=temp[1], parent=temp[0])
    tree.show()
