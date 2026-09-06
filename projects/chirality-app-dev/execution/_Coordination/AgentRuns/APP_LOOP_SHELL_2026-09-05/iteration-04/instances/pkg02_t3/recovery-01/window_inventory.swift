import Foundation
import CoreGraphics
let names = Set(["Chirality", "Electron", "Preview", "Microsoft Word", "Microsoft Excel", "Microsoft PowerPoint", "Finder"])
let windows = CGWindowListCopyWindowInfo(.optionAll, kCGNullWindowID) as? [[String:Any]] ?? []
let filtered = windows.filter { names.contains($0[kCGWindowOwnerName as String] as? String ?? "") }
let data = try JSONSerialization.data(withJSONObject: filtered, options: [.prettyPrinted, .sortedKeys])
print(String(data:data,encoding:.utf8)!)
