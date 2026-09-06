import Foundation
import CoreGraphics
let a=CommandLine.arguments
let start=CGPoint(x:Double(a[1])!,y:Double(a[2])!)
CGEvent(mouseEventSource:nil,mouseType:.mouseMoved,mouseCursorPosition:start,mouseButton:.left)?.post(tap:.cghidEventTap)
CGEvent(mouseEventSource:nil,mouseType:.leftMouseDown,mouseCursorPosition:start,mouseButton:.left)?.post(tap:.cghidEventTap)
Thread.sleep(forTimeInterval:0.3)
if a.count == 5 { let end=CGPoint(x:Double(a[3])!,y:Double(a[4])!);for n in 1...40 {let t=Double(n)/40;CGEvent(mouseEventSource:nil,mouseType:.leftMouseDragged,mouseCursorPosition:CGPoint(x:start.x+(end.x-start.x)*t,y:start.y+(end.y-start.y)*t),mouseButton:.left)?.post(tap:.cghidEventTap);Thread.sleep(forTimeInterval:0.025)};Thread.sleep(forTimeInterval:0.5);CGEvent(mouseEventSource:nil,mouseType:.leftMouseUp,mouseCursorPosition:end,mouseButton:.left)?.post(tap:.cghidEventTap)}else {CGEvent(mouseEventSource:nil,mouseType:.leftMouseUp,mouseCursorPosition:start,mouseButton:.left)?.post(tap:.cghidEventTap)}
print("Native mouse operation",Array(a.dropFirst()))
