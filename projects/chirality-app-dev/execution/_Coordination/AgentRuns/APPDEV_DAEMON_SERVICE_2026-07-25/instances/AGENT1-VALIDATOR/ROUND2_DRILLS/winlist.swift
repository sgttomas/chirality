import CoreGraphics
import Foundation
let opts = CGWindowListOption(arrayLiteral: .optionOnScreenOnly, .excludeDesktopElements)
guard let list = CGWindowListCopyWindowInfo(opts, kCGNullWindowID) as? [[String: Any]] else { exit(1) }
let target = CommandLine.arguments.count > 1 ? CommandLine.arguments[1] : ""
for w in list {
  let owner = (w[kCGWindowOwnerName as String] as? String) ?? ""
  let pid = (w[kCGWindowOwnerPID as String] as? Int) ?? -1
  let num = (w[kCGWindowNumber as String] as? Int) ?? -1
  let name = (w[kCGWindowName as String] as? String) ?? ""
  let b = (w[kCGWindowBounds as String] as? [String: Any]) ?? [:]
  let layer = (w[kCGWindowLayer as String] as? Int) ?? -99
  if target.isEmpty || owner.contains(target) || String(pid) == target {
    print("\(num)\t\(pid)\t\(layer)\t\(owner)\t\(name)\tX=\(b["X"] ?? "?") Y=\(b["Y"] ?? "?") W=\(b["Width"] ?? "?") H=\(b["Height"] ?? "?")")
  }
}
