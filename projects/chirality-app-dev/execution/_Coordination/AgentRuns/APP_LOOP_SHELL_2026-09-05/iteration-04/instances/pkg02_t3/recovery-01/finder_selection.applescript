tell application "Finder"
set output to ""
repeat with selectedItem in (get selection)
set output to output & (POSIX path of (selectedItem as alias)) & linefeed
end repeat
return output
end tell
