import Foundation

func solution(_ absolutes:[Int], _ signs:[Bool]) -> Int {
    var result: Int = 0
    for i in 0..<absolutes.count {
        if(signs[i]) {
            result += absolutes[i]
        } else {
            result -= absolutes[i]
        }
    }
    return result
}