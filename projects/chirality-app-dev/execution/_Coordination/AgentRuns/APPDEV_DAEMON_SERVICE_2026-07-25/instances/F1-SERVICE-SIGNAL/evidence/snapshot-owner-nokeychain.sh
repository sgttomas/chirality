#!/bin/zsh
# Read-only snapshot of the operator's live state. No writes anywhere outside $1.
out="$1"
{
  echo "captured: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "--- owner LaunchAgent plist ---"
  ls -la "$HOME/Library/LaunchAgents/" 2>&1
  shasum -a 256 "$HOME/Library/LaunchAgents/com.chirality.runtime.plist" 2>&1
  stat -f '%m %z %N' "$HOME/Library/LaunchAgents/com.chirality.runtime.plist" 2>&1
  echo "--- owner job ---"
  launchctl print gui/501/com.chirality.runtime 2>&1 | grep -E '^\s*(state|runs|last exit code|pid|program) ' 2>&1
  echo "--- owner launcher ---"
  shasum -a 256 "$HOME/.local/bin/chirality" 2>&1
  stat -f '%m %z %Sp' "$HOME/.local/bin/chirality" 2>&1
  stat -f '%Sp %N' "$HOME/.local/bin" 2>&1
  echo "--- owner userData (2 levels) ---"
  stat -f '%m %N' "$HOME/Library/Application Support/chirality-frontend" 2>&1
  find "$HOME/Library/Application Support/chirality-frontend" -maxdepth 2 -exec stat -f '%m %z %N' {} \; 2>&1 | sort
  echo "--- chirality processes ---"
  pgrep -fl 'Chirality' 2>&1 || echo "(none)"
} > "$out" 2>&1
