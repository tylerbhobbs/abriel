 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/agent.py b/agent.py
index 2d4a5c5be90c6d8af2a0d4efe59087da8d488df7..fa127843a728881c3be9e43225588aa776fb3dfd 100644
--- a/agent.py
+++ b/agent.py
@@ -1,23 +1,18 @@
-diff --git a//dev/null b/agent.py
-index 0000000000000000000000000000000000000000..551a521d0cfcba445831b72e5e882c07592abebd 100644
---- a//dev/null
-+++ b/agent.py
-@@ -0,0 +1,18 @@
-+#!/usr/bin/env python3
-+"""Simple agent utility to read the AGENTS instructions."""
-+
-+from pathlib import Path
-+
-+
-+def read_agents_file(path: str = "AGENTS.md") -> str:
-+    """Return the contents of the AGENTS file."""
-+    return Path(path).read_text()
-+
-+
-+def main() -> None:
-+    """Print the AGENTS instructions."""
-+    print(read_agents_file())
-+
-+
-+if __name__ == "__main__":
-+    main()
+#!/usr/bin/env python3
+"""Utility to display repository instructions."""
+
+from pathlib import Path
+
+
+def read_agents_file(path: str = "AGENTS.md") -> str:
+    """Return the contents of the AGENTS file."""
+    return Path(path).read_text()
+
+
+def main() -> None:
+    """Print the AGENTS instructions."""
+    print(read_agents_file())
+
+
+if __name__ == "__main__":
+    main()
 
EOF
)
