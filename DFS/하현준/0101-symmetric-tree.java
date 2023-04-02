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
    public boolean isSymmetric(TreeNode root) {
        return check(root.left, root.right);
    }

    private boolean check(TreeNode node1, TreeNode node2) {
        if (node1 == null && node2 == null) {
            return true;
        }
        if (node1 == null || node2 == null) {
            return false;
        }
        if (node1.val == node2.val) {
            return check(node1.left, node2.right) && check(node1.right, node2.left);
        }
        

        return false;
    }
}

/** 멍청한 풀이 
class Solution {
    private Map<Integer, List<Integer>> map = new HashMap<>();
    private int lastDepth = -1;
    private int depth = 1;

    public boolean isSymmetric(TreeNode root) {
        dfs(root);
        if (lastDepth != map.get(lastDepth).size()) {
            map.remove(lastDepth);
        }
        System.out.println(map);
        for (List<Integer> value : map.values()) {
            int size = value.size();
            for (int i = 0; i < size / 2; i++) {
                if (value.get(i) != value.get(size - 1 - i)) {
                    return false;
                }
            }
        }
        return true;
    }

    private void dfs(TreeNode node) {
        if (node == null) {
            map.putIfAbsent(depth, new ArrayList<>());
            map.computeIfPresent(depth, (k, v) -> {
                v.add(null);
                return v;
            });
            return;
        }

        map.putIfAbsent(depth, new ArrayList<>());
        map.computeIfPresent(depth, (k, v) -> {
            v.add(node.val);
            return v;
        });

        depth *= 2;
        lastDepth = Math.max(lastDepth, depth);
        dfs(node.left);
        dfs(node.right);
        depth /= 2;
    }
}

 */