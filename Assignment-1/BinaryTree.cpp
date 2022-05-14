#include <iostream>
#include <queue>

using namespace std;

class Node
{
private:
    int data;
    Node *left;
    Node *right;

public:
    Node()
    {
        data = 0;
        left = nullptr;
        right = nullptr;
    }
    Node(int data)
    {
        this->data = data;
        left = nullptr;
        right = nullptr;
    }
    friend class BinaryTree;
};

class BinaryTree
{
private:
    Node *root;

public:
    BinaryTree()
    {
        root = nullptr;
    }

    void CreateTree()
    {
        this->root = CreateNode();
    }
    void dfs(Node *curNode)
    {
        if (curNode == nullptr)
            return;
        cout << curNode->data << " ";
        dfs(curNode->left);
        dfs(curNode->right);
    }

    void bfs()
    {
        if (root == nullptr)
            return;
        queue<Node *> q;
        Node *curNode = root;
        q.push(curNode);
        while (!q.empty())
        {
            curNode = q.front();
            q.pop();
            cout << curNode->data << endl;
            if (curNode->left != nullptr)
            {
                q.push(curNode->left);
            }
            if (curNode->right != nullptr)
            {
                q.push(curNode->right);
            }
        }
    }
    Node *CreateNode()
    {
        int val;
        cout << "Enter Value of the Node: ";
        cin >> val;
        Node *node = new Node(val);
        cout << "Do you want to create Left Child of " << node->data << " (1/0): ";
        cin >> val;
        if (val)
            node->left = CreateNode();
        cout << "Do you want to create Right Child of " << node->data << " (1/0): ";
        cin >> val;
        if (val)
            node->right = CreateNode();
        return node;
    }
    Node *getroot()
    {
        return root;
    }
};

int main()
{
    BinaryTree bt = BinaryTree();
    bt.CreateTree();
    cout << "DFS: ";
    bt.dfs(bt.getroot());
    cout << endl;
    cout << "BFS: ";
    bt.bfs();
    cout << endl;
    return 0;
}

/*
1
1
2
1
4
1
7
0
0
1
8
0
0
1
5
0
0
1
3
1
9
0
0
0
            1   
        2       3
    4     5   9
7       8
    */