/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode() {}
 * TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) {
 * this.val = val;
 * this.left = left;
 * this.right = right;
 * }
 * }
 */
class Solution {
    private final List<Integer> answer = new ArrayList<>();

    public List<Integer> preorderTraversal(TreeNode root) {
        preorder(root);
        return answer;
    }

    private void preorder(TreeNode node) {
        if (Objects.isNull(node)) {
            return;
        }

        answer.add(node.val);
        preorder(node.left);
        preorder(node.right);
    }
}