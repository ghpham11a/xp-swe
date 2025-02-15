#include <vector>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution 
{
public:
    std::vector<std::vector<int>> LevelOrder(TreeNode* Root) 
    {
        std::vector<std::vector<int>> Output;

        if (Root == NULL)
        {
            return Output;
        }

        Recurse(Root, Output, 0);

        return Output;
    }

    void Recurse(TreeNode* Node, std::vector<std::vector<int>>& Output, int Level)
    {
        if (Output.size() == Level)
        {
            std::vector<int> InitLevel;
            Output.push_back(InitLevel);
        }

        Output[Level].push_back(Node->val);

        if (Node->left != NULL)
        {
            Recurse(Node->left, Output, Level + 1);
        }

        if (Node->right != NULL)
        {
            Recurse(Node->right, Output, Level + 1);
        }
    }
};