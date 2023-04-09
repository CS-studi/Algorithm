class Solution {
    private final List<TreeNode> visited = new ArrayList<>();
    private List<TreeNode> lca = new ArrayList<>();
    private List<TreeNode> lca2 = new ArrayList<>();

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        dfs(root, root, p, q);
        int size = Math.min(lca.size(), lca2.size());
        TreeNode node = null;
        for (int i = 0; i < size; i++) {
            if (lca.get(i).val == lca2.get(i).val) {
                node = lca.get(i);
            } else {
                break;
            }
        }
        return node;
    }

    private void dfs(TreeNode ancestor, TreeNode now, TreeNode p, TreeNode q) {
        if (!lca.isEmpty() && !lca2.isEmpty()) {
            return;
        }
        if (now == null) {
            return;
        }

        if (visited.contains(now)) {
            return;
        }

        visited.add(now);
        if (p.val == now.val) {
            lca = new ArrayList<>(visited);
        }
        if (q.val == now.val) {
            lca2 = new ArrayList<>(visited);
        }
        dfs(now, now.left, p, q);
        dfs(now, now.right, p, q);
        visited.remove(now);
    }
}