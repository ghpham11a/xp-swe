package main

type Node struct {
    children map[rune]*Node
    isEnd    bool
}

type Trie struct {
    root *Node
}

func NewNode() *Node {
    return &Node{children: make(map[rune]*Node)}
}

func NewTrie() *Trie {
    return &Trie{root: NewNode()}
}

func (t *Trie) Insert(word string) {
    currNode := t.root
    for _, char := range word {
        if _, ok := currNode.children[char]; !ok {
            currNode.children[char] = NewNode()
        }
        currNode = currNode.children[char]
    }
    currNode.isEnd = true
}

func (t *Trie) Delete(word string) bool {
    currNode := t.root
    parents := []*Node{currNode}
    for _, char := range word {
        if _, ok := currNode.children[char]; !ok {
            return false
        }
        currNode = currNode.children[char]
        parents = append(parents, currNode)
    }

    currNode.isEnd = false

    parents = parents[:len(parents)-1]

    for i := len(parents) - 1; i > 0; i-- {
        parent := parents[i]
        char := rune(word[i])
        if !parent.children[char].isEnd && len(parent.children[char].children) == 0 {
            delete(parent.children, char)
        }
    }

    return true
}

func (t *Trie) Search(word string) bool {
    currNode := t.root
    for _, char := range word {
        if _, ok := currNode.children[char]; !ok {
            return false
        }
        currNode = currNode.children[char]
    }
    return currNode.isEnd
}

func main() {
    trie := NewTrie()
    trie.Insert("hello")
    println(trie.Search("hello"))  // true
    println(trie.Search("hell"))   // false
    trie.Delete("hello")
    println(trie.Search("hello"))  // false
}