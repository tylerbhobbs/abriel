 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/AGENTS.md b/AGENTS.md
index 7d78602b0ab4f1462e6d12d6a26a6c04777aef29..8dc8eb382bd8fd533011dcb5c68af369b5ccccd1 100644
--- a/AGENTS.md
+++ b/AGENTS.md
@@ -1 +1,4 @@
-##agent data here
+# Abriel Repository Instructions
+
+This repository contains a few demonstration files.
+Run `python3 agent.py` to display these instructions.
 
EOF
)
