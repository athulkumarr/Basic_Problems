# Trie Implementation

Trie is an efficient information reTrieval data structure. Using Trie, search complexities can be brought to optimal limit (key length). 

If we store keys in binary search tree, a well balanced BST will need time proportional to M * log N, where M is maximum string length and N is number of keys in tree. 

Using Trie, we can search the key in O(M) time. However the penalty is on Trie storage requirements

![Image](trie.png)

# Implement the Trie class:

    Trie() Initializes the trie object.

    void insert(String word) Inserts the string word into the trie.

    boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.

    boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
