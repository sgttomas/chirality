import Foundation
import AppKit
import CoreGraphics
import ApplicationServices
// Exact PID only. No global app or window inventory.
guard CommandLine.arguments.count == 3, let pid = Int32(CommandLine.arguments[1]), let app = NSRunningApplication(processIdentifier: pid) else { fatalError("Owned PID required") }
let expected = CommandLine.arguments[2]
guard app.bundleIdentifier == expected else { fatalError("Bundle identity mismatch") }
let windows = (CGWindowListCopyWindowInfo(.optionAll, kCGNullWindowID) as? [[String:Any]] ?? []).filter { ($0[kCGWindowOwnerPID as String] as? Int32) == pid }
let result: [String:Any] = ["pid":pid, "bundleIdentifier": app.bundleIdentifier ?? "", "bundleURL":app.bundleURL?.path ?? "", "executableURL":app.executableURL?.path ?? "", "accessibilityTrusted":AXIsProcessTrusted(), "windows": windows]
print(String(data:try JSONSerialization.data(withJSONObject:result,options:[.prettyPrinted,.sortedKeys]),encoding:.utf8)!)
