diff --git a//dev/null b/agent.py
index 0000000000000000000000000000000000000000..551a521d0cfcba445831b72e5e882c07592abebd 100644
--- a//dev/null
+++ b/agent.py
@@ -0,0 +1,18 @@
+#!/usr/bin/env python3
+"""Simple agent utility to read the AGENTS instructions."""
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
