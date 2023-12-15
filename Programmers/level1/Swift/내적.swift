import Foundation

func solution(_ a:[Int], _ b:[Int]) -> Int {
    var result: Int = 0
    for i in 0..<a.count {
        result += a[i]*b[i]
    }
    return result
}