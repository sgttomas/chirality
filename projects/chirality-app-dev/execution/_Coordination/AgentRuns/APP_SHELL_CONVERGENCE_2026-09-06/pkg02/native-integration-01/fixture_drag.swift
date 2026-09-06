import Foundation
import CoreGraphics
let start=CGPoint(x:90,y:232), end=CGPoint(x:550,y:646)
CGEvent(mouseEventSource:nil,mouseType:.mouseMoved,mouseCursorPosition:start,mouseButton:.left)?.post(tap:.cghidEventTap)
CGEvent(mouseEventSource:nil,mouseType:.leftMouseDown,mouseCursorPosition:start,mouseButton:.left)?.post(tap:.cghidEventTap)
Thread.sleep(forTimeInterval:0.3)
for n in 1...30 {let t=Double(n)/30;let p=CGPoint(x:start.x+(end.x-start.x)*t,y:start.y+(end.y-start.y)*t);CGEvent(mouseEventSource:nil,mouseType:.leftMouseDragged,mouseCursorPosition:p,mouseButton:.left)?.post(tap:.cghidEventTap);Thread.sleep(forTimeInterval:0.025)}
Thread.sleep(forTimeInterval:0.5)
CGEvent(mouseEventSource:nil,mouseType:.leftMouseUp,mouseCursorPosition:end,mouseButton:.left)?.post(tap:.cghidEventTap)
print("Native Finder fixture drag from (90,232) to (550,646) completed")
